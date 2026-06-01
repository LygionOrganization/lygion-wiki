# TTL Adapter (A) 驱动与串口

TTL Adapter (A) 使用 CH343 USB 转串口芯片。连接电脑后，系统会识别出一个串口设备。

## 常见串口名称

| 系统 | 常见串口名称 |
| --- | --- |
| Linux | `/dev/ttyUSB0`、`/dev/ttyACM0` |
| MacOS | `/dev/tty.usbserial-xxxx`、`/dev/cu.usbserial-xxxx` |
| Windows | `COM3`、`COM4`、`COM12` |

## 快速查找

=== "Linux"

    ```bash
    ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
    dmesg | grep tty
    ```

=== "MacOS"

    ```bash
    ls /dev/tty.usb* /dev/cu.usb* 2>/dev/null
    ```

=== "Windows"

    打开“设备管理器 → 端口（COM 和 LPT）”，查找 CH343 或 USB Serial 设备。

## 驱动安装

如果系统无法识别串口，请参考：

- [安装 USB 串口驱动](../../../tutorials/install-usb-serial-driver.md)

## Python 中的写法

```python
# Linux
portHandler = PortHandler('/dev/ttyUSB0')

# MacOS
portHandler = PortHandler('/dev/tty.usbserial-xxxx')

# Windows
portHandler = PortHandler('COM3')
```

## 排查顺序

1. 换 USB 数据线。
2. 换 USB 口。
3. 确认驱动。
4. 确认串口没有被其它软件占用。
5. 确认 Python 脚本中的端口名称正确。

详细排查见：[常见通信问题排查](../../../tutorials/communication-troubleshooting.md)。
