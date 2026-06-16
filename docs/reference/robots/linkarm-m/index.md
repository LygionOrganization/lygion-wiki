# LinkArm-M

<a href="https://item.taobao.com/item.htm?id=1044538492624&mi_id=0000ZVmzMPRoJcPzxCJy8lUHlAOsRlC-rTjLSGUnqUzB4y0&spm=a21xtw.29178619.0.0&xxc=shop&skuId=6230288603405" target="_blank">淘宝购买链接</a>

![LinkArm](assets/A.png){ .img-rounded }

LinkArm-M 是一款可通过 Python SDK 直接控制的机器人机械臂，适合模块调试、教学演示、自动化脚本、移动机器人和 AI Agent 集成。

主机通过 USB 连接机械臂上的 [TTL Node (A)](../../bus-devices/ttl-node-a/index.md)，SDK 再通过串口控制四个总线舵机、夹爪以及节点板上的 LED 和 PWM 输出。

## 主要能力

- 关节空间单关节与多关节控制
- 笛卡尔空间逆运动学（IK）
- 当前姿态正运动学读取（FK）
- 夹爪、舵机扭矩和扭矩限制
- TTL Node (A) RGB LED 与 PWM 输出
- CLI 一次性命令和交互式 Shell
- Python `RobotController` API
- JSON 输出和批量命令，便于自动化及 AI 调用
- 多台机械臂独立配置和同时控制

!!! info "坐标单位"
    LinkArm-M 的笛卡尔坐标、连杆尺寸和距离控制接口全部使用毫米（mm）。关节角度使用弧度。

## 系统结构

```text
PC / Raspberry Pi / Jetson / AI Agent
                  │
          CLI 或 Python SDK
                  │ USB 串口
                  ▼
             TTL Node (A)
                  │ TTL Bus
                  ▼
       四个 SCS 总线舵机与夹爪
```

## 基本参数

| 项目 | 参数 |
| --- | --- |
| 推荐电源 | 12V DC，供电能力不低于 3A |
| 电池供电 | 3S 锂电池，约 9~12.6V |
| 主机通信接口 | TTL Node (A) 的 USB Type-C |
| 串口波特率 | `500000` |
| 舵机类型 | 飞特 SCS 系列总线舵机 |
| 默认关节 ID | `31`、`32`、`33`、`34` |
| TTL Node (A) 默认 ID | `40` |
| SDK | Python 3.8 及以上 |

## 机械图纸下载

LinkArm-LT 与 LinkArm-M 的主体机械结构和安装尺寸基本一致，可使用以下 LinkArm-LT 图纸进行结构设计与安装评估：

- [展开姿态尺寸图（PDF）](assets/LinkArm_LT.pdf)
- [折叠姿态尺寸图（PDF）](assets/LinkArm_LT_folded.pdf)
- [二维 CAD 图纸（DXF）](assets/LinkArm_LT_dxf.dxf)

!!! warning "加工前请复核版本"
    以上文件原始名称和图纸内容均为 LinkArm-LT。LinkArm-M 与其结构几乎相同，但不同生产版本仍可能存在局部差异。用于开孔、加工或批量生产前，请核对实际 LinkArm-M 的安装孔位、外形尺寸和图纸版本。

!!! danger "USB 不能作为机械臂动力电源"
    USB 主要用于通信。控制机械臂动作前，必须正确连接 12V 电源或满足能力要求的 3S 锂电池。

!!! danger "首次动作前必须填写专属中位值"
    每台 LinkArm-M 的四个舵机中位不同。请把机身贴纸上的 `servo_middle` 数组准确写入 `arm_config.json`，否则可能出现姿态偏移、运动幅度异常、IK/FK 错误或碰撞。

## 从哪里开始

=== "第一次使用"

    完成供电、USB 连接、Python 安装、串口配置和安全测试。

    [开始使用](quickstart.md){ .md-button .md-button--primary }

=== "终端控制"

    使用 CLI 读取状态、控制夹爪、关节和笛卡尔坐标。

    [CLI 命令控制](cli-control.md){ .md-button }

=== "编写程序"

    在自己的 Python 项目中导入 `RobotController`。

    [Python SDK 开发](python-sdk.md){ .md-button }

=== "AI 或多机械臂"

    使用 JSON 输出、批量命令或多个配置文件搭建上层应用。

    [多机械臂与 AI 集成](multi-arm-and-ai.md){ .md-button }

## 文档导航

- [快速开始](quickstart.md)
- [配置与中位校准](configuration-and-calibration.md)
- [CLI 命令控制](cli-control.md)
- [Python SDK 开发](python-sdk.md)
- [外设与维护](peripherals-and-maintenance.md)
- [多机械臂与 AI 集成](multi-arm-and-ai.md)
- [故障排查](faq.md)

## 开源项目

- [LygionOrganization/linkarm_python_sdk](https://github.com/LygionOrganization/linkarm_python_sdk)
- [TTL Node (A) 产品 Wiki](../../bus-devices/ttl-node-a/index.md)
