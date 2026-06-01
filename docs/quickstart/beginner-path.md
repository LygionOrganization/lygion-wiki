# 新手路径

本页适合第一次使用 TTL 总线设备的用户。你不需要先理解所有寄存器和参数，只需要按顺序完成每一步。

## 推荐流程

```text
安装 Python
    ↓
连接 TTL Adapter (A)
    ↓
确认串口号
    ↓
运行 ping 或读取脚本
    ↓
确认设备 ID 和波特率
    ↓
进入具体产品教程
```

## 第一步：安装 Python

按照你的系统安装 Python 3.8 或更高版本：

- [安装 Python](../tutorials/install-python.md)

安装完成后确认版本：

=== "Linux"

    ```bash
    python3 --version
    ```

=== "MacOS"

    ```bash
    python3 --version
    ```

=== "Windows"

    ```powershell
    py -3 --version
    ```

## 第二步：连接硬件

第一次测试建议只连接一个设备。多个新设备同时接入时，如果它们默认 ID 相同，会导致总线通信冲突。

- [供电与接线基础](../tutorials/power-and-wiring-basics.md)
- [TTL Adapter (A) 供电与接线](../reference/bus-devices/ttl-adapter-a/power-and-wiring.md)

## 第三步：确认串口

连接 TTL Adapter (A) 后，系统会识别出一个串口设备。

- [查找串口设备](../tutorials/find-serial-port.md)

## 第四步：运行脚本

先运行读取类或 ping 类脚本，不要直接运行会让电机高速运动的脚本。

- [运行 Python 脚本](../tutorials/run-python-scripts.md)

## 第五步：确认设备 ID

大多数灵影 TTL 总线设备出厂默认 ID 为 `1`，默认波特率为 `1000000`。如果你连接多个设备，必须先把它们改成不同 ID。

- [设备 ID 与波特率](../tutorials/device-id-and-baudrate.md)
- [FD 调试软件](../tutorials/fd-tool.md)

## 第六步：进入产品教程

| 你使用的产品 | 推荐继续阅读 |
| --- | --- |
| TTL Encoder E02 | [硬件安装](../reference/bus-devices/ttl-encoder-e02/hardware-installation.md) → [Python 读取](../reference/bus-devices/ttl-encoder-e02/python-quickstart.md) |
| TTL Stepper Driver (A) | [硬件接线](../reference/bus-devices/ttl-stepper-driver-a/hardware-wiring.md) → [Python 控制](../reference/bus-devices/ttl-stepper-driver-a/python-quickstart.md) |
| TTL Adapter (A) | [驱动与串口](../reference/bus-devices/ttl-adapter-a/drivers-and-ports.md) |

!!! warning "先读后写"
    第一次使用时建议先完成 `ping`、读取位置、读取速度等操作。确认通信稳定后，再运行会控制电机或舵机运动的示例。
