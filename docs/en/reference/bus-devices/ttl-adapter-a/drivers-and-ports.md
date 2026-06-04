# TTL Adapter (A) Drivers and Serial Ports

TTL Adapter (A) uses a CH343 USB-to-serial controller. After connection, the operating system exposes it as a serial port.

| Operating system | Typical port names |
| --- | --- |
| Linux | `/dev/ttyUSB0`, `/dev/ttyACM0` |
| macOS | `/dev/tty.usbserial-xxxx`, `/dev/cu.usbserial-xxxx` |
| Windows | `COM3`, `COM4`, `COM12` |

## Find the Port

=== "Linux"

    ```bash
    ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
    dmesg | grep tty
    ```

=== "macOS"

    ```bash
    ls /dev/tty.usb* /dev/cu.usb* 2>/dev/null
    ```

=== "Windows"

    Open **Device Manager -> Ports (COM & LPT)** and find the CH343 or USB Serial entry.

If no port appears, follow [Install the USB serial driver](../../../tutorials/install-usb-serial-driver.md).

## Use the Port in Python

```python
# Linux
portHandler = PortHandler('/dev/ttyUSB0')

# macOS
portHandler = PortHandler('/dev/cu.usbserial-xxxx')

# Windows
portHandler = PortHandler('COM3')
```

If the port will not open, replace the USB cable, try another USB socket, verify the driver, close other serial applications, and confirm the port name. See [Communication troubleshooting](../../../tutorials/communication-troubleshooting.md).
