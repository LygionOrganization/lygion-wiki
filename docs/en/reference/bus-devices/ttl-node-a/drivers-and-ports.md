# TTL Node (A) Drivers and Serial Ports

Connect the Type-C port with a data-capable cable. If no serial port appears, install the USB serial driver listed in [Install the USB Serial Driver](../../../tutorials/install-usb-serial-driver.md).

Find the port with:

```bash
python -m serial.tools.list_ports
```

Typical names are `COM7` on Windows, `/dev/ttyUSB0` or `/dev/ttyACM0` on Linux, and `/dev/cu.usbserial-*` on macOS.

## Parallel TTL Bus

Connect TTL data, ground, and a compatible power rail in parallel. Every device needs a unique ID, and all devices must use the same baud rate.

For communication failures, check the selected port, baud rate, device ID, common ground, connector polarity, and whether another application has opened the serial port.

