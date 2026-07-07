from lygion_devs_py.lydevs_sdk import *
import time


# TTL Encoder E02 的设备 ID，用于读取转向关节的绝对位置。
ENCODER_ID = 10
# 转向电机对应的 TTL Stepper Driver (A) 设备 ID。
TURNING_ID = 11
# 行走电机对应的 TTL Stepper Driver (A) 设备 ID。
WALKING_ID = 12

# 转向关节总减速比：
# 72 / 20 为同步带传动级减速比，5.181818182 为步进电机行星减速器减速比。
RATIO = (72 / 20) * 5.181818182

# 编码器单圈计数。
ENCODER_ONE_CIRCLE = 4096
# FD 中位校准后，转向机械中位通常对应编码器读数 2047 或 2048。
# 如果你的设备在机械中位读到的是其它值，请改成实测中位读数。
ENCODER_CENTER = 2048
# 步进电机驱动器中，电机轴单圈对应的微步数。
STEPPER_ONE_CIRCLE = 3200
# 转向关节输出端转一圈对应的电机位置计数。
JOINT_TOTAL_STEPS = STEPPER_ONE_CIRCLE * RATIO
# 转向关节中位对应的电机位置值。
JOINT_MID = int(JOINT_TOTAL_STEPS / 2)
# 程序中 0° 转向目标对应的电机位置。
STEERING_ZERO = int(JOINT_TOTAL_STEPS)
# 转向关节弧度值到电机位置值的换算系数。
RAD2STEPS = 1 / (2 * 3.1415926) * JOINT_TOTAL_STEPS
# 编码器每变化 1 个计数，对应的转向电机位置变化量。
ENCODER2STEPS = JOINT_TOTAL_STEPS / ENCODER_ONE_CIRCLE

# 请根据 TTL Adapter (A) 在当前系统中的实际串口名称修改。
# 示例：Windows 为 "COM3"，Linux 为 "/dev/ttyUSB0"，macOS 为 "/dev/cu.usbserial-xxxx"。
portHandler = PortHandler("COM18")
packetHandler = TTLSDClass(portHandler)

if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    quit()

if portHandler.setBaudRate(1000000):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()


def set_position(device_id, position):
    """将设备当前位置校准为指定位置值。

    SW69-TTL 的转向电机为开环步进系统，驱动器上电后并不知道真实机械角度。
    本函数用于在开机同步时，将转向电机驱动器的当前位置设置为编码器换算得到的位置值。
    编码器中位已在 FD 软件中完成校准，因此这里不再对编码器执行中位校准。
    """
    scs_comm_result, scs_error = packetHandler.reOfsCal(device_id, position)
    if scs_comm_result != COMM_SUCCESS:
        print(packetHandler.getTxRxResult(scs_comm_result))
    else:
        print("[ID:%03d] offset calibration succeeded." % device_id)
    if scs_error != 0:
        print(packetHandler.getRxPacketError(scs_error))


def read_position_speed(device_id):
    """读取 TTL 总线设备的当前位置和当前速度。

    在 SW69-TTL 示例中，该函数主要用于读取 TTL Encoder E02 的绝对位置。
    同一读取接口也可用于步进电机驱动器，但步进电机本体为开环控制，
    因此转向关节的可靠绝对角度应以编码器读数为准。
    """
    present_position, present_speed, scs_comm_result, scs_error = packetHandler.ReadPosSpeed(device_id)
    if scs_comm_result != COMM_SUCCESS:
        print(packetHandler.getTxRxResult(scs_comm_result))
        return None
    if scs_error != 0:
        print(packetHandler.getRxPacketError(scs_error))
        return None
    return [present_position, present_speed]


def servo_simple_ctrl(device_id, position, speed, acc, current):
    """使用位置模式控制步进电机驱动器。

    Args:
        device_id: TTL Stepper Driver (A) 设备 ID。
        position: 目标位置，单位为驱动器位置计数，范围为 0 到 65534。
        speed: 目标速度，单位为 50 微步/秒。SW69-TTL 转向调试建议不超过 400。
        acc: 加速度，单位为 100 微步/秒^2。0 表示最高加速度，调试时建议使用 15。
        current: 相电流参数。相电流约为 3.3 * 2 * (current / 1000) A；
            current = 200 时，相电流约为 1.32 A。
    """
    scs_comm_result, scs_error = packetHandler.WritePosEx(device_id, position, speed, acc, current)
    if scs_comm_result != COMM_SUCCESS:
        print(packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print(packetHandler.getRxPacketError(scs_error))


def joint_init(encoder_id, turning_id):
    """根据编码器绝对位置同步转向电机驱动器当前位置。

    程序上电后应先调用本函数，再发送转向角度控制指令。
    """
    encoder_state = read_position_speed(encoder_id)
    if encoder_state is None:
        raise RuntimeError("Failed to read steering encoder position")

    encoder_position = encoder_state[0]
    # 编码器已经用 FD 做过中位校准，所以这里只需要计算当前读数相对中位的偏移。
    encoder_delta = encoder_position - ENCODER_CENTER
    motor_position = round(JOINT_MID + encoder_delta * ENCODER2STEPS)
    motor_position = max(0, min(65534, motor_position))
    set_position(turning_id, int(motor_position))


def joint_rad_ctrl(device_id, rad, speed, acc, current):
    """使用弧度值控制转向关节。"""
    position = int(rad * RAD2STEPS + STEERING_ZERO)
    servo_simple_ctrl(device_id, position, speed, acc, current)


def joint_deg_ctrl(device_id, deg, speed, acc, current):
    """使用角度值控制转向关节。"""
    rad = deg * 3.1415926 / 180
    joint_rad_ctrl(device_id, rad, speed, acc, current)


def walking_motor_ctrl(device_id, speed, acc, current):
    """使用速度模式控制行走电机。

    行走电机驱动器需要先在 FD 软件中设置为运行模式 1。
    如果启用了心跳保护，控制程序应周期性发送速度指令。
    """
    scs_comm_result, scs_error = packetHandler.WriteSpec(device_id, speed, acc, current)
    if scs_comm_result != COMM_SUCCESS:
        print(packetHandler.getTxRxResult(scs_comm_result))
    elif scs_error != 0:
        print(packetHandler.getRxPacketError(scs_error))


if __name__ == "__main__":
    # 上电后先同步转向电机驱动器位置，保证后续角度控制基准正确。
    joint_init(ENCODER_ID, TURNING_ID)

    # 转到中位，再分别转到 +45° 和 -45°，最后回到中位。
    joint_deg_ctrl(TURNING_ID, 0, 400, 15, 200)
    time.sleep(1.5)

    joint_deg_ctrl(TURNING_ID, 45, 400, 15, 200)
    time.sleep(1.5)

    joint_deg_ctrl(TURNING_ID, -45, 400, 15, 200)
    time.sleep(1.5)

    joint_deg_ctrl(TURNING_ID, 0, 400, 15, 200)

    # 第一次测试行走轮时，请将轮体抬离桌面或地面。
    # 以下流程依次执行：正转、停止、反转、停止。
    walking_motor_ctrl(WALKING_ID, 50, 15, 200)
    time.sleep(1.5)

    walking_motor_ctrl(WALKING_ID, 0, 15, 200)
    time.sleep(0.5)

    walking_motor_ctrl(WALKING_ID, -50, 15, 200)
    time.sleep(1.5)

    walking_motor_ctrl(WALKING_ID, 0, 15, 200)
