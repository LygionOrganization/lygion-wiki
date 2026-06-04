# Read TTL Encoder E02 with Python

TTL Encoder E02 shares several SDK interfaces with TTL Stepper Driver (A). For the encoder, use position, speed, synchronous read, and reference-calibration functions.

Before starting, complete the [Python first demo](../../../quickstart/python-first-demo.md).

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

## Read One Encoder

```python
while True:
    position, speed, result, error = packetHandler.ReadPosSpeed(1)
    if result != COMM_SUCCESS:
        print(packetHandler.getTxRxResult(result))
    else:
        angle_deg = position / 4096.0 * 360.0
        speed_deg_s = speed / 4096.0 * 360.0
        print(f"pos={position}, angle={angle_deg:.2f} deg, speed={speed_deg_s:.2f} deg/s")
    time.sleep(0.1)
```

One revolution equals 4096 position steps. Raw speed is reported in steps per second.

## Synchronously Read Multiple Encoders

```python
ids = [1, 2, 3]
groupSyncRead = GroupSyncRead(packetHandler, LY_TTLSD_PRESENT_POSITION_L, 4)

for device_id in ids:
    groupSyncRead.addParam(device_id)

result = groupSyncRead.txRxPacket()

for device_id in ids:
    available, error = groupSyncRead.isAvailable(
        device_id, LY_TTLSD_PRESENT_POSITION_L, 4
    )
    if available:
        position = groupSyncRead.getData(
            device_id, LY_TTLSD_PRESENT_POSITION_L, 2
        )
        speed = groupSyncRead.getData(
            device_id, LY_TTLSD_PRESENT_POSITION_L + 2, 2
        )
        print(device_id, position, speed)

groupSyncRead.clearParam()
```

!!! warning "Add only IDs that are physically present"
    A missing ID can cause a synchronous read to fail or time out.

## Set the Current Angle Reference

Set the current angle of encoder ID 1 to position 1024:

```python
result, error = packetHandler.reOfsCal(1, 1024)
```

At 12-bit resolution:

```text
1024 = 90 degrees
2048 = 180 degrees
3072 = 270 degrees
```

The single-turn calibration reference is retained after power loss.
