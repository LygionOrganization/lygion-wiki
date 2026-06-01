# TTL Stepper Driver (A) 硬件接线

TTL Stepper Driver (A) 需要同时连接 TTL 总线、电源和步进电机。正式上电前应仔细检查接线。

## 典型连接

```text
PC / Raspberry Pi / Jetson / Mac
        │ USB
        ▼
TTL Adapter (A)
        │ 5264-3P TTL Bus
        ▼
TTL Stepper Driver (A)
        │
        ▼
Stepper Motor
```

## 上电前检查

- 电源电压是否在 DC 9~26V 范围内。
- 步进电机线序是否正确。
- TTL 总线的 `+ / - / S` 是否接线正确。
- 总线上是否存在重复 ID。
- 限位开关是否接到正确接口。
- EDS 同步接口是否方向正确。

![TTL Stepper Driver (A) Basic Parameters](../../../assets/images/ttlsd-02-cn.png){ .img-rounded }

## 电源

TTL Stepper Driver (A) 驱动电机时必须接入外部电源。不要只依赖 USB 供电。

| 项目 | 参数 |
| --- | --- |
| 输入电压 | DC 9~26V |
| 电流设置 | 设置的是电机相电流，不是电源输入电流 |

## 步进电机接口

请确认步进电机为双极步进电机，并确认 A/B 相线序。线序错误可能导致电机只响不转、抖动或无法正常输出扭矩。

## TTL 总线接口

TTL 总线可连接：

- TTL Adapter (A)
- TTL Encoder E02
- Feetech TTL 总线舵机
- 其它 Lygion TTL 总线设备

同一总线所有设备 ID 必须不同。

## 限位接口

TTL Stepper Driver (A) 提供 MIN 和 LIMIT 两个限位接口。详细逻辑见：[限位、回零与心跳保护](limits-homing-heartbeat.md)。

## EDS 同步接口

EDS 同步接口用于从动同步模式，连接方向为：

```text
主设备 EDS OUT → 从设备 EDS IN
从设备 EDS OUT → 下一个从设备 EDS IN
```

!!! warning "EDS 方向不能接反"
    从动同步模式依赖接口方向，接反后从设备无法正确跟随主设备。
