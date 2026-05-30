# TTL Stepper Driver (A)

TTL Stepper Driver (A) is a compact bipolar stepper motor driver with a single-wire TTL serial bus interface. It allows a standard two-phase stepper motor to be controlled like a bus servo: the host only needs to send position, speed, current, and configuration commands, while the driver handles low-level step generation, acceleration/deceleration, feedback, limit handling, and protection logic.

This guide explains how to connect the TTL Stepper Driver (A), how to control it with the Python SDK, and how to understand the most important parameters such as position, speed, acceleration, current, limit switches, and heartbeat protection.

!!! info "Who this guide is for"
    This document is intended for first-time users of TTL Stepper Driver (A). If you are already familiar with Lygion TTL bus devices, you can skip directly to the Python SDK examples.

---

## 1. Feature Overview

TTL Stepper Driver (A) supports:

- Single-wire TTL bus communication
- Position control mode
- Speed control mode
- Slave synchronization mode
- Multi-device sync write
- Multi-device sync read
- Position and speed feedback
- Voltage, temperature, moving-state, and target-position feedback
- Current position reference calibration
- ID, mode, and resolution configuration
- MIN and LIMIT switch inputs
- Heartbeat protection in speed mode
- Automatic current limiting, over-current protection, and over-temperature protection
- Mixed use with other Lygion TTL bus devices
- Mixed use with Feetech STS / SMS / HLS TTL bus servos

Typical applications include robotic joints, linear actuators, lead-screw slides, turntables, wheel modules, grippers, education platforms, robotic arms, and multi-motor synchronized mechanisms.

![TTL Stepper Driver (A) Product View](assets/images/ttlsd-01.png){ .img-rounded width="300" }

---

## 2. Specifications

| Item | Specification |
| --- | --- |
| Product name | TTL Stepper Driver (A) |
| Communication | Single-wire TTL bus |
| Default baud rate | 1 Mbps |
| Input voltage | DC 9–26V |
| Maximum current | 1.5A |
| Motor type | Bipolar stepper motor |
| Microstepping | 1, 1/2, 1/4, 1/8, 1/16, 1/32 default |
| Control modes | Position mode / Speed mode / Slave sync mode |
| Feedback | Current position, current speed, voltage, temperature, moving state, target position, etc. |
| Limit inputs | MIN / LIMIT |
| Sync interface | EDS IN / EDS OUT |
| SDK support | Python SDK, C/C++ SDK, example programs |

!!! warning "Check the bus voltage before powering the system"
    TTL Stepper Driver (A) supports DC 9–26V input. If other devices are connected to the same TTL bus, make sure every device on the bus can tolerate the selected supply voltage.

---

## 3. Interfaces and Wiring

TTL Stepper Driver (A) integrates the power and TTL bus connector, stepper motor connector, limit switch connectors, and EDS synchronization connectors.

Before powering the board, check the following:

- The power supply is within DC 9–26V.
- The stepper motor phases are wired correctly.
- The TTL bus `+ / - / S` pins are connected correctly.
- There are no duplicate IDs on the same bus.
- Limit switches, if used, are connected to the correct inputs.

![TTL Stepper Driver (A) Basic Parameters](assets/images/ttlsd-02-en.png){ .img-rounded }

---

## 4. Hardware Connection

### 4.1 Control from PC / Raspberry Pi / Jetson / Mac

For development on a computer or single-board computer, use [TTL Adapter (A)](ttl-adapter-a.md) to convert USB to the single-wire TTL bus.

```text
PC / Raspberry Pi / Jetson / Mac
        │ USB
        ▼
TTL Adapter (A)
        │ 5264-3P TTL Bus
        ▼
TTL Stepper Driver (A)
        │
        ▼
Stepper Motor
```

TTL Adapter (A) can also provide the bus power input. In typical use, connect a DC 9–26V power supply to TTL Adapter (A), then power TTL Stepper Driver (A) through the TTL bus.

!!! warning "Do not power the stepper motor from USB only"
    USB is only suitable for communication or very low-power devices. A stepper motor requires an external DC 9–26V power supply. Without external power, the motor may not run correctly and communication may become unstable.

---

### 4.2 Control from Arduino / ESP32S3 / STM32 and Other MCUs

There are three common ways to control TTL Stepper Driver (A) from an MCU.

#### Option A: Use Lygion ESP32S3 Robot Driver

```text
ESP32S3 Robot Driver
        │ 5264-3P TTL Bus
        ▼
TTL Stepper Driver (A)
        │
        ▼
Stepper Motor
```

Lygion ESP32S3 Robot Driver includes an onboard UART-to-single-wire-TTL circuit, so it can directly connect to Lygion TTL bus devices.

#### Option B: Design Your Own UART-to-Single-Wire-TTL Circuit

```text
MCU UART
        │
        ▼
UART-to-single-wire-TTL circuit
        │
        ▼
TTL Stepper Driver (A)
```

This is suitable for custom robot controllers or embedded control boards.

#### Option C: Connect MCU UART to TTL Adapter (A)

```text
ESP32 / STM32 UART
        │ RX → RX
        │ TX → TX
        ▼
TTL Adapter (A)
        │
        ▼
TTL Stepper Driver (A)
```

!!! note "RX / TX wiring note"
    When TTL Adapter (A) is used as a bus transceiver board, the external MCU UART is usually connected as `RX → RX` and `TX → TX`. This is different from the cross-wiring used by many ordinary USB-TTL modules.

---

## 5. Software Environment

The Python examples support:

- Windows
- Linux
- macOS
- Raspberry Pi
- Jetson

The C++ / Arduino examples support:

- ESP32S3
- ESP32
- Arduino Mega2560
- STM32 Arduino Core
- Other controllers with a stable hardware UART

Recommended Python version:

```text
Python >= 3.8
```

Get the Python SDK:

```bash
git clone https://github.com/LygionOrganization/lygion_devs_py.git
cd lygion_devs_py
```

If GitHub is not accessible, download the SDK from this site:

[Download Python SDK](assets/files/lygion_devs_py.zip)

C++ SDK:

```text
https://github.com/LygionOrganization/lygion_devs_cpp
```

If GitHub is not accessible, download the C++ SDK from this site:

[Download C++ SDK](assets/files/lygion_devs_cpp.zip)

---

## 6. Find the Serial Port Name

After connecting TTL Adapter (A), confirm the serial port name recognized by your operating system.

| System | Common serial port name |
| --- | --- |
| Windows | `COM3`, `COM4`, `COMx` |
| Linux | `/dev/ttyUSB0`, `/dev/ttyAMA0` |
| macOS | `/dev/tty.usbserial-xxxx` |

On Windows, open **Device Manager → Ports (COM & LPT)**.

On Linux, you can run:

```bash
ls /dev/ttyUSB*
```

or:

```bash
dmesg | grep tty
```

!!! tip "CH343 / CH34X driver"
    TTL Adapter (A) uses the CH343 USB-to-serial chip. Some Linux, Raspberry Pi, or older systems may require the CH343 / CH34X driver before the serial port appears.

---

## 7. Important Notes Before First Use

### 7.1 Default ID

The default ID of TTL Stepper Driver (A) is usually:

```text
1
```

When setting up multiple drivers for the first time, do not connect several new boards with the same default ID to the same bus.

Recommended procedure:

```text
1. Connect only one new driver board.
2. Change its ID.
3. Disconnect it.
4. Connect the next new driver board.
5. Assign a different ID to each board.
6. After all IDs are unique, connect all boards to the same bus.
```

!!! warning "Do not use duplicate IDs"
    Two devices with the same ID on one TTL bus will respond at the same time. This may cause read failures, abnormal data, unexpected motion, or unstable communication.

### 7.2 Default Baud Rate

The default baud rate is:

```text
1000000
```

This means 1 Mbps.

If you have changed the baud rate, the SDK example must use the same value. When mixing multiple bus devices, all devices on the same bus should use the same baud rate.

### 7.3 Changing ID, Mode, or Resolution

You can configure ID, operating mode, and resolution either with the FD servo debugging software on Windows or with SDK configuration examples.

!!! note
    The FD software workflow is introduced in [Getting Started](../getting-started.md#fd-software).

    - [Download FD software](../assets/files/FD.7z)

---

## 8. Operating Modes

TTL Stepper Driver (A) has three common operating modes:

| Mode | Name | Typical use |
| --- | --- | --- |
| Mode 0 | Position mode | Move the motor to a target position |
| Mode 1 | Speed mode | Run forward, reverse, or stop continuously |
| Mode 2 | Slave sync mode | Let one or more driver boards follow a master board through the EDS sync interface |

### 8.1 Position Mode

Position mode moves the motor to a target position.

Typical command:

```python
packetHandler.WritePosEx(ID, position, speed, acc, current)
```

Parameter meaning:

| Parameter | Description |
| --- | --- |
| `ID` | Device ID |
| `position` | Target position |
| `speed` | Speed parameter |
| `acc` | Acceleration parameter |
| `current` | Target phase current parameter |

With the default settings, one revolution of the stepper motor corresponds to 3200 microsteps. The position range is approximately `0–65534`, so the default maximum control range is about 20.5 revolutions.

!!! tip "When to use position mode"
    Position mode is suitable for turntables, robotic joints, lead-screw slides, grippers, and other mechanisms that need to move to a specific position.

---

### 8.2 Speed Mode

Speed mode makes the motor run continuously.

Typical workflow:

```python
packetHandler.WheelMode(ID)
packetHandler.WriteSpec(ID, speed, acc, current)
```

The speed value can be positive or negative:

```text
speed > 0: forward rotation
speed < 0: reverse rotation
speed = 0: stop
```

!!! warning "Use heartbeat protection in speed mode"
    In speed mode, the motor may continue running if the host program crashes, the bus disconnects, or the controller goes offline. Configure heartbeat protection so the driver automatically stops the motor if no new command is received within the specified time.

---

### 8.3 Slave Sync Mode

Slave sync mode is used when several stepper motors must move together. Typical applications include:

- Multi-lead-screw lifting platforms
- Dual-motor synchronized drive
- Parallel mechanisms
- Multi-axis structures where several motors must remain mechanically synchronized

Basic setup:

```text
1. Set the slave device to Mode 2.
2. Set the slave device sub-ID so it follows the master device.
3. Connect the EDS sync connectors using GH1.25-3P cables.
4. Control only the master ID. The slave devices will follow automatically.
```

EDS connection direction:

```text
Master EDS OUT  →  Slave EDS IN
Slave EDS OUT   →  Next slave EDS IN
```

!!! warning "Do not reverse the EDS direction"
    The EDS sync interface has a direction. Use `master EDS OUT → slave EDS IN`. Do not connect it in reverse.

!!! note "Slave sync mode vs. bus sync write"
    Bus sync write can also start several motors nearly at the same time. However, for mechanisms such as multi-lead-screw lifting platforms, EDS slave sync is usually safer because synchronization is handled at the device level rather than only by application-layer timing. If the master device has a limit switch, the limit behavior can also be applied consistently through the synchronized motion structure.

![EDS Sync Control](assets/images/ttlsd-03.png){ .img-rounded }

---

## 9. Position, Speed, Acceleration, and Current Parameters

### 9.1 Position Parameter

Default setting:

```text
1 motor revolution = 3200 microsteps
Position range = 0–65534
Maximum travel ≈ 65534 / 3200 ≈ 20.48 revolutions
```

To increase the multi-turn control range, change the angle resolution parameter. This parameter can be set through the FD software or by SDK script. Valid range:

```text
1–128
```

For example, if the angle resolution parameter is set to `3`, the effective steps per revolution become:

```text
3200 / 3
```

Then the actual range represented by position `0–65534` becomes approximately:

```text
65534 / (3200 / 3) ≈ 61.44 revolutions
```

!!! info "Resolution vs. range"
    Increasing the angle resolution parameter expands the multi-turn range in position mode, but it reduces position control precision.

---

### 9.2 Speed Parameter

With the default phase setting, the speed parameter unit is:

```text
50 microsteps/s
```

For example, if the speed parameter is `400`:

```text
400 × 50 = 20000 microsteps/s
```

With 3200 microsteps per revolution, the speed is:

```text
400 × 50 × 60 / 3200 = 375 RPM
```

Conversion:

```text
RPM = speed parameter × 50 × 60 / 3200
speed parameter = RPM × 3200 / 50 / 60
```

!!! tip "Recommended starting speed"
    As a general starting point, keep the speed parameter at or below `400`. Higher speeds depend on motor inductance, input voltage, phase current, load inertia, and acceleration settings, and should be tested gradually.

!!! note "Speed is not changed by the resolution parameter"
    The value `3200` used in the speed calculation is fixed for the default phase setting. Reducing position resolution increases the position-mode travel range, but does not increase the speed calculation range. Higher maximum speed requires advanced phase-related configuration and must be verified with the actual motor and load.

---

### 9.3 Acceleration Parameter

When commanding motor motion, use a reasonable acceleration value. Avoid using `0` for real applications unless you fully understand the mechanical load.

```text
Acceleration parameter unit = 100 microsteps/s²
```

!!! warning "Meaning of acceleration = 0"
    `acc = 0` means the highest acceleration, close to an immediate speed change. If the motor only vibrates, stalls easily, loses steps, or stops under light load, reduce the target speed and use a non-zero acceleration value.

A suitable acceleration value helps the motor start, stop, and change speed smoothly while reducing the risk of losing steps.

---

### 9.4 Current Parameter

TTL Stepper Driver (A) sets the motor phase current, not the input current shown on a power supply.

The onboard HR8825 driver uses chopper current control to limit the current in the motor winding. The examples often use:

```python
current = 150
```

!!! note "Phase current is not the same as power supply current"
    The current shown by a bench power supply is the DC bus input current drawn by the driver. It depends on input voltage, motor resistance, motor inductance, speed, load, microstepping, and driver efficiency. Therefore, even with the same current parameter, the power supply current may be different with different voltages or motors. This is normal.

Approximate phase current:

```text
Phase current ≈ 3.3 × 2 × (parameter / 1000)
```

Example when the parameter is `200`:

```text
Phase current ≈ 3.3 × 2 × (200 / 1000) = 1.32A
```

---

## 10. Limit Switches

TTL Stepper Driver (A) provides two limit switch inputs:

```text
MIN
LIMIT
```

Each limit connector has three pins:

```text
S / + / -
```

When the `S` pin is pulled high, the corresponding limit function is triggered.

![Limit Switch Wiring](assets/images/ttlsd-04.png){ .img-rounded }

### 10.1 Mechanical Limit Switch

For a common mechanical limit switch, use the normally-open wiring:

```text
One side of the switch → S
Other side of the switch → +
```

When the switch is pressed, `S` is pulled high and the limit is triggered.

### 10.2 Photoelectric / Inductive Limit Switch

For photoelectric or inductive limit switches, a PNP output type is recommended.

```text
Switch positive → +
Switch negative → -
Switch signal → S
```

When the switch is triggered, its signal output goes high and activates the corresponding limit input.

### 10.3 Limit Logic in Different Modes

#### Position Mode (Mode = 0)

In position mode, only the `LIMIT` input is active.

```text
LIMIT is used as the maximum-position limit.
After it is triggered, the motor cannot continue moving toward a larger target position.
It can still move toward a smaller target position.
```

#### Speed Mode (Mode = 1)

In speed mode, both `MIN` and `LIMIT` inputs are active.

```text
MIN: limits negative-direction motion
LIMIT: limits positive-direction motion
```

### 10.4 Homing with Speed Mode

For a lead-screw mechanism with a limit switch, homing is usually performed in speed mode.

Typical homing process:

```text
1. After power-on, set the driver to speed mode (Mode 1).
2. Command the motor to move toward the MIN limit.
3. The motor moves in the homing direction.
4. The MIN limit is triggered and the motor stops.
5. Set the current position as the zero reference.
6. Switch back to position mode (Mode 0).
```

!!! tip "Why homing usually uses speed mode"
    After power-on, the driver treats its current position as 0, and the normal position-mode range is usually `0–65534`. Homing often requires moving toward a physical end stop first, so it is usually done in speed mode. After homing, the system has a clear mechanical zero reference.

---

## 11. Heartbeat Protection

Heartbeat protection improves safety in speed mode. It is only active in Mode 1.

If the host does not send a new control command within the configured time, the driver automatically stops the motor. This helps prevent wheels or actuators from continuing to move after a program crash, communication loss, or controller disconnection.

Heartbeat time can be set through the FD software or by script. Make sure you set:

```text
Heartbeat protection time
```

not:

```text
Protection time
```

The unit is:

```text
100 ms
```

For example, if the value is set to `30`:

```text
30 × 100 ms = 3000 ms = 3 s
```

This means the motor will automatically stop if it does not receive a new command within 3 seconds.

---

## 12. Python SDK Quick Start

### 12.1 Common Initialization Code

All Python examples share a similar serial initialization structure:

```python
import sys
import os

sys.path.append("..")
from lydevs_sdk import *

portHandler = PortHandler('/dev/ttyUSB0')
packetHandler = TTLSDClass(portHandler)

if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    quit()

if portHandler.setBaudRate(1000000):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()
```

Modify the serial port name for your system:

```python
# Windows
portHandler = PortHandler('COM3')

# Linux
portHandler = PortHandler('/dev/ttyUSB0')

# macOS
portHandler = PortHandler('/dev/tty.usbserial-xxxx')
```

---

### 12.2 Test Communication with `ttlsd_ping.py`

Example file:

```text
ttlsd_ping.py
```

This example checks whether a device with the specified ID is online.

Core command:

```python
model_number, result, error = packetHandler.ping(1)
```

A successful response looks like:

```text
[ID:001] ping Succeeded. lynode model number : xxx
```

If ping fails, check the serial port, baud rate, device ID, power supply, and wiring.

---

### 12.3 Read Position and Speed with `ttlsd_read.py`

Example file:

```text
ttlsd_read.py
```

This example continuously reads the current position and speed of ID 1.

Core command:

```python
position, speed, result, error = packetHandler.ReadPosSpeed(1)
```

Run:

```bash
python ttlsd_read.py
```

Example output:

```text
[ID:001] PresPos:3200 PresSpd:0
```

Return values:

| Return value | Meaning |
| --- | --- |
| `position` | Current motor position |
| `speed` | Current motor speed |
| `result` | Communication result |
| `error` | Device error status |

---

### 12.4 Position Control with `ttlsd_write.py`

Example file:

```text
ttlsd_write.py
```

This example moves the motor between two positions.

Core command:

```python
packetHandler.WritePosEx(1, 3200, 600, 0, 150)
```

Parameter meaning:

```text
ID = 1
Target position = 3200
Speed parameter = 600
Acceleration parameter = 0
Current parameter = 150
```

!!! warning "Example speed and acceleration are for demonstration"
    The example values `speed=600` and `acc=0` are intended for quick testing only. In real applications, start with lower speed, use a reasonable non-zero acceleration, and increase values gradually according to the motor and load.

A safer starting command:

```python
packetHandler.WritePosEx(1, 3200, 200, 10, 150)
```

---

### 12.5 Move and Read Status with `read_write.py`

Example file:

```text
read_write.py
```

This example sends a position command, then repeatedly reads position, speed, and moving state until the motor reaches the target.

Core status-reading commands:

```python
position, speed, result, error = packetHandler.ReadPosSpeed(ID)
moving, result, error = packetHandler.ReadMoving(ID)
```

When `moving == 0`, the motion has finished.

This example is useful when your application needs to wait until the motor has reached its target before continuing.

---

### 12.6 Speed Control with `ttlsd_wheel.py`

Example file:

```text
ttlsd_wheel.py
```

This example controls the motor in speed mode.

First set the driver to speed mode:

```python
packetHandler.WheelMode(1)
```

Then send speed commands:

```python
packetHandler.WriteSpec(1, 600, 0, 150)
packetHandler.WriteSpec(1, 0, 0, 150)
packetHandler.WriteSpec(1, -600, 0, 150)
```

Meaning:

```text
600: forward rotation
0: stop
-600: reverse rotation
```

!!! warning "Speed mode safety"
    Before using speed mode, configure heartbeat protection and make sure the mechanism cannot cause damage if it runs continuously. For first tests, use a low speed such as `100` or `200`.

---

### 12.7 Sync Read Multiple Devices with `sync_read.py`

Example file:

```text
sync_read.py
```

This example reads position and speed from multiple devices on the same bus.

The default example reads ID 1–10:

```python
for scs_id in range(1, 11):
    groupSyncRead.addParam(scs_id)
```

If you only have ID 1, 2, and 3, change it to:

```python
for scs_id in range(1, 4):
    groupSyncRead.addParam(scs_id)
```

You can also add specific IDs manually:

```python
groupSyncRead.addParam(1)
groupSyncRead.addParam(3)
groupSyncRead.addParam(7)
```

!!! warning "Only read IDs that actually exist"
    Add only devices that are physically connected and configured with the expected ID. If the list includes missing IDs, sync read may fail or wait until timeout.

---

### 12.8 Sync Write Multiple Devices with `sync_write.py`

Example file:

```text
sync_write.py
```

This example packages target position, speed, acceleration, and current parameters for multiple devices and sends them in one bus transaction.

Core commands:

```python
packetHandler.SyncWritePosEx(scs_id, 3200, 600, 0, 150)
packetHandler.groupSyncWrite.txPacket()
packetHandler.groupSyncWrite.clearParam()
```

Typical use cases:

- Start several joints at nearly the same time
- Move several slides together
- Reduce start-time differences between multiple motors

For only ID 1, 2, and 3:

```python
for scs_id in range(1, 4):
    packetHandler.SyncWritePosEx(scs_id, 3200, 200, 50, 150)
```

---

### 12.9 Preload Commands with `reg_write.py`, Then Execute Together

Example file:

```text
reg_write.py
```

This example first writes target parameters into the internal register buffer of each device, then triggers all buffered commands with `RegAction()`.

Core commands:

```python
packetHandler.RegWritePosEx(scs_id, 3200, 600, 0, 150)
packetHandler.RegAction()
```

Comparison:

| Method | Description |
| --- | --- |
| `SyncWrite` | Broadcasts target parameters for multiple devices in one packet |
| `RegWrite + RegAction` | Writes parameters to device buffers first, then triggers execution together |

---

### 12.10 Set Current Position Reference with `ttlsd_ofscal.py`

Example file:

```text
ttlsd_ofscal.py
```

This example sets the current actual position to a specified value.

Core command:

```python
packetHandler.reOfsCal(1, 1024)
```

Meaning:

```text
Set the current position of ID 1 to 1024.
```

Typical uses:

- Set the mechanical zero point to `0`
- Set the current position to a middle value such as `1600`
- Set the zero point after a homing operation
- Calibrate a batch of mechanisms after assembly

!!! note "Calibration is not saved after power-off"
    For TTL Stepper Driver (A), the reference set by `reOfsCal()` is not retained after power-off. After each power cycle, recalibrate the reference position based on homing or external encoder feedback as required by your application.

---

### 12.11 Configure Parameters with `ttlsd_eprom.py`

Example file:

```text
ttlsd_eprom.py
```

This example shows how to unlock EPROM and configure parameters such as ID, operating mode, and resolution.

Common flow:

```python
packetHandler.TorqueEn(1, 0)
packetHandler.unLockEprom(1)
packetHandler.SetID(254, 1)
packetHandler.SetMode(1, 0)
packetHandler.SetResolution(1, 1)
packetHandler.LockEprom(1)
```

!!! warning "Connect only one target device when changing a new product ID"
    New devices often ship with the same default ID. When changing an ID, connect only one device to the bus to avoid modifying the wrong device.

!!! note "About broadcast ID 254"
    `SetID(254, 1)` uses broadcast ID 254 to set a device ID. Use this only when there is exactly one device on the bus.

---

### 12.12 Restore Factory Settings with `ttlsd_recover.py`

Example file:

```text
ttlsd_recover.py
```

Core command:

```python
packetHandler.Recover(1)
```

This restores the target device to factory settings.

!!! danger "Use factory reset carefully"
    Factory reset may change important parameters such as ID, mode, and resolution. Before running this command, make sure only the target device is on the bus and record the current configuration if needed.

---

## 13. C++ / Arduino SDK Overview

If you use ESP32S3, ESP32, Arduino Mega2560, STM32 Arduino Core, or another MCU, you can also control TTL Stepper Driver (A) with the C++ / Arduino SDK.

Common C++ examples:

| Example | Purpose |
| --- | --- |
| `FeedBack.ino` | Read position, speed, voltage, temperature, and other feedback |
| `WritePos.ino` | Position mode control |
| `WriteSpe.ino` | Speed mode control |
| `SyncRead.ino` | Sync read multiple devices |
| `SyncWritePos.ino` | Sync write target positions |
| `SyncWriteSpe.ino` | Sync write target speeds |
| `RegWritePos.ino` | Preload position command and execute later |
| `ProgramEprom.ino` | Configure device parameters |
| `CalibrationOfs.ino` | Set the current position reference |

Typical ESP32S3 serial configuration:

```cpp
Serial1.begin(1000000, SERIAL_8N1, 18, 17);
ttlsd.pSerial = &Serial1;
```

Typical Arduino Mega2560 serial configuration:

```cpp
Serial1.begin(1000000);
ttlsd.pSerial = &Serial1;
```

!!! tip "Use a hardware UART"
    The default bus speed is 1 Mbps. Use a hardware UART whenever possible. Software serial is not recommended for stable high-speed TTL bus communication.

---

## 14. Common Function Reference

| Function | Purpose |
| --- | --- |
| `packetHandler.ping(ID)` | Check whether a device is online |
| `packetHandler.ReadPosSpeed(ID)` | Read current position and speed |
| `packetHandler.ReadMoving(ID)` | Read moving state |
| `packetHandler.WritePosEx(ID, pos, speed, acc, current)` | Position mode control |
| `packetHandler.WheelMode(ID)` | Set speed mode |
| `packetHandler.WriteSpec(ID, speed, acc, current)` | Speed mode control |
| `packetHandler.SyncWritePosEx(ID, pos, speed, acc, current)` | Add one device to a sync-write position packet |
| `packetHandler.groupSyncWrite.txPacket()` | Send the sync-write packet |
| `packetHandler.RegWritePosEx(ID, pos, speed, acc, current)` | Preload a position command |
| `packetHandler.RegAction()` | Execute preloaded register commands |
| `packetHandler.reOfsCal(ID, position)` | Set current position reference |
| `packetHandler.TorqueEn(ID, enable)` | Enable or disable output |
| `packetHandler.unLockEprom(ID)` | Unlock EPROM |
| `packetHandler.LockEprom(ID)` | Lock EPROM |
| `packetHandler.SetID(old_id, new_id)` | Change device ID |
| `packetHandler.SetMode(ID, mode)` | Set operating mode |
| `packetHandler.GetMode(ID)` | Read operating mode |
| `packetHandler.SetResolution(ID, resolution)` | Set position resolution |
| `packetHandler.Recover(ID)` | Restore factory settings |

---

## 15. Common Workflows

### 15.1 Single-Motor Position Control

```text
1. Connect TTL Adapter (A).
2. Connect TTL Stepper Driver (A).
3. Connect the stepper motor.
4. Apply DC 9–26V external power.
5. Confirm the serial port name.
6. Run ttlsd_ping.py to confirm communication.
7. Use ttlsd_eprom.py or FD software to confirm Mode 0.
8. Run ttlsd_write.py to move to a target position.
9. Use ttlsd_read.py or read_write.py to monitor position and moving state.
```

### 15.2 Single-Motor Speed Control

```text
1. Confirm motor and driver wiring.
2. Configure heartbeat protection first if possible.
3. Set the driver to speed mode.
4. Run ttlsd_wheel.py.
5. Test forward, stop, and reverse at a low speed first.
```

### 15.3 Multi-Motor Sync Control

```text
1. Assign a unique ID to each driver board.
2. Make sure all drivers use the same baud rate.
3. Connect all drivers to the same TTL bus.
4. Use sync_read.py to confirm all devices respond correctly.
5. Use sync_write.py or reg_write.py to send synchronized motion commands.
```

### 15.4 Lead-Screw Homing

```text
1. Install the MIN limit switch.
2. Set the driver to speed mode.
3. Command the motor to move toward the MIN direction.
4. The motor stops when the MIN limit is triggered.
5. Use reOfsCal() to set the current position to 0.
6. Switch back to position mode.
7. Use position mode for precise motion control.
```

---

## 16. Troubleshooting

### Q1: The serial port cannot be found. What should I check?

Possible causes:

- CH343 / CH34X driver is not installed.
- The USB cable only supports charging, not data.
- TTL Adapter (A) is not connected correctly.
- The operating system does not have permission to access the serial port.

Solutions:

- Use a USB cable that supports data transfer.
- Check Device Manager on Windows for a CH343 serial device.
- Install the CH343 / CH34X driver on Linux or Raspberry Pi if needed.
- On Linux, check whether the current user has serial port permissions.

---

### Q2: Ping works, but the motor does not rotate. Why?

Check:

- External DC 9–26V power is connected.
- The stepper motor phases are wired correctly.
- The motor is a bipolar stepper motor.
- The current parameter is not too low.
- The operating mode is correct.
- A limit switch is not currently triggered.
- Torque output is not disabled.
- The mechanical load is not too large.

---

### Q3: The motor only vibrates, stalls, or loses steps. What should I do?

Common causes:

- Speed parameter is too high.
- Acceleration is too high or set to `0`.
- Current parameter is too low.
- Input voltage is too low.
- The motor has high winding inductance and poor high-speed performance.
- Load inertia is too large.
- Microstepping setting is not suitable.

Recommended steps:

```text
1. Reduce the speed parameter.
2. Use a small but non-zero acceleration.
3. Increase the current parameter carefully.
4. Increase input voltage within the safe range of the motor and driver.
5. Test the motor without load first.
6. Increase the load gradually.
```

---

### Q4: Why is the power supply current different from the current parameter?

The driver current parameter sets the phase current in the motor winding. It is not the same as the DC input current shown by the power supply.

The power supply current is affected by input voltage, motor resistance, motor inductance, speed, load, microstepping, and driver efficiency. Therefore, different voltages or motors may show different supply currents even with the same phase-current setting.

---

### Q5: How should I understand the speed parameter?

By default, the speed unit is:

```text
50 microsteps/s
```

With 3200 microsteps per revolution:

```text
RPM = speed parameter × 50 × 60 / 3200
```

Example when speed parameter is `400`:

```text
400 × 50 × 60 / 3200 = 375 RPM
```

---

### Q6: Why does position mode control only about 20.5 revolutions by default?

By default:

```text
1 revolution = 3200 microsteps
Position range = 0–65534
65534 / 3200 ≈ 20.48 revolutions
```

To increase the multi-turn range, change the angle resolution parameter. For example, if it is set to `3`:

```text
65534 / (3200 / 3) ≈ 61.44 revolutions
```

The tradeoff is lower position precision.

---

### Q7: After a limit switch is triggered, why can the motor still move in the opposite direction?

This is expected.

A limit switch blocks motion further into the dangerous direction, but it allows the motor to move away from the limit. Otherwise, once a limit is triggered, the mechanism would be unable to leave the limit position.

---

### Q8: What is heartbeat protection?

Heartbeat protection is a safety feature for speed mode.

If the host stops sending new commands, the driver automatically stops the motor after the configured timeout. This prevents wheels or actuators from continuing to move after a program crash, communication loss, or controller disconnection.

Heartbeat time unit:

```text
100 ms
```

Example value:

```text
30 × 100 ms = 3 s
```

---

### Q9: How do I synchronize multiple motors?

There are two common methods:

```text
Method 1: Bus sync write
Use sync_write.py or RegWrite + RegAction to send target commands to multiple drivers with very small timing differences.

Method 2: EDS slave synchronization
Set slave drivers to Mode 2 and connect EDS IN / OUT so they follow a master driver at the device level.
```

Bus sync write is suitable for general multi-axis motion. EDS slave synchronization is better for multi-lead-screw lifting platforms, dual-motor synchronized drive, and other mechanisms that require strong low-level synchronization.

---

### Q10: Can TTL Stepper Driver (A) share a bus with bus servos or TTL Encoder E02?

Yes.

TTL Stepper Driver (A) can be connected to the same TTL bus as Feetech STS / SMS / HLS bus servos, Lygion TTL Encoder E02, and other Lygion TTL bus devices.

Requirements:

- Device IDs must be unique.
- Baud rates must match.
- The bus voltage must be compatible with all connected devices.
- The power supply must be stable enough for the number of devices and motors on the bus.

---

## 17. Example Code Locations

Python SDK:

```text
https://github.com/LygionOrganization/lygion_devs_py
```

Relevant Python examples:

```text
ttlsd_ping.py
ttlsd_read.py
ttlsd_write.py
ttlsd_wheel.py
read_write.py
sync_read.py
sync_write.py
reg_write.py
ttlsd_ofscal.py
ttlsd_eprom.py
ttlsd_recover.py
```

C++ SDK:

```text
https://github.com/LygionOrganization/lygion_devs_cpp
```

Relevant C++ / Arduino examples:

```text
FeedBack.ino
WritePos.ino
WriteSpe.ino
SyncRead.ino
SyncWritePos.ino
SyncWriteSpe.ino
RegWritePos.ino
ProgramEprom.ino
CalibrationOfs.ino
```

---

## 18. Resources

### FD Servo Debugging Software

- [Download FD software](../assets/files/FD.7z)

### SDK

[GitHub Python SDK](https://github.com/LygionOrganization/lygion_devs_py)

[GitHub C++ SDK](https://github.com/LygionOrganization/lygion_devs_cpp)

If GitHub is not accessible, download from this site:

[Download Python SDK](assets/files/lygion_devs_py.zip)

[Download C++ SDK](assets/files/lygion_devs_cpp.zip)

### STEP Model

[TTL Stepper Driver (A) STEP](assets/files/TTL_SD_Simple Assembly.step)
