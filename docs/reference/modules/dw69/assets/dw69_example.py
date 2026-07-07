from lygion_devs_py.lydevs_sdk import *
import time


# DW69 对应的 TTL Stepper Driver (A) 设备 ID。
# 如果总线上只有一个驱动器，可保持默认 ID 1；如果有多个设备，请改成 FD 中配置的实际 ID。
WHEEL_DRIVER_ID = 1

# 请根据 TTL Adapter (A) 在当前系统中的实际串口名称修改。
# 示例：Windows 为 "COM3"，Linux 为 "/dev/ttyUSB0"，macOS 为 "/dev/cu.usbserial-xxxx"。
PORT_NAME = "COM18"

# TTL Stepper Driver (A) 默认波特率。
BAUDRATE = 1000000

# 第一次测试建议使用较低速度。
# 速度为正数时电机向一个方向旋转，速度为负数时反向旋转，速度为 0 时停止。
TEST_SPEED = 50

# 加速度参数不建议在调试时设置为 0。
# 0 表示接近最高加速度，可能造成启动冲击、抖动或失步。
WHEEL_ACC = 15

# 相电流参数。
# 相电流(A) 约等于 3.3 * 2 * (current / 1000)。
# current = 200 时，相电流约为 1.32 A。
MOTOR_CURRENT = 200

# 如果在 FD 中开启了心跳保护，程序需要周期性发送速度指令。
# 这里使用 0.1 s 周期，远小于 2 s 心跳保护时间。
COMMAND_PERIOD_S = 0.1


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


def wheel_speed_ctrl(device_id, speed, acc, current):
    """使用速度模式控制 DW69 驱动轮。

    使用前需要先在 FD 中将 TTL Stepper Driver (A) 设置为速度模式。

    Args:
        device_id: TTL Stepper Driver (A) 设备 ID。
        speed: 速度参数。正数和负数表示两个旋转方向，0 表示停止。
        acc: 加速度参数。调试时建议使用较小但非 0 的值，例如 15。
        current: 相电流参数。current = 200 时，相电流约为 1.32 A。
    """
    scs_comm_result, scs_error = packetHandler.WriteSpec(device_id, speed, acc, current)
    if scs_comm_result != COMM_SUCCESS:
        print(packetHandler.getTxRxResult(scs_comm_result))
        return False
    if scs_error != 0:
        print(packetHandler.getRxPacketError(scs_error))
        return False
    return True


def drive_wheel_for(speed, duration_s):
    """让车轮按指定速度运行一段时间。

    如果驱动器开启了心跳保护，循环中的周期性发送可以避免电机因超时自动停止。
    函数结束时会主动发送 0 速度，让车轮停止。
    """
    print(f"Wheel speed={speed}, duration={duration_s}s")
    start_time = time.time()
    while time.time() - start_time < duration_s:
        if not wheel_speed_ctrl(WHEEL_DRIVER_ID, speed, WHEEL_ACC, MOTOR_CURRENT):
            break
        time.sleep(COMMAND_PERIOD_S)

    wheel_speed_ctrl(WHEEL_DRIVER_ID, 0, WHEEL_ACC, MOTOR_CURRENT)


if __name__ == "__main__":
    # 第一次运行前，请将车轮抬离桌面或地面，避免车轮转动带动设备移动。

    # 低速正转 1.5 s。
    drive_wheel_for(TEST_SPEED, 1.5)
    time.sleep(0.5)

    # 低速反转 1.5 s。
    drive_wheel_for(-TEST_SPEED, 1.5)
    time.sleep(0.5)

    # 明确发送停止指令。
    wheel_speed_ctrl(WHEEL_DRIVER_ID, 0, WHEEL_ACC, MOTOR_CURRENT)
    print("DW69 wheel test finished")
