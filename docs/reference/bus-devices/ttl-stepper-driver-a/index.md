# TTL Stepper Driver (A)

<a href="https://item.taobao.com/item.htm?id=1048288207796&mi_id=0000PBGMdvfnvMc72n4rxwwUZAGE0n6lUbaEop4yui_kyz8&spm=a21xtw.29178619.0.0&xxc=shop&skuId=6079071304518" target="_blank">淘宝购买链接</a>

TTL Stepper Driver (A) 是一款基于单线 TTL 总线通信的双极步进电机驱动板。它可以让普通两相步进电机像总线舵机一样被控制：上位机或 MCU 只需要发送位置、速度、电流等指令，驱动板完成底层步进驱动、加减速、反馈和保护逻辑。

![TTL Stepper Driver (A)](assets/ttlsd-01.png){ .img-rounded width="360" }

## 主要功能

- 位置模式控制
- 速度模式控制
- 从动同步模式
- 多设备同步读写
- 当前位置与速度反馈
- 电压、温度、移动状态反馈
- 限位开关输入
- 心跳保护
- 自动限流、过流、过热保护

## 主要参数

| 项目 | 参数 |
| --- | --- |
| 通信方式 | 单线 TTL 总线 |
| 默认波特率 | 1 Mbps |
| 输入电压 | DC 9~26V |
| 最大电流 | 1.5A |
| 适用电机 | 双极步进电机 |
| 微步设置 | 1、1/2、1/4、1/8、1/16、1/32（默认） |
| 控制模式 | 位置模式 / 速度模式 / 从动同步模式 |

## 文档导航

- [硬件接线](hardware-wiring.md)
- [运行模式](operating-modes.md)
- [参数说明](parameters.md)
- [内存表与相位计算](memory-map.md)
- [Python 控制](python-quickstart.md)
- [C++ / Arduino](cpp-arduino.md)
- [限位、回零与心跳保护](limits-homing-heartbeat.md)
- [FAQ](faq.md)

## 第一次使用

建议先完成：

- [快速上手](../../../quickstart/index.md)
- [查找串口设备](../../../tutorials/find-serial-port.md)

!!! warning "第一次测试请使用保守参数"
    示例中的速度和加速度可能只是演示值。实际项目中建议从较低速度、非 0 加速度和合适电流开始测试。
