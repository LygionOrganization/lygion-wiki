# Install the USB Serial Driver

TTL Adapter (A) uses a CH343 USB-to-serial controller. Most current operating systems recognize it automatically, but some Windows, Linux, or older systems require a CH343 or CH34X driver.

## Do You Need a Driver?

You normally do not need to install anything if the adapter appears as:

- `COMx` in Windows Device Manager
- `/dev/ttyUSB0` or `/dev/ttyACM0` on Linux
- `/dev/tty.usbserial-xxxx` on macOS

Install a driver if no port appears or Windows Device Manager shows an unknown device with a warning icon.

## Windows

1. Connect TTL Adapter (A).
2. Open Device Manager.
3. Check **Ports (COM & LPT)** and **Other devices**.
4. If the adapter appears as an unknown device, install the CH343 or CH34X driver.
5. Disconnect and reconnect the adapter.

## Linux

Linux usually includes the required driver. Check detection with:

```bash
lsusb
ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
```

If the device appears but the port cannot be opened, add your user to the `dialout` group:

```bash
sudo usermod -aG dialout $USER
```

Then log out and back in.

## macOS

Check for a detected port:

```bash
ls /dev/tty.usb* /dev/cu.usb* 2>/dev/null
```

## If the Adapter Is Still Not Detected

1. Confirm that the USB cable supports data, not charging only.
2. Try a different USB port.
3. Close other serial applications.
4. If using a virtual machine, attach the USB device to the guest system.
5. Bypass low-quality USB hubs.
