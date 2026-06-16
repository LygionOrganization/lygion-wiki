# TTL Node (A) 驱动与串口

TTL Node (A) 可通过 USB Type-C 直接连接电脑或单板电脑，也可以作为设备接入单线 TTL 总线。

## USB 使用方式

通过 USB 连接主机后，可在程序中实现：

- 读取 S.BUS 遥控通道数据
- 控制两组 RGB 状态灯
- 控制两路 PWM 电源输出
- 调节和控制总线舵机
- 读取兼容总线设备的反馈信息

适用主机包括：

- Windows、Linux 或 macOS 电脑
- Raspberry Pi
- NVIDIA Jetson
- RK3566 等 Linux 单板电脑

### 使用 FD 实现基础调参

!!! note "适用人群"
    新手友好，无需环境配置，图形化界面操作直观简单，但仅限于简单的测试、调参、固件升级。

    如果你使用的是非 Windows 系统，也可以参考后续的 Python / C++ 教程和对应产品的内存表，通过程序进行调参或调试工作。

![FT SCServo Debug](../../../assets/images/fd-01-cn.png){ .img-rounded width="450" }

FD 软件是运行在 Windows 平台上的总线设备调试 / 测试工具，用户可以使用它的图形化界面对总线产品进行简单测试和调参，例如为新产品更改 ID。

[FD 调试软件使用教程](../../../tutorials/fd-tool.md){ .md-button }

[TTL Node (A) 的 FD 配置步骤](fd-configuration.md){ .md-button }

## 查找串口

连接 USB 后，请根据操作系统查找新增的串口设备。

| 系统 | 常见形式 |
| --- | --- |
| Windows | `COM3`、`COM4`、`COM12` |
| Linux | `/dev/ttyUSB0`、`/dev/ttyACM0` |
| macOS | `/dev/tty.usbserial-*`、`/dev/cu.usbserial-*` |

详细操作请参考：

- [安装 USB 串口驱动](../../../tutorials/install-usb-serial-driver.md)
- [查找串口设备](../../../tutorials/find-serial-port.md)

!!! note "串口名称以系统实际识别结果为准"
    不同固件版本、操作系统和 USB 驱动可能显示不同的设备名称。连接前后对比系统新增的串口最可靠。

## TTL 总线并联

TTL Node (A) 可以与兼容的总线舵机和其他 Lygion TTL 设备共用总线：

```text
Host / Bus Controller
          │
          ├── TTL Node (A), ID 1
          ├── TTL Node (A), ID 2
          ├── Bus Servo, ID 3
          └── Other TTL Device, ID 4
```

并联使用时请确保：

1. 每个设备使用不同的 ID。
2. 所有设备使用一致的通信波特率。
3. 总线供电满足所有设备的电压和电流要求。
4. GH1.25-3P 接口只连接信号与 GND，不承担设备供电。

TTL Node (A) 的出厂设备 ID 为 `0`，默认波特率为 `1,000,000 bps`。如果总线舵机使用其他波特率，需要先将 TTL Node (A) 设置为相同值。

## 通信排查

如果软件无法访问设备，请依次检查：

1. USB 线是否支持数据传输。
2. 系统是否识别出串口。
3. 串口是否被其他软件占用。
4. 程序选择的端口名称是否正确。
5. 总线设备 ID 是否冲突。
6. 所有设备波特率是否一致。
7. 电源电压、电流和共地是否正确。

更多说明见：[常见通信问题排查](../../../tutorials/communication-troubleshooting.md)。
