# Find the Serial Port

When TTL Adapter (A) is connected, the operating system exposes it as a USB serial port. The SDK must use that port name to communicate.

| Operating system | Typical port names |
| --- | --- |
| Linux | `/dev/ttyUSB0`, `/dev/ttyACM0` |
| macOS | `/dev/tty.usbserial-xxxx`, `/dev/cu.usbserial-xxxx` |
| Windows | `COM3`, `COM4`, `COM12` |

## Find the Port

=== "Linux"

    Connect TTL Adapter (A), then run:

    ```bash
    ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
    dmesg | grep tty
    ```

    Use the detected port in your script:

    ```python
    portHandler = PortHandler('/dev/ttyUSB0')
    ```

=== "macOS"

    Connect TTL Adapter (A), then run:

    ```bash
    ls /dev/tty.usb* /dev/cu.usb* 2>/dev/null
    ```

    Use the detected port in your script:

    ```python
    portHandler = PortHandler('/dev/tty.usbserial-xxxx')
    ```

=== "Windows"

    1. Right-click the Start button and open **Device Manager**.
    2. Expand **Ports (COM & LPT)**.
    3. Find an entry such as `USB-Enhanced-SERIAL CH343 (COM3)`.
    4. Use that COM port in your script:

    ```python
    portHandler = PortHandler('COM3')
    ```

## Linux Serial-Port Permissions

If the port exists but your program reports a permission error, add your account to the `dialout` group:

```bash
sudo usermod -aG dialout $USER
```

Log out and back in, or restart the computer, before trying again.

## Can the Port Name Change?

Yes. The port can change after reconnecting the adapter, using a different USB socket, or adding another USB serial device. Confirm the port before running an example.
