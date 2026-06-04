# Communication Troubleshooting

Use this checklist when a TTL bus device cannot be detected, a script cannot open its port, or a read or ping fails.

## Identify the Failure Stage

| Symptom | Check first |
| --- | --- |
| No serial port appears | USB cable, driver, USB port, USB hub |
| Python cannot open the port | Port name, permissions, another application using the port |
| Port opens but ping fails | Device ID, baud rate, power, bus wire order |
| Ping succeeds but an actuator does not move | External power, operating mode, current, limit switches, torque enable |
| Synchronous read fails | Nonexistent IDs, duplicate IDs, excessive bus length, insufficient power |

## 1. Confirm the Serial Port

Start with [Find the serial port](find-serial-port.md). If no port appears, try another data-capable USB cable and USB port, bypass the USB hub, and install the CH343 or CH34X driver.

## 2. Verify the Port Name

The script must use the port detected by the operating system:

```python
portHandler = PortHandler('COM3')
```

Do not use a Linux path on Windows or a COM port name on Linux.

## 3. Match the Baud Rate

The configured rate must match the device:

```python
portHandler.setBaudRate(1000000)
```

## 4. Use the Correct Device ID

Reading ID 1 fails when the device is configured as ID 2:

```python
packetHandler.ReadPosSpeed(1)
```

Change the code to the actual ID or scan the bus with FD.

## 5. Verify Power

USB power may be enough for low-power configuration, but it is not a suitable working supply for actuators. Connect a compatible external supply for stepper drivers, bus servos, wheel modules, and similar products.

## 6. Eliminate Duplicate IDs

Do not connect several new devices that all use factory-default ID 1. Configure one device at a time.

## 7. Read Only Existing IDs

If the bus contains IDs 1, 2, and 3, do not add IDs 4 through 10 to a synchronous read:

```python
for scs_id in range(1, 4):
    groupSyncRead.addParam(scs_id)
```

## 8. Return to a Minimum Test System

Reduce the setup to:

```text
Computer + USB cable + TTL Adapter (A) + one TTL device + correct power supply
```

Run a `ping` or read-only example. Add hubs, extension cables, and additional devices only after the minimum setup works.
