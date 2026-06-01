# TTL Encoder E02 硬件安装

TTL Encoder E02 通过检测径向磁铁的旋转角度输出位置和速度。

## 工作原理

```text
旋转轴 / 齿轮 / 同步轮
        │
        │ 安装径向磁铁
        ▼
磁铁随轴旋转
        │
        ▼
TTL Encoder E02 检测磁场角度
        │
        ▼
通过 TTL 总线输出位置和速度
```

12bit 精度下：

```text
0~4095 = 0°~360°
```

角度换算：

```python
angle_deg = position / 4096.0 * 360.0
```

## 安装要求

- 使用径向磁铁，不要使用普通轴向磁铁替代。
- 磁铁中心尽量对准编码器 IC 中心。
- 磁铁与编码器 IC 上表面间距建议约 1mm。
- 间距最大不建议超过 1.5mm。
- 磁铁旋转时应尽量减少偏心和晃动。
- 编码器 PCB 应固定可靠。

![TTL Encoder E02 assembly](../../../assets/images/ttle02-02-cn.png){ .img-rounded }

## 典型连接

```text
PC / Raspberry Pi / Jetson / Mac
        │ USB
        ▼
TTL Adapter (A)
        │ 5264-3P
        ▼
HC-1.25 8P Hub (A)
        │ HC-1.25-3P
        ▼
TTL Encoder E02
```

## 引脚说明

TTL Encoder E02 使用 HC-1.25-3P 接口：

```text
- / + / S
```

接线前请确认接口方向。

## 常见安装问题

| 现象 | 可能原因 |
| --- | --- |
| 角度跳动明显 | 磁铁偏心、距离过大、磁铁固定不牢 |
| 转动方向与预期相反 | 安装方向或应用层定义不同 |
| 读数不稳定 | 供电不稳、总线连接松动、磁铁间距不合适 |
