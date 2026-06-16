# LinkArm-LT

<a href="https://item.taobao.com/item.htm?id=1000788647949&mi_id=0000AALo0AjaNxbfVhObzA__Lx09u33F7ftbHVAvJAWjnyw&spm=a21xtw.29178619.0.0&xxc=shop&skuId=6156172559107" target="_blank">淘宝购买链接</a>

LinkArm-LT 是一款可通过浏览器直接控制、支持动作脚本与多种上位机通信方式的轻量机械臂。控制器基于 ESP32-S3，内置 Web 应用，无需安装专用 App 即可完成基础控制、Wi-Fi 配置、动作编排和 JSON 指令调试。

![LinkArm-LT 产品主图](assets/A.png){ .img-rounded }

## 核心能力

- 浏览器 Web 控制台，支持手机、平板和电脑
- FPV 与三维直角坐标两种末端控制方式
- ESP-NOW 一对一或一对多同步示教
- 动作脚本保存、播放、循环与开机自动运行
- USB CDC、HTTP、WebSocket 三种上位机接口
- JSON 指令控制机械臂、舵机、OLED、蜂鸣器、Wi-Fi 和文件系统
- 支持固件恢复、中位校准与移动底盘集成

## 基本参数

| 项目 | 参数 |
| --- | --- |
| 工作电压 | DC 9~12.6V |
| 推荐电源 | 12V 3A，DC5521 |
| 移动供电 | 满足功率要求的 3S 锂电池 |
| 总线波特率 | 500,000 bps |
| 默认 Wi-Fi 热点 | `Robot` |
| 默认热点密码 | `12345678` |
| AP 模式地址 | `http://192.168.4.1` |
| HTTP 服务 | 端口 `80`，接口 `/api/cmd` |
| WebSocket 服务 | `ws://<设备IP>:80/ws` |
| 机械臂总线设备 | 4 个舵机 + 1 个 TTL Node (A) |

!!! danger "使用前必须固定机械臂"
    机械臂动作时重心变化明显。请用两只 G 字夹牢固固定在桌面，或使用安装孔固定到可靠底盘。不要在工作范围内放置易碎物品，设备应远离眼睛和儿童。

## 从哪里开始

=== "第一次使用"

    依次完成固定、线缆检查、外部供电和 Web 控制台连接。

    [开始使用](quickstart.md){ .md-button .md-button--primary }

=== "浏览器控制"

    了解热点、局域网接入、FPV 控制和直角坐标控制。

    [Web 控制台](web-control.md){ .md-button }

=== "动作编排"

    将多条 JSON 指令保存为任务文件，支持循环和开机运行。

    [动作脚本](action-scripting.md){ .md-button }

=== "程序开发"

    通过 USB CDC、HTTP 或 WebSocket 从 Python 等上位机程序控制机械臂。

    [上位机通信](host-communication.md){ .md-button }

## 文档导航

- [快速开始](quickstart.md)
- [Web 控制台](web-control.md)
- [ESP-NOW 同步示教](sync-teaching.md)
- [动作脚本](action-scripting.md)
- [JSON 指令参考](json-commands.md)
- [上位机通信](host-communication.md)
- [固件恢复与中位校准](firmware-and-calibration.md)
- [项目集成与尺寸](integration.md)
- [故障排查](faq.md)

## 开源资源

- [Robot Driver with ESP32S3 Lite 源码与上位机示例](https://github.com/EffectsMachine/robot_driver_with_esp32s3_lite)
- [Robot Driver with ESP32S3 Lite 产品 Wiki](../../bus-devices/robot-driver-with-esp32s3-lite/index.md)
- [TTL Node (A) 产品 Wiki](../../bus-devices/ttl-node-a/index.md)
