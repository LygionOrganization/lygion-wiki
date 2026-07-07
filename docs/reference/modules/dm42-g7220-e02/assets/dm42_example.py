from lygion_devs_py.lydevs_sdk import *
import time


# TTL Encoder E02 的设备 ID，用于读取关节输出端的绝对角度。
# 请改成你在 FD 中为编码器保存的实际 ID。
ENCODER_ID = 2

# 关节步进电机对应的 TTL Stepper Driver (A) 设备 ID。
# 请改成你在 FD 中为驱动器保存的实际 ID。
JOINT_DRIVER_ID = 1

# 请根据 TTL Adapter (A) 在当前系统中的实际串口名称修改。
# 示例：Windows 为 "COM3"，Linux 为 "/dev/ttyUSB0"，macOS 为 "/dev/cu.usbserial-xxxx"。
PORT_NAME = "COM18"

# TTL 总线默认波特率。
BAUDRATE = 1000000

# DM42-G7220-E02 的传动比：
# 72 / 20 为同步带传动级减速比，5.181818182 为 4240BY-G5.2 电机减速器减速比。
RATIO = (72 / 20) * 5.181818182

# E02 编码器单圈位置范围为 0~4095。
ENCODER_ONE_CIRCLE = 4096

# FD 中位校准后，关节机械中位通常对应编码器读数 2047 或 2048。
# 如果你的设备在机械中位读到的是其它值，请改成实测中位读数。
ENCODER_CENTER = 2048

# TTL Stepper Driver (A) 默认 1/32 微步时，电机轴单圈对应 3200 个位置计数。
STEPPER_ONE_CIRCLE = 3200

# 关节输出端转一圈对应的电机位置计数。
JOINT_TOTAL_STEPS = STEPPER_ONE_CIRCLE * RATIO

# 关节机械中位对应的电机位置值。
JOINT_MID = int(JOINT_TOTAL_STEPS / 2)

# 程序中 0° 目标角度对应的电机位置。
JOINT_ZERO = int(JOINT_TOTAL_STEPS)

# 关节弧度值到电机位置值的换算系数。
RAD2STEPS = JOINT_TOTAL_STEPS / (2 * 3.1415926)

# 编码器每变化 1 个计数，对应的电机位置变化量。
ENCODER2STEPS = JOINT_TOTAL_STEPS / ENCODER_ONE_CIRCLE

# 第一次测试建议使用较低速度和非 0 加速度。
JOINT_SPEED = 400
JOINT_ACC = 15

# 相电流参数。
# 相电流(A) 约等于 3.3 * 2 * (current / 1000)。
# current = 200 时，相电流约为 1.32 A。
MOTOR_CURRENT = 200


portHandler = PortHandler(PORT_NAME)
packetHandler = TTLSDClass(portHandler)

if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    quit()

if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()


def set_position(device_id, position):
    """将驱动器当前位置校准为指定位置值。

    DM42-G7220-E02 使用步进电机驱动，驱动器上电后不知道关节输出端的绝对角度。
    上电初始化时，程序先读取 E02 编码器，再把驱动器当前位置同步为对应的位置值。
    """
    scs_comm_result, scs_error = packetHandler.reOfsCal(device_id, position)
    if scs_comm_result != COMM_SUCCESS:
        print(packetHandler.getTxRxResult(scs_comm_result))
        return False
    if scs_error != 0:
        print(packetHandler.getRxPacketError(scs_error))
        return False

    print("[ID:%03d] position synchronized to %d" % (device_id, position))
    return True


def read_position_speed(device_id):
    """读取 TTL 总线设备的当前位置和当前速度。

    对 DM42-G7220-E02，通常用该函数读取 E02 编码器的绝对位置。
    """
    present_position, present_speed, scs_comm_result, scs_error = packetHandler.ReadPosSpeed(device_id)
    if scs_comm_result != COMM_SUCCESS:
        print(packetHandler.getTxRxResult(scs_comm_result))
        return None
    if scs_error != 0:
        print(packetHandler.getRxPacketError(scs_error))
        return None
    return [present_position, present_speed]


def joint_init(encoder_id, driver_id):
    """根据编码器绝对位置同步关节电机驱动器当前位置。"""
    encoder_state = read_position_speed(encoder_id)
    if encoder_state is None:
        raise RuntimeError("Failed to read joint encoder position")

    encoder_position = encoder_state[0]
    # 编码器已经在 FD 中完成中位校准，这里只计算当前读数相对中位的偏移。
    encoder_delta = encoder_position - ENCODER_CENTER
    motor_position = round(JOINT_MID + encoder_delta * ENCODER2STEPS)
    motor_position = max(0, min(65534, motor_position))

    print(
        "encoder_position=%d, encoder_delta=%d, motor_position=%d"
        % (encoder_position, encoder_delta, motor_position)
    )
    return set_position(driver_id, int(motor_position))


def joint_position_ctrl(device_id, position, speed, acc, current):
    """使用位置模式控制关节电机驱动器。"""
    position = max(0, min(65534, int(position)))
    scs_comm_result, scs_error = packetHandler.WritePosEx(device_id, position, speed, acc, current)
    if scs_comm_result != COMM_SUCCESS:
        print(packetHandler.getTxRxResult(scs_comm_result))
        return False
    if scs_error != 0:
        print(packetHandler.getRxPacketError(scs_error))
        return False
    return True


def joint_rad_ctrl(device_id, rad, speed, acc, current):
    """使用弧度值控制关节角度。"""
    position = int(rad * RAD2STEPS + JOINT_ZERO)
    return joint_position_ctrl(device_id, position, speed, acc, current)


def joint_deg_ctrl(device_id, deg, speed, acc, current):
    """使用角度值控制关节角度。"""
    rad = deg * 3.1415926 / 180
    print("joint target deg=%s" % deg)
    return joint_rad_ctrl(device_id, rad, speed, acc, current)


if __name__ == "__main__":
    # 第一次运行前，请固定执行器本体，并确认输出端附近没有线缆、手指或其它障碍物。

    # 上电后先同步驱动器当前位置，保证后续角度控制基准正确。
    joint_init(ENCODER_ID, JOINT_DRIVER_ID)

    # 依次转到 0°、+45°、-45°，最后回到 0°。
    joint_deg_ctrl(JOINT_DRIVER_ID, 0, JOINT_SPEED, JOINT_ACC, MOTOR_CURRENT)
    time.sleep(1.5)

    joint_deg_ctrl(JOINT_DRIVER_ID, 45, JOINT_SPEED, JOINT_ACC, MOTOR_CURRENT)
    time.sleep(1.5)

    joint_deg_ctrl(JOINT_DRIVER_ID, -45, JOINT_SPEED, JOINT_ACC, MOTOR_CURRENT)
    time.sleep(1.5)

    joint_deg_ctrl(JOINT_DRIVER_ID, 0, JOINT_SPEED, JOINT_ACC, MOTOR_CURRENT)
    print("DM42-G7220-E02 joint test finished")
