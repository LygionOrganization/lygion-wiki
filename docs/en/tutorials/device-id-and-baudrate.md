# Device IDs and Baud Rates

The TTL bus supports multiple devices on one signal line. For reliable communication:

1. Every device on the bus must have a unique ID.
2. Every device must use the same baud rate as the controller.

## Typical Factory Defaults

| Setting | Typical default |
| --- | --- |
| Device ID | `1` |
| Baud rate | `1000000` |

Defaults can vary by product or production batch. Confirm them on the product page or from the factory configuration.

## Why IDs Must Be Unique

Two devices with the same ID respond to the same command at the same time. This can cause failed reads, corrupted replies, unexpected motion, and unstable communication.

## Safely Assign IDs to New Devices

```text
1. Connect only one new device to the bus.
2. Change its ID with FD or an SDK example.
3. Ping the new ID to confirm the change.
4. Disconnect it and repeat for the next device.
5. Connect all devices only after every ID is unique.
```

Windows users can scan devices and change IDs with the [FD device utility](fd-tool.md).

## Change an ID with the SDK

The exact API varies by product. The following examples show the general EEPROM workflow.

### Python

```python
# Enable EEPROM writes. 254 is the broadcast ID.
packetHandler.unLockEprom(254)

# Set the new ID to 1.
packetHandler.SetID(254, 1)

# Lock EEPROM again using the new device ID.
packetHandler.LockEprom(1)
```

### C++

```cpp
// Enable EEPROM writes. 254 is the broadcast ID.
hlscl.unLockEprom(254);

// Set the new ID to 1.
hlscl.writeByte(254, HLSCL_ID, 1);

// Lock EEPROM again using the new device ID.
hlscl.LockEprom(1);
```

!!! warning "Connect only one target device when using a default or broadcast ID"
    A broadcast write can change every connected device. Isolate the device you intend to configure.

## Baud-Rate Mismatch

Communication fails when the controller uses `1000000` but the device uses another baud rate. Use FD to scan common baud rates, change the baud rate in your code, or restore the device configuration when necessary.
