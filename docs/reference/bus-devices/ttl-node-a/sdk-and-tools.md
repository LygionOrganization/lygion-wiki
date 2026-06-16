# TTL Node (A) SDK 与工具

TTL Node (A) 提供 Python 和 C++ 开发示例，可用于读取 S.BUS 信号、控制 RGB 状态灯、控制 PWM 输出，以及访问同一总线中的兼容设备。

## Python SDK

Python SDK 适合 Windows、Linux、macOS、Raspberry Pi 和 Jetson 等平台。

- [TTL Node (A) Python SDK 与示例](https://github.com/LygionOrganization/lygion_devs_py/tree/main/lynode)
- [Lygion Python SDK 仓库](https://github.com/LygionOrganization/lygion_devs_py)
- [本站下载 Python SDK](../../../assets/files/lygion_devs_py.zip)

建议先完成以下基础步骤：

1. 使用 USB 数据线连接 TTL Node (A)。
2. 确认系统识别出的串口名称。
3. 安装 SDK 所需依赖。
4. 打开 `lynode` 目录中的示例，根据实际串口和设备配置运行。

相关教程：

- [安装 Python](../../../tutorials/install-python.md)
- [查找串口设备](../../../tutorials/find-serial-port.md)
- [运行 Python 脚本](../../../tutorials/run-python-scripts.md)

## C++ / Arduino SDK

C++ 示例适合在嵌入式控制器或原生 C++ 项目中使用。

- [TTL Node (A) C++ 示例](https://github.com/LygionOrganization/lygion_devs_cpp/tree/main/example/lyttln)
- [Lygion C++ SDK 仓库](https://github.com/LygionOrganization/lygion_devs_cpp)
- [本站下载 C++ / Arduino SDK](../../../assets/files/lygion_devs_cpp.zip)

[TTL Node (A) Arduino 开发教程](arduino-development.md){ .md-button }

使用 Arduino IDE 或 PlatformIO 时，可参考：

- [安装 Arduino IDE](../../../tutorials/install-arduino-ide.md)
- [安装 PlatformIO](../../../tutorials/install-platformio.md)
- [上传 Arduino 示例程序](../../../tutorials/upload-arduino-sketch.md)
- [打开串口监视器](../../../tutorials/serial-monitor.md)

## FD 调试软件

TTL Node (A) 作为可寻址的总线设备，可配合上位机工具进行设备连接和参数配置。使用前请确认软件版本支持 TTL Node (A)。

- [FD 调试软件教程](../../../tutorials/fd-tool.md)
- [TTL Node (A) 的 FD 参数配置](fd-configuration.md)

## 示例索引

| 功能 | C++ / Arduino | Python |
| --- | --- | --- |
| 修改设备参数 | `lyttln/ttln_eprom` | `lynode/ttln_eprom.py` |
| 读取总线电压 | `lyttln/ttln_adc` | `lynode/ttln_adc.py` |
| 控制 PWM 输出 | `lyttln/ttln_pwm` | `lynode/ttln_pwm.py` |
| 控制 RGB 灯 | `lyttln/ttln_rgb` | `lynode/ttln_rgb.py` |
| 读取 S.BUS | `lyttln/ttln_sbus` | `lynode/ttln_subs.py` |

## 开发建议

- 首次调试时只连接一块 TTL Node (A)，确认通信后再加入其他设备。
- 多设备并联前先分别设置不重复的设备 ID。
- 读取 S.BUS 数据前，确认遥控器与接收机已完成配对。
- 测试 PWM 输出时先使用低功率负载，并逐步增加占空比。
- 控制感性负载时，注意启动电流、反向电动势和电源波动。

!!! tip "同一条总线可以混合设备"
    TTL Node (A)、其他 Lygion TTL 设备和兼容的飞特 STS、SCS、HLS 系列舵机可以接入同一条总线。所有设备的 ID 必须不同，通信波特率需要一致，供电电压也必须兼容。
