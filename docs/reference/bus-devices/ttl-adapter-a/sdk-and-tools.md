# TTL Adapter (A) SDK 与工具

TTL Adapter (A) 本身是通信适配器。具体使用哪个 SDK，取决于你要控制的总线设备。

## FD 调试软件

FD 软件适合用于：

- 扫描设备 ID
- 修改 ID
- 修改波特率
- 读取反馈
- 设置部分参数

[FD 调试软件教程](../../../tutorials/fd-tool.md)

## Lygion Python SDK

用于控制或读取 Lygion TTL 总线设备，例如：

- TTL Encoder E02
- TTL Stepper Driver (A)
- 后续 Lygion TTL 总线设备

下载入口：

- [Python SDK](../../../downloads/index.md#python-sdk)

## Lygion C++ / Arduino SDK

适合 ESP32S3、ESP32、Arduino Mega2560、STM32 Arduino Core 等 MCU。

下载入口：

- [C++ / Arduino SDK](../../../downloads/index.md#c--arduino-sdk)

## Feetech SDK

当你控制飞特 STS / HLS / SCS 系列总线舵机时，可使用飞特官方 SDK。

!!! tip "同一根总线可以混合设备"
    Lygion TTL 总线设备可以与兼容的飞特 TTL 总线舵机接入同一根总线，但所有设备的 ID 必须不同，波特率需要一致，供电电压也必须兼容。
