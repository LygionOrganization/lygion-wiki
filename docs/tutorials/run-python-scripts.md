# 运行 Python 脚本

本文说明如何在 Linux、macOS 和 Windows 中运行 Lygion Python SDK 示例脚本。

如果你还不知道如何打开终端，请先阅读：

- [如何打开终端 / CMD / PowerShell](open-terminal.md)

## 1. 进入 SDK 目录

假设你已经获取了 Python SDK：

```text
lygion_devs_py
```

需要先进入这个目录。

=== "Linux"

    ```bash
    cd ~/lygion_devs_py
    ```

=== "MacOS"

    ```bash
    cd ~/lygion_devs_py
    ```

=== "Windows"

    ```powershell
    cd $env:USERPROFILE\Desktop\lygion_devs_py
    ```

如果你把 SDK 解压到了其它位置，请把命令中的路径改成你的实际路径。

## 2. 创建虚拟环境

建议每个 Python 项目单独使用虚拟环境。

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

启用成功后，终端前面通常会出现：

```text
(.venv)
```

## 3. Windows 无法激活虚拟环境怎么办？

如果 PowerShell 显示类似：

```text
running scripts is disabled on this system
```

可以在当前 PowerShell 窗口中执行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

该设置只对当前窗口生效，关闭窗口后不会长期改变系统策略。

## 4. 修改脚本中的串口

打开示例脚本，找到：

```python
portHandler = PortHandler('/dev/ttyUSB0')
```

改成你的实际串口：

=== "Linux"

    ```python
    portHandler = PortHandler('/dev/ttyUSB0')
    ```

=== "MacOS"

    ```python
    portHandler = PortHandler('/dev/tty.usbserial-xxxx')
    ```

=== "Windows"

    ```python
    portHandler = PortHandler('COM3')
    ```

不知道串口名称时，请阅读：[查找串口设备](find-serial-port.md)。

## 5. 运行脚本

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

如果脚本在子目录中，例如：

```text
lyttlsd/ttlsd_read.py
```

则运行：

=== "Linux / macOS"

    ```bash
    python3 lyttlsd/ttlsd_read.py
    ```

=== "Windows"

    ```powershell
    python .\lyttlsd\ttlsd_read.py
    ```

## 6. 运行成功的判断

如果通信正常，可能看到：

```text
[ID:001] ping Succeeded.
```

或：

```text
[ID:001] PresPos:1200 PresSpd:0
```

这说明：

- 串口可以打开。
- 波特率基本正确。
- 设备 ID 正确。
- TTL 总线通信正常。

## 7. 常见错误

### 找不到 Python

=== "Linux / macOS"

    ```bash
    python3 --version
    ```

=== "Windows"

    ```powershell
    py -3 --version
    ```

如果无法显示版本，请先安装 Python：[安装 Python](install-python.md)。

### 找不到脚本文件

请确认你当前所在目录是否正确：

=== "Linux / macOS"

    ```bash
    pwd
    ls
    ```

=== "Windows"

    ```powershell
    pwd
    dir
    ```

### 打不开串口

常见原因：

- 串口名称写错。
- FD 软件或其它串口工具占用了端口。
- Windows 驱动未安装。
- Linux 用户没有串口访问权限。

请阅读：[查找串口设备](find-serial-port.md) 和 [安装 USB 串口驱动](install-usb-serial-driver.md)。
