# FD Device Utility

FD is a Windows graphical utility for scanning TTL bus devices, changing IDs and baud rates, viewing feedback, editing parameters, and updating firmware.

## When to Use FD

- Confirm that a new device is online.
- Find an unknown device ID.
- Change an ID or baud rate.
- Inspect a device before writing code.
- Check or restore parameters.

## Download

[Download FD](../../assets/files/FD.7z){ .md-button }

## Basic Workflow

```text
1. Connect TTL Adapter (A).
2. Connect one bus device.
3. Apply external power when the device is an actuator.
4. Open FD.
5. Select the correct COM port and baud rate.
6. Scan for the device.
7. Read or change parameters.
```

When changing an ID, connect only one device. Scan again afterward to confirm the new ID.

## Troubleshooting

### No device is found

Check the COM port, baud rate, device power, TTL bus wire order, and duplicate IDs.

### The device is found but does not move

Check the external actuator supply, operating mode, limit inputs, and configured current.
