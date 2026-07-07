# 步进电机 4240BY-G5.2

4240BY-G5.2 是一款带减速机构的 42 系列双极步进电机，适用于机器人底盘、关节、转台、滑台和其它需要低速大扭矩输出的机构。电机本体不包含独立控制器，通常需要配合外部步进电机驱动器使用。

![4240BY-G5.2 stepper motor](assets/hero.webp){ .img-rounded }

## 产品特点

- 42 mm 级步进电机本体，便于集成到常见机器人结构中。
- 前端集成减速机构，可提升低速输出能力。
- 双极步进电机接口，可配合 [TTL Stepper Driver (A)](../../bus-devices/ttl-stepper-driver-a/index.md) 实现总线控制。
- 输出端提供 D 形轴和前法兰安装孔，适合连接联轴器、同步轮、齿轮或自定义执行机构。
- 提供 STEP、PDF 和 DXF 资料，便于结构设计、装配检查和加工确认。

## 典型应用

- 移动机器人底盘驱动
- 小型机械臂或教学机械结构
- 低速转台、分度机构和夹具
- 同步带、齿轮或丝杆传动机构

## 配套驱动器

4240BY-G5.2 可作为普通两相双极步进电机接入步进电机驱动器。若需要通过 TTL 总线进行位置、速度、电流和参数配置，推荐配合 [TTL Stepper Driver (A)](../../bus-devices/ttl-stepper-driver-a/index.md) 使用。

```text
上位机 / MCU
    │
    ▼
TTL Adapter (A) 或 TTL 总线主控
    │
    ▼
TTL Stepper Driver (A)
    │
    ▼
4240BY-G5.2
```

![4240BY-G5.2 wiring example](assets/ttl-wiring.webp){ .img-rounded }

!!! warning "外部供电"
    步进电机工作时必须为驱动器接入符合规格的外部电源。USB 连接通常只用于通信，不应作为电机工作的主要供电来源。

## 机械尺寸

下图为 4240BY-G5.2 的主要安装尺寸。结构设计时请以页面提供的 PDF、DXF 或 STEP 文件为最终依据。

![4240BY-G5.2 dimensions](assets/dimensions.webp){ .img-rounded }

| 项目 | 参数 |
| --- | --- |
| 电机框架尺寸 | 42 mm 级 |
| 机身宽度 | 42 mm |
| 参考总长 | 67.5 mm |
| 输出轴形式 | D 形轴 |
| 输出轴参考直径 | 8 mm |
| 输出轴伸出长度 | 18 mm |
| 前端安装孔 | 4 × M3，PCD Ø28 |

!!! note "尺寸说明"
    表格中的尺寸来自当前机械图纸的主要标注，适合用于快速评估装配空间。正式开孔、加工或批量装配前，请下载图纸或 3D 模型复核。

## 使用建议

1. 根据负载、速度和散热条件设置合适的相电流。
2. 第一次上电测试时使用较低速度和较低加速度，确认电机相线、旋转方向和机构限位。
3. 若电机出现只响不转、抖动或发热异常，请优先检查 A/B 相线序和驱动器电流设置。
4. 需要长时间运行时，应确认电机温升、驱动器散热和机构负载是否处于安全范围。

## 包装内容

![4240BY-G5.2 package contents](assets/package-contents.webp){ .img-rounded }

## 资料下载

| 资料 | 文件 |
| --- | --- |
| STEP 3D 模型 | [4240BY-G5.2.step](assets/4240BY-G5.2.step) |
| 机械图纸 PDF | [4240BY-G5.2.pdf](assets/4240BY-G5.2.pdf) |
| DXF 图纸 | [4240BY-G5.2.dxf](assets/4240BY-G5.2.dxf) |

## 相关资料

- [TTL Stepper Driver (A)](../../bus-devices/ttl-stepper-driver-a/index.md)
- [TTL Stepper Driver (A)：硬件接线](../../bus-devices/ttl-stepper-driver-a/hardware-wiring.md)
- [TTL Stepper Driver (A)：运行模式](../../bus-devices/ttl-stepper-driver-a/operating-modes.md)
