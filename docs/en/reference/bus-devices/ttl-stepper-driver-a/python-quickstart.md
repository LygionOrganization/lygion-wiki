# Control TTL Stepper Driver (A) with Python

Complete the [Python first demo](../../../quickstart/python-first-demo.md) before commanding motion.

## Initialize the Port

```python
import sys
import time

sys.path.append("..")
from lydevs_sdk import *

portHandler = PortHandler('/dev/ttyUSB0')
packetHandler = TTLSDClass(portHandler)

if not portHandler.openPort():
    print("Failed to open the port")
    quit()

if not portHandler.setBaudRate(1000000):
    print("Failed to set the baud rate")
    quit()
```

Replace `/dev/ttyUSB0` with the serial port on your system.

## 1. Ping the Driver

```python
model_number, result, error = packetHandler.ping(1)
```

A successful ping confirms the serial port, baud rate, and device ID.

## 2. Read Position and Speed

```python
position, speed, result, error = packetHandler.ReadPosSpeed(1)
print(position, speed)
```

Confirm stable feedback before commanding motion.

## 3. Move to a Position

```python
packetHandler.WritePosEx(1, 3200, 200, 10, 150)
```

```text
ID = 1
Target position = 3200
Speed parameter = 200
Acceleration parameter = 10
Current parameter = 150
```

Begin with a speed around `100-200` and acceleration around `10-50`.

## 4. Read Feedback During Motion

```python
packetHandler.WritePosEx(1, 3200, 200, 10, 150)

while True:
    position, speed, result, error = packetHandler.ReadPosSpeed(1)
    moving, result, error = packetHandler.ReadMoving(1)
    print(position, speed, moving)
    if moving == 0:
        break
    time.sleep(0.05)
```

## 5. Run in Speed Mode

```python
packetHandler.WheelMode(1)
packetHandler.WriteSpec(1, 100, 10, 150)
time.sleep(2)
packetHandler.WriteSpec(1, 0, 10, 150)
```

Speed may be positive, negative, or zero. Enable heartbeat protection before using continuous speed mode in a real mechanism.

## 6. Synchronously Read Multiple Drivers

```python
groupSyncRead = GroupSyncRead(packetHandler, LY_TTLSD_PRESENT_POSITION_L, 4)

for device_id in [1, 2, 3]:
    groupSyncRead.addParam(device_id)

groupSyncRead.txRxPacket()
groupSyncRead.clearParam()
```

Add only IDs that are connected.

## 7. Synchronously Start Multiple Moves

```python
for device_id in [1, 2, 3]:
    packetHandler.SyncWritePosEx(device_id, 3200, 200, 10, 150)

packetHandler.groupSyncWrite.txPacket()
packetHandler.groupSyncWrite.clearParam()
```

## 8. Assign the Current Position

```python
packetHandler.reOfsCal(1, 0)
```

This assigns the requested position value to the current physical position. Whether the result is retained after power loss can depend on the firmware version.
