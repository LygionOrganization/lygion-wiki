# 总线设备

本分类收录 Lygion Robotics 的总线适配器、传感器、驱动器、舵机、集线板和控制板。它们共享单线 TTL 半双工总线，多个设备可以并联使用，但每个设备必须拥有唯一 ID，并且波特率、供电电压和接口线序需要匹配。

## 选型入口

| 分类 | 产品 | 适合场景 | 推荐入口 |
| --- | --- | --- | --- |
| 通信适配 | TTL Adapter (A) | 电脑、树莓派、Jetson 或 MCU 接入单线 TTL 总线 | [查看文档](ttl-adapter-a/index.md) |
| 角度反馈 | TTL Encoder E02 | 读取关节、转轴或机构的 12bit 绝对角度 | [查看文档](ttl-encoder-e02/index.md) |
| 电机驱动 | TTL Stepper Driver (A) | 通过 TTL 总线控制步进电机的位置、速度和参数 | [查看文档](ttl-stepper-driver-a/index.md) |
| 多功能节点 | TTL Node (A) | S.BUS、RGB、PWM、ADC、USB 和 TTL 总线桥接 | [查看文档](ttl-node-a/index.md) |
| 执行器 | 总线舵机 | 飞特 TTL 串行总线舵机，适合关节、夹爪和云台机构 | [查看文档](bus-servos/index.md) |
| 控制板 | Robot Driver with ESP32S3 Lite | 可用做机器人下位机，机器人动作脚本、Web 控制台、舵机和外设控制 | [查看文档](robot-driver-with-esp32s3-lite/index.md) |
| 接线扩展 | 总线集线板 | 扩展多路 TTL 总线设备接入和供电分配 | [TTL-5264](hub-boards/ttl-5264-8p-hub-a.md) · [HC-1.25](hub-boards/hc-1.25-8p-hub-a.md) |

## 推荐学习路径

第一次使用总线设备时，建议按下面顺序准备：

1. [快速开始](../../quickstart/index.md)：完成一次基础通信测试。
2. [供电与接线基础](../../tutorials/power-and-wiring-basics.md)：确认外部电源、共地和电流余量。
3. [设备 ID 与波特率](../../tutorials/device-id-and-baudrate.md)：理解总线设备并联时的 ID 管理。
4. [FD 调试软件](../../tutorials/fd-tool.md)：搜索设备、读取反馈、修改 ID 和波特率。
5. [常见通信问题排查](../../tutorials/communication-troubleshooting.md)：处理扫描不到设备、反馈异常或动作无响应。

[快速开始](../../quickstart/index.md){ .md-button }
[下载中心](../../downloads/index.md){ .md-button }

## 使用原则

!!! warning "先单设备配置，再并联使用"
    多个新设备可能使用相同默认 ID。第一次修改 ID 或调试新设备时，建议总线上只保留一个待配置设备。

!!! danger "总线供电会影响所有并联设备"
    同一条总线上的 Vcc 会进入所有并联设备。接入电池或高电压电源前，请确认每个设备都支持该电压范围。

!!! tip "先读反馈，再写控制指令"
    新项目调试时优先运行读取反馈或扫描类示例。确认通信、ID、方向、限位和供电都正常后，再运行运动控制或参数写入示例。
