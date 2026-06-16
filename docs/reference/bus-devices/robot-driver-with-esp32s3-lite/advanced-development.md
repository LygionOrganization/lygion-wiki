# PlatformIO 二次开发

Robot Driver with ESP32S3 Lite 的完整固件使用 Arduino 框架，推荐通过 VS Code + PlatformIO 修改和构建。

[学习 VS Code + PlatformIO 复杂项目开发](../../../tutorials/platformio-development/index.md){ .md-button .md-button--primary }

通用教程涵盖环境安装、工程结构、`platformio.ini`、依赖管理、编译上传、串口调试和 Git 工作流。本页只补充本产品特有的信息。

## 获取项目

- [robot_driver_with_esp32s3_lite 开源项目](https://github.com/EffectsMachine/robot_driver_with_esp32s3_lite)

下载或克隆后，应打开包含 `platformio.ini` 的项目根目录，不要只打开 `src`。

## 硬件配置

| 项目 | 配置 |
| --- | --- |
| 主控 | ESP32-S3-WROOM-1 R8N8 |
| Flash | 8 MB |
| PSRAM | 8 MB |
| 框架 | Arduino |
| 日志串口 | 原生 USB CDC |
| 固件上传 | 以仓库内 `platformio.ini` 为准 |

!!! warning "不要新建空工程后手动猜配置"
    优先使用仓库自带的 `platformio.ini`。开发板名称相似并不代表 Flash、PSRAM、USB 模式和分区表相同。

## 两个 Type-C 接口

| 接口 | 用途 |
| --- | --- |
| `USB` | ESP32-S3 原生 USB CDC、程序日志和上位机通信 |
| `UART` | UART0 转 USB、串口透传和固件恢复 |

上传前根据项目配置确认实际上传接口。接错接口通常表现为找不到端口或一直等待连接。

## 安全开发流程

1. 断开舵机、电机和外部动力电源。
2. 只连接 USB，先编译并上传。
3. 观察 OLED、蜂鸣器和日志，确认主程序正常启动。
4. 检查 Wi-Fi、文件系统和 JSON 接口。
5. 最后接回执行器，并从低速度、低负载开始测试。

!!! danger "固件启动可能立即驱动执行器"
    开机任务、保存的动作文件或自定义初始化代码都可能让机器人自动动作。上传和首次运行时应断开动力设备。

## 常用功能开关

项目功能通常通过配置头文件中的宏控制。例如将 UART0 用于 S.BUS：

```cpp
#define UART0_AS_SBUS
```

启用后：

- UART0 不再同时用于默认串口透传。
- S.BUS 信号连接 ESP32-RX。
- 接收机与驱动板共地。
- 应用层需要处理失联和 failsafe。

详细说明见[UART 透传与 S.BUS](uart-sbus.md)。

## 修改建议

- 保留底层总线、网络和文件系统封装，优先修改应用层。
- 新功能拆分为独立 `.h/.cpp`，不要持续堆入入口文件。
- 自定义默认值集中放入配置文件。
- 修改 JSON 协议时尽量保持旧字段兼容。
- 先用 OLED、蜂鸣器或日志验证逻辑，再连接执行器。
- 文件系统布局或分区变化前，先保存任务和 Wi-Fi 配置。

## 相关页面

- [硬件资源与接线](board-resources.md)
- [UART 透传与 S.BUS](uart-sbus.md)
- [固件恢复](firmware-flash-and-reset.md)
- [故障排查](faq.md)
