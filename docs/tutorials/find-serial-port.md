# 查找串口设备

连接 TTL Adapter (A) 后，系统会识别出一个 USB 串口设备。Python SDK 需要使用这个串口名称打开通信端口。

## 常见串口名称

| 系统 | 常见名称 |
| --- | --- |
| Linux | `/dev/ttyUSB0`、`/dev/ttyACM0` |
| MacOS | `/dev/tty.usbserial-xxxx`、`/dev/cu.usbserial-xxxx` |
| Windows | `COM3`、`COM4`、`COM12` |

## 查找方法

=== "Linux"

    插入 TTL Adapter (A) 后运行：

    ```bash
    ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
    dmesg | grep tty
    ```

    如果看到 `/dev/ttyUSB0`，脚本中通常写：

    ```python
    portHandler = PortHandler('/dev/ttyUSB0')
    ```

=== "MacOS"

    插入 TTL Adapter (A) 后运行：

    ```bash
    ls /dev/tty.usb* /dev/cu.usb* 2>/dev/null
    ```

    如果看到 `/dev/tty.usbserial-xxxx`，脚本中写：

    ```python
    portHandler = PortHandler('/dev/tty.usbserial-xxxx')
    ```

=== "Windows"

    1. 右键点击“开始”。
    2. 打开“设备管理器”。
    3. 展开“端口（COM 和 LPT）”。
    4. 查找类似 `USB-Enhanced-SERIAL CH343 (COM3)` 的设备。

    如果端口是 `COM3`，脚本中写：

    ```python
    portHandler = PortHandler('COM3')
    ```

## Linux 串口权限

如果 Linux 能看到串口，但程序提示权限不足，可以把当前用户加入 `dialout` 组：

```bash
sudo usermod -aG dialout $USER
```

执行后需要注销并重新登录，或重启系统。

## 端口名称会变化吗？

会。更换 USB 口、同时连接多个 USB 串口设备、重新插拔设备后，端口号可能变化。运行脚本前建议再次确认端口名称。
