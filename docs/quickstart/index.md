# 快速开始

快速开始的目标是让用户尽快完成第一次通信，而不是一次性学习所有产品原理。

请先选择你的开发方式：

<div class="grid cards" markdown>

-   **Python 路线**

    适合使用 PC、Linux、macOS、Windows、Raspberry Pi、Jetson、RK 等设备的用户。

    你会通过 USB 连接 TTL Adapter (A)，然后运行 Python 示例脚本读取或控制总线设备。

    [开始 Python 路线](python-first-demo.md)

-   **C++ 路线**

    适合使用 ESP32S3、ESP32、STM32、Arduino Mega2560 等嵌入式控制器的用户。

    你会通过 MCU 的硬件串口连接 TTL 总线设备，然后使用 Arduino IDE 或 PlatformIO 运行 C++ 示例程序。

    [开始 MCU C++ 路线](cpp-first-demo.md)

</div>

!!! tip "如何选择"
    如果你的控制器是电脑、树莓派、Jetson 或其它运行 Linux / macOS / Windows 的设备，选择 **Python 路线**。

    如果你的控制器是 ESP32、STM32、Arduino 等单片机开发板，选择 **MCU C++ 路线**。

## 两条路线的区别

| 路线 | 常见硬件 | 连接方式 | 使用语言 | 适合场景 |
| --- | --- | --- | --- | --- |
| Python 路线 | PC、Mac、Raspberry Pi、Jetson、RK、N100 小主机 | USB → TTL Adapter (A) → TTL 总线 | Python | 快速测试、上位机控制、机器人主控、调参脚本 |
| MCU C++ 路线 | ESP32S3、ESP32、STM32、Arduino | MCU UART → TTL Adapter (A) 或 UART 转单线 TTL 电路 | C++ / Arduino | 嵌入式控制、底盘控制器、关节控制器、产品集成 |

## 第一次使用建议

- 第一次只连接 **一个** TTL 总线设备，避免默认 ID 冲突。
- 优先运行 `ping` 或读取类示例，不要一开始就运行高速运动程序。
- 执行器类设备必须接入合适的外部电源，不能只依赖 USB 供电。
- 如果遇到问题，先检查串口、波特率、设备 ID、供电和接线。

## 常用基础教程

- [如何打开终端 / CMD / PowerShell](../tutorials/open-terminal.md)
- [安装 Python](../tutorials/install-python.md)
- [查找串口设备](../tutorials/find-serial-port.md)
- [运行 Python 脚本](../tutorials/run-python-scripts.md)
- [安装 Arduino IDE](../tutorials/install-arduino-ide.md)
- [安装 PlatformIO](../tutorials/install-platformio.md)
- [MCU UART 接线基础](../tutorials/mcu-uart-wiring.md)
- [设备 ID 与波特率](../tutorials/device-id-and-baudrate.md)
- [常见通信问题排查](../tutorials/communication-troubleshooting.md)
