# 机器人整机

本分类收录 Lygion 机器人整机产品的上手、控制、校准、集成和维护资料。

## 产品入口

| 产品 | 定位 | 推荐入口 |
| --- | --- | --- |
| LinkArm-M | 基于 Python SDK 和 CLI 控制的机械臂，适合脚本控制、教学实验和上层 AI 集成。 | [查看文档](linkarm-m/index.md) |
| LinkArm-LT | 包含 ESP32-S3 下位机，带 Web 控制台、动作脚本、JSON 指令和无线示教功能的机械臂平台。 | [查看文档](linkarm-lt/index.md) |

## 如何阅读

1. 先阅读对应产品的[快速开始](linkarm-m/quickstart.md)，完成供电、连接和基础动作测试。
2. 需要长期使用时，继续阅读配置、校准和固件恢复章节。
3. 需要集成到上位机、移动平台或 AI 应用时，再阅读 SDK、JSON 指令、动作脚本和通信接口。

## 相关基础教程

- [安装 Python](../../tutorials/install-python.md)
- [查找串口设备](../../tutorials/find-serial-port.md)
- [供电与接线基础](../../tutorials/power-and-wiring-basics.md)
- [常见通信问题排查](../../tutorials/communication-troubleshooting.md)

!!! tip "先验证单机，再接入复杂系统"
    机械臂接入移动底盘、视觉系统或 AI 工作流前，应先确认单机动作、零位、限位、急停和供电都可靠。
