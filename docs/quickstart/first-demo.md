# 跑通第一个 Demo

本页用于完成第一次通信测试。建议第一次测试使用 **TTL Adapter (A) + TTL Encoder E02**，因为编码器功耗低，测试风险更小。如果你使用的是 TTL Stepper Driver (A)，也可以按照相同流程运行 `ttlsd_ping.py` 或读取示例。

## 1. 连接硬件

典型连接方式：

```text
Computer / Raspberry Pi / Jetson / Mac
        │ USB
        ▼
TTL Adapter (A)
        │ TTL Bus
        ▼
TTL Bus Device
```

检查以下项目：

- USB 线是数据线，不是只能充电的线。
- TTL 总线的 `+ / - / S` 没有接反。
- 如果连接执行器类设备，已接入外部电源。
- 同一根总线上暂时只接一个新设备，避免默认 ID 冲突。

## 2. 准备 Python 环境

=== "Linux"

    ```bash
    python3 --version
    python3 -m venv .venv
    source .venv/bin/activate
    ```

=== "MacOS"

    ```bash
    python3 --version
    python3 -m venv .venv
    source .venv/bin/activate
    ```

=== "Windows"

    ```powershell
    py -3 --version
    py -3 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

不确定 Python 是否已经安装，请先看：[安装 Python](../tutorials/install-python.md)。

## 3. 获取 SDK

```bash
git clone https://github.com/LygionRobotics/lygion_devs_py.git
cd lygion_devs_py
```

如果无法访问 GitHub，可以从下载中心获取压缩包：

- [Python SDK](../downloads/index.md#python-sdk)

## 4. 找到串口名称

=== "Linux"

    ```bash
    ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
    dmesg | grep tty
    ```

    常见名称：`/dev/ttyUSB0`、`/dev/ttyACM0`。

=== "MacOS"

    ```bash
    ls /dev/tty.usb* /dev/cu.usb* 2>/dev/null
    ```

    常见名称：`/dev/tty.usbserial-xxxx` 或 `/dev/cu.usbserial-xxxx`。

=== "Windows"

    打开“设备管理器 → 端口（COM 和 LPT）”，查看类似 `USB-Enhanced-SERIAL CH343 (COM3)` 的设备。

    常见名称：`COM3`、`COM4`、`COM12`。

更详细说明见：[查找串口设备](../tutorials/find-serial-port.md)。

## 5. 修改示例脚本中的串口

打开示例脚本，找到：

```python
portHandler = PortHandler('/dev/ttyUSB0')
```

根据系统改成你的实际串口：

```python
# Linux
portHandler = PortHandler('/dev/ttyUSB0')

# MacOS
portHandler = PortHandler('/dev/tty.usbserial-xxxx')

# Windows
portHandler = PortHandler('COM3')
```

## 6. 运行通信测试

优先运行 `ping` 或读取类脚本，不要一开始就运行电机运动脚本。

=== "Linux"

    ```bash
    python3 ttlsd_ping.py
    ```

=== "MacOS"

    ```bash
    python3 ttlsd_ping.py
    ```

=== "Windows"

    ```powershell
    python .\ttlsd_ping.py
    ```

如果输出中出现 `Succeeded` 或能持续读取到位置、速度数据，说明通信已经打通。

## 7. 下一步

根据你正在使用的产品继续阅读：

| 产品 | 下一步 |
| --- | --- |
| TTL Encoder E02 | [Python 读取编码器](../reference/bus-devices/ttl-encoder-e02/python-quickstart.md) |
| TTL Stepper Driver (A) | [Python 控制步进驱动](../reference/bus-devices/ttl-stepper-driver-a/python-quickstart.md) |
| TTL Adapter (A) | [驱动与串口](../reference/bus-devices/ttl-adapter-a/drivers-and-ports.md) |

!!! tip "遇到问题先看这里"
    找不到串口、读取失败、无法打开端口、ping 不通等问题，请先看：[常见通信问题排查](../tutorials/communication-troubleshooting.md)。
