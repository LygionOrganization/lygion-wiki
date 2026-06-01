# Python 路线：跑通第一个 Demo

本页把原来的“跑通第一个 Demo”和“新手路径”合并为一条完整流程。你只需要按顺序完成每一步，就可以确认电脑已经能通过 TTL Adapter (A) 与 Lygion TTL 总线设备通信。

推荐第一次测试使用：

```text
Computer / Raspberry Pi / Jetson / Mac
        │ USB
        ▼
TTL Adapter (A)
        │ TTL Bus
        ▼
TTL Encoder E02 或 TTL Stepper Driver (A)
```

!!! tip "第一次测试推荐 TTL Encoder E02"
    TTL Encoder E02 功耗低，测试风险小。只要能读取位置和速度，就说明串口、总线、ID 和波特率基本正常。

    如果你使用 TTL Stepper Driver (A)，第一次也建议先运行 `ping` 或读取类脚本，确认通信后再运行电机运动示例。

## 1. 准备硬件

你需要准备：

- TTL Adapter (A)
- 一个 TTL 总线设备，例如 TTL Encoder E02 或 TTL Stepper Driver (A)
- USB Type-C **数据线**
- 合适电压的外部电源
- 电脑、Raspberry Pi、Jetson 或其它 SBC

检查以下项目：

- USB 线不是只能充电的线。
- TTL 总线的 `+ / - / S` 没有接反。
- 同一根总线上暂时只接一个新设备。
- 如果连接步进电机、舵机或其它执行器，已经接入外部电源。

!!! warning "不要只依赖 USB 给执行器供电"
    USB 通常只适合通信和低功耗调试。驱动步进电机、舵机或其它执行器时，请接入符合设备规格的外部电源。

    不确定如何接线时，请先阅读：[供电与接线基础](../tutorials/power-and-wiring-basics.md)。

## 2. 打开终端工具

后面的步骤需要输入命令。不同系统打开命令行工具的方法不同。

=== "Linux"

    常见方法：

    - 按 `Ctrl + Alt + T`。
    - 或在应用菜单中搜索 `Terminal`。

    打开后会看到类似这样的窗口，可以输入命令：

    ```bash
    username@computer:~$
    ```

=== "MacOS"

    常见方法：

    - 按 `Command + Space` 打开 Spotlight。
    - 输入 `Terminal` 或 `终端`。
    - 回车打开。

    打开后会看到类似这样的窗口：

    ```bash
    username@MacBook ~ %
    ```

=== "Windows"

    推荐使用 **PowerShell**：

    - 右键点击 Windows 开始菜单。
    - 选择 `终端`、`Windows PowerShell` 或 `Terminal`。

    也可以使用 CMD：

    - 按 `Win + R`。
    - 输入 `cmd`。
    - 回车打开。

    后续 Windows 示例默认使用 PowerShell。

更多说明见：[如何打开终端 / CMD / PowerShell](../tutorials/open-terminal.md)。

## 3. 确认 Python 是否可用

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

如果显示类似 `Python 3.10.x`、`Python 3.11.x`、`Python 3.12.x`，说明 Python 已经安装。

如果提示找不到命令，请先阅读：[安装 Python](../tutorials/install-python.md)。

## 4. 获取 Python SDK

推荐使用 Git 获取 SDK：

=== "Linux"

    ```bash
    git clone https://github.com/LygionRobotics/lygion_devs_py.git
    cd lygion_devs_py
    ```

=== "MacOS"

    ```bash
    git clone https://github.com/LygionRobotics/lygion_devs_py.git
    cd lygion_devs_py
    ```

=== "Windows"

    ```powershell
    git clone https://github.com/LygionRobotics/lygion_devs_py.git
    cd lygion_devs_py
    ```

如果无法访问 GitHub，可以从下载中心下载压缩包：

- [Python SDK 下载](../downloads/index.md#python-sdk)

!!! note "不会使用 Git 也可以继续"
    下载 ZIP 后解压到一个容易找到的位置，例如桌面或 `D:\Lygion\lygion_devs_py`，然后在终端中进入该目录即可。

## 5. 创建并启用 Python 虚拟环境

虚拟环境用于把当前项目用到的 Python 包与系统环境隔离，避免以后项目变多时互相影响。

=== "Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

=== "MacOS"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

=== "Windows"

    ```powershell
    py -3 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

如果 Windows 提示无法运行脚本，可以临时使用：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

不熟悉这一步时，请阅读：[运行 Python 脚本](../tutorials/run-python-scripts.md)。

## 6. 找到串口名称

连接 TTL Adapter (A) 后，系统会识别出一个串口设备。你需要把这个串口名称写到示例脚本里。

=== "Linux"

    ```bash
    ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
    dmesg | grep tty
    ```

    常见名称：

    ```text
    /dev/ttyUSB0
    /dev/ttyACM0
    ```

=== "MacOS"

    ```bash
    ls /dev/tty.usb* /dev/cu.usb* 2>/dev/null
    ```

    常见名称：

    ```text
    /dev/tty.usbserial-xxxx
    /dev/cu.usbserial-xxxx
    ```

=== "Windows"

    打开：

    ```text
    设备管理器 → 端口（COM 和 LPT）
    ```

    查找类似下面的设备：

    ```text
    USB-Enhanced-SERIAL CH343 (COM3)
    ```

    其中 `COM3` 就是脚本中要使用的串口名称。

更详细说明见：[查找串口设备](../tutorials/find-serial-port.md)。

## 7. 修改示例脚本中的串口

打开你要运行的示例脚本，找到类似这一行：

```python
portHandler = PortHandler('/dev/ttyUSB0')
```

根据你的系统改成实际串口：

```python
# Linux
portHandler = PortHandler('/dev/ttyUSB0')

# macOS
portHandler = PortHandler('/dev/tty.usbserial-xxxx')

# Windows
portHandler = PortHandler('COM3')
```

默认波特率通常保持为：

```python
portHandler.setBaudRate(1000000)
```

默认设备 ID 通常为：

```python
1
```

!!! warning "同一根总线上不要有重复 ID"
    多个新设备可能都有默认 ID `1`。第一次修改 ID 时，建议总线上只连接一个设备。

## 8. 运行第一个测试脚本

优先运行 `ping` 或读取类脚本。下面命令中的脚本名称需要根据 SDK 实际目录调整。

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

如果通信正常，通常会看到类似输出：

```text
[ID:001] ping Succeeded.
```

如果你使用 TTL Encoder E02，也可以运行读取位置和速度的示例：

=== "Linux"

    ```bash
    python3 ttlsd_read.py
    ```

=== "MacOS"

    ```bash
    python3 ttlsd_read.py
    ```

=== "Windows"

    ```powershell
    python .\ttlsd_read.py
    ```

成功后会看到类似：

```text
[ID:001] PresPos:1200 PresSpd:0
```

## 9. 成功后继续学习

| 你使用的产品 | 下一步 |
| --- | --- |
| TTL Encoder E02 | [TTL Encoder E02：Python 读取](../reference/bus-devices/ttl-encoder-e02/python-quickstart.md) |
| TTL Stepper Driver (A) | [TTL Stepper Driver (A)：Python 控制](../reference/bus-devices/ttl-stepper-driver-a/python-quickstart.md) |
| TTL Adapter (A) | [TTL Adapter (A)：驱动与串口](../reference/bus-devices/ttl-adapter-a/drivers-and-ports.md) |

## 10. 如果没有成功

优先检查下面几项：

| 现象 | 常见原因 | 处理方式 |
| --- | --- | --- |
| 找不到串口 | USB 线不是数据线；驱动未安装 | 更换 USB 线；安装 CH343 / CH34X 驱动 |
| 打不开串口 | 串口号写错；端口被其它软件占用 | 确认串口名；关闭 FD 软件或其它串口工具 |
| ping 失败 | ID 错误；波特率错误；接线错误；供电不足 | 检查 ID、波特率、`+/-/S`、电源 |
| 电机不转 | 没有外部电源；电流太低；模式错误 | 接入外部电源；降低速度；检查模式 |

更多问题见：[常见通信问题排查](../tutorials/communication-troubleshooting.md)。
