# TTL Encoder E02

TTL Encoder E02 is a compact 12-bit absolute magnetic encoder with single-wire TTL bus communication. It is designed for reading angular position and speed feedback from robotic mechanisms, such as robot arms, dexterous hands, gear or pulley shafts, reducer output shafts, turntables, steering modules, and other rotary structures.

This guide explains how to connect the encoder, read angle and speed data with the Python SDK and the C++ / Arduino SDK, and set the current mechanical position as a user-defined reference position.

!!! info "Who this guide is for"
    This guide is intended for first-time users of TTL Encoder E02. If you are already familiar with Lygion TTL bus devices, you can skip directly to the Python or C++ example sections.

---

## 1. Features

TTL Encoder E02 supports:

- Absolute angle feedback
- Speed feedback
- Multi-device synchronous reading
- User-defined position reference calibration
- Power-off retention of calibration data
- Mixed use with Lygion TTL bus devices
- Mixed use with Feetech STS / SMS / HLS TTL bus servos

TTL Encoder E02 detects the rotation angle of a radial magnet. The encoder PCB is fixed to the mechanical structure, while the radial magnet is mounted on the rotating shaft or moving part. When the magnet rotates, the encoder outputs the current angular position and speed through the TTL bus.

![TTL Encoder E02 Product View](assets/images/ttle02-01.png){ .img-rounded }

---

## 2. Specifications

| Item | Specification |
| --- | --- |
| Product model | TTL Encoder E02 |
| Communication | Single-wire TTL bus |
| Default baud rate | 1 Mbps |
| Factory default ID | 1 |
| ID range | 1 ~ 252 |
| Input voltage | DC 5~28V |
| Angle feedback | 12-bit absolute angle |
| Single-turn position range | 0~4095 |
| Multi-turn position range | 0~65534, not retained after power-off |
| Speed unit | steps/s |
| Connector | HC-1.25-3P |
| Pin definition | `- / + / S` |
| Operating current | <10mA |
| PCB diameter | Approx. 16mm |
| SDK | Python SDK / C++ SDK |

!!! warning "Check bus voltage before connection"
    TTL Encoder E02 supports a wide DC 5~28V input range. If other devices are connected to the same TTL bus, make sure every device on the bus supports the selected bus voltage.

---

## 3. How It Works

TTL Encoder E02 measures the angular position of a radial magnet and outputs real-time position and speed data.

A typical installation structure is:

```text
Rotating shaft / gear / pulley
        │
        │  Radial magnet mounted on the rotating part
        ▼
Radial magnet rotates with the shaft
        │
        ▼
TTL Encoder E02 detects the magnetic field angle
        │
        ▼
Position and speed are output through the TTL bus
```

In 12-bit mode, one full rotation is divided into 4096 steps:

```text
0 ~ 4095 = 0° ~ 360°
```

Position-to-angle conversion:

```python
angle_deg = position_steps / 4096.0 * 360.0
```

For example, if the reading changes from `1200` to `2300`, the position difference is:

```text
2300 - 1200 = 1100 steps
```

The corresponding angle change is:

```text
1100 / 4096 × 360 ≈ 96.68°
```

This means the radial magnet has rotated about `96.68°` relative to the encoder.

Speed is returned in `steps/s`. It can be converted to degrees per second:

```python
speed_deg_s = speed_steps_s / 4096.0 * 360.0
```

![TTL Encoder E02 assembly](assets/images/ttle02-02-en.png){ .img-rounded width="300"}

!!! note "Image needed"
    For the English version, consider replacing the image above with an English-labelled version, for example `assets/images/ttle02-02-en.png`.

---

## 4. Installation Requirements

To use TTL Encoder E02, mount a radial magnet on the rotating part and align the magnet center with the encoder IC as closely as possible.

Recommended installation guidelines:

- Use a radial magnet, not a standard axial magnet.
- Keep the magnet and encoder IC as concentric as possible.
- Keep the gap between the magnet and the top surface of the encoder IC at about 1mm.
- The gap should preferably not exceed 1.5mm.
- Minimize eccentricity and wobble during rotation.
- Fix the encoder PCB firmly to avoid movement during operation.

!!! tip "Mechanical alignment"
    TTL Encoder E02 does not require extremely tight machining tolerances, but the relative position between the magnet and the encoder IC directly affects angle stability. If the reading jumps or becomes unstable, first check magnet centering, gap, and mechanical fixing.

---

## 5. Hardware Connection

### 5.1 Using a PC / Raspberry Pi / Jetson / Mac

For desktop or SBC development, use [TTL Adapter (A)](ttl-adapter-a.md) to convert USB to a single-wire TTL bus, then connect TTL Encoder E02 through [HC-1.25 8P Hub (A)](hc-1.25-8p-hub-a.md).

```text
PC / Raspberry Pi / Jetson / Mac
        │ USB
        ▼
TTL Adapter (A)
        │ 5264-3P
        ▼
HC-1.25 8P Hub (A)
        │ HC-1.25-3P
        ▼
TTL Encoder E02
```

Notes:

- TTL Adapter (A) converts USB or UART to the single-wire TTL bus.
- TTL Adapter (A) uses the CH343 USB-to-serial chip.
- HC-1.25 8P Hub (A) expands one 5264-3P bus port into eight HC-1.25-3P ports.
- Multiple hubs can be cascaded to connect more encoders.
- The same bus can also be shared with Feetech STS / SMS / HLS servos or other Lygion TTL bus devices.

TTL Encoder E02 is usually powered through the bus. In a typical setup, DC 5~28V power is connected to TTL Adapter (A), and the encoder receives power through the TTL bus.

![TTL Encoder E02 USB connection](assets/images/ttle02-03.png){ .img-rounded }

---

### 5.2 Using Arduino / ESP32S3 / STM32 and Other MCUs

If you want to control TTL Encoder E02 from an MCU, use one of the following connection methods.

#### Option A: Use [Lygion ESP32S3 Robot Driver](robot-driver-with-esp32s3-lite.md)

```text
ESP32S3 Robot Driver
        │ 5264-3P
        ▼
HC-1.25 8P Hub (A)
        │ HC-1.25-3P
        ▼
TTL Encoder E02
```

The ESP32S3 Robot Driver includes an onboard UART-to-single-wire TTL bus circuit, so it can directly connect to Lygion TTL bus devices.

#### Option B: Use Your Own UART-to-Single-Wire TTL Circuit

```text
MCU UART
        │
        ▼
UART-to-single-wire TTL circuit
        │
        ▼
TTL Encoder E02
```

This option is suitable for custom controller boards or robot control boards.

#### Option C: Connect MCU UART to TTL Adapter (A)

```text
ESP32 / STM32 UART
        │ RX → RX
        │ TX → TX
        ▼
TTL Adapter (A)
        │ 5264-3P
        ▼
HC-1.25 8P Hub (A)
        │ HC-1.25-3P
        ▼
TTL Encoder E02
```

!!! note "RX / TX wiring with TTL Adapter (A)"
    When TTL Adapter (A) is used as a communication adapter for an external MCU, the MCU UART is normally connected as `RX to RX` and `TX to TX`. This is different from the crossed wiring commonly used with basic USB-TTL modules.

---

## 6. Software Environment

Python examples are suitable for:

- Windows
- Linux
- macOS
- Raspberry Pi
- Jetson

C++ / Arduino examples are suitable for:

- ESP32S3
- Arduino Mega2560
- Other controllers with a stable hardware UART

Recommended Python version:

```text
Python >= 3.8
```

Clone the Python SDK:

```bash
git clone https://github.com/LygionOrganization/lygion_devs_py.git
cd lygion_devs_py
```

If GitHub is not accessible, you can also download the SDK from this site:

[Download Python SDK](assets/files/lygion_devs_py.zip)

This guide uses the following Python examples:

```text
lyttlsd/ttlsd_read.py
lyttlsd/sync_read.py
lyttlsd/ttlsd_ofscal.py
```

And the following C++ / Arduino examples:

```text
example/lyttlsd/FeedBack.ino
example/lyttlsd/SyncRead.ino
example/lyttlsd/CalibrationOfs.ino
```

!!! info "About example names"
    TTL Encoder E02 and TTL Stepper Driver (A) share part of the same SDK interface. Some example files, code comments, or class names may include `TTLSD`, `Servo`, or `motor`. For TTL Encoder E02, you mainly use the position reading, speed reading, synchronous reading, and reference calibration functions.

---

## 7. Check the Serial Port Name

After connecting TTL Adapter (A), confirm the serial port name detected by your system.

| System | Common port name |
| --- | --- |
| Windows | `COM3`, `COM4`, `COMx` |
| Linux | `/dev/ttyUSB0`, `/dev/ttyAMA0` |
| macOS | `/dev/tty.usbserial-xxxx` |

On Windows, open **Device Manager → Ports (COM & LPT)** to check the assigned COM port.

On Linux, you can use:

```bash
ls /dev/ttyUSB*
```

or:

```bash
dmesg | grep tty
```

!!! tip "CH343 / CH34X driver"
    TTL Adapter (A) uses the CH343 USB-to-serial chip. Some Linux, Raspberry Pi, or older operating systems may not recognize it automatically. If no serial port appears, install the CH343 / CH34X driver.

---

## 8. Before First Use

### 8.1 Default ID

The factory default ID of TTL Encoder E02 is:

```text
1
```

When configuring multiple new encoders, do not connect several devices with the same default ID to the same bus at the same time.

Recommended workflow:

```text
1. Connect only one new encoder.
2. Change its ID.
3. Disconnect it and connect the next encoder.
4. Assign a unique ID to each encoder.
5. Connect all configured encoders to the same bus.
```

!!! warning "Do not use duplicate IDs"
    Two devices with the same ID on one TTL bus will cause bus conflicts. This can result in read failures, abnormal data, or unstable communication.

### 8.2 Default Baud Rate

The default baud rate is:

```text
1000000
```

That is, `1 Mbps`.

If you have changed the encoder baud rate, make sure the SDK example uses the same baud rate. When multiple devices share the same bus, all devices should use a consistent baud rate.

### 8.3 Change ID or Baud Rate

The simplest way to change the device ID or baud rate is to use the Feetech FD software on Windows.

!!! note
    The FD software workflow is introduced in [Getting Started](../getting-started.md#fd-software).

    - [Download FD software](../assets/files/FD.7z)

---

## 9. Python: Read a Single Encoder with `ttlsd_read.py`

Example file:

```text
lyttlsd/ttlsd_read.py
```

This example reads the current position and speed of one TTL Encoder E02.

### 9.1 Set the Serial Port

Open `ttlsd_read.py` and find the port configuration:

```python
portHandler = PortHandler('/dev/ttyUSB0')
```

Change it to the actual port on your system.

Windows example:

```python
portHandler = PortHandler('COM3')
```

Linux example:

```python
portHandler = PortHandler('/dev/ttyUSB0')
```

macOS example:

```python
portHandler = PortHandler('/dev/tty.usbserial-xxxx')
```

### 9.2 Set the Baud Rate

The default example uses 1 Mbps:

```python
if portHandler.setBaudRate(1000000):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()
```

If your encoder uses another baud rate, replace `1000000` with the actual value.

### 9.3 Set the Device ID

To read the device with ID `1`:

```python
position, speed, result, error = packetHandler.ReadPosSpeed(1)
```

Returned values:

- `position`: current position, commonly used
- `speed`: current rotation speed, commonly used
- `result`: communication status
- `error`: device error status

If your encoder ID is `3`, change the call to:

```python
position, speed, result, error = packetHandler.ReadPosSpeed(3)
```

### 9.4 Run the Example

Run the script from the example directory:

```bash
python ttlsd_read.py
```

If communication is successful, the program will print the current position and speed.

Position unit:

```text
steps
```

In 12-bit mode:

```text
1 turn = 4096 steps
0 ~ 4095 = 0° ~ 360°
```

Angle conversion:

```python
angle_deg = position / 4096.0 * 360.0
```

Speed unit:

```text
steps/s
```

---

## 10. Python: Synchronous Reading with `sync_read.py`

Example file:

```text
lyttlsd/sync_read.py
```

This example reads position and speed from multiple bus devices at the same time. It is useful for robot arms, dexterous hands, multi-joint systems, leader arms, and low-cost closed-loop mechanisms.

### 10.1 Add Device IDs

Example code:

```python
for scs_id in range(1, 11):
    scs_addparam_result = groupSyncRead.addParam(scs_id)
    if scs_addparam_result != True:
        print("[ID:%03d] groupSyncRead addparam failed" % scs_id)
```

This reads devices with IDs `1` to `10`.

If you only have three encoders with IDs `1`, `2`, and `3`, change it to:

```python
for scs_id in range(1, 4):
    scs_addparam_result = groupSyncRead.addParam(scs_id)
    if scs_addparam_result != True:
        print("[ID:%03d] groupSyncRead addparam failed" % scs_id)
```

You can also add specific IDs manually:

```python
groupSyncRead.addParam(1)
groupSyncRead.addParam(3)
groupSyncRead.addParam(7)
```

### 10.2 Run the Example

Run:

```bash
python sync_read.py
```

The example sends one synchronous read request and then parses the returned data from each device.

!!! warning "Only read IDs that actually exist"
    The ID list should only include devices connected to the bus. If the program tries to read an ID that does not exist, synchronous reading may fail or wait until timeout.

### 10.3 Mixed Use with Feetech TTL Bus Servos

TTL Encoder E02 can share the same TTL bus with Feetech STS / SMS / HLS servos.

Example bus layout:

```text
ID 1: TTL Encoder E02
ID 2: TTL Encoder E02
ID 3: STS bus servo
ID 4: HLS bus servo
```

When `sync_read.py` reads IDs `1` to `4`, it can obtain position and speed feedback from these devices at the same time.

!!! warning "Mixed bus requirements"
    When different device types share one bus, make sure IDs are unique, baud rates are consistent, and all devices support the selected bus voltage.

---

## 11. Python: Set Current Position Reference with `ttlsd_ofscal.py`

Example file:

```text
lyttlsd/ttlsd_ofscal.py
```

`ttlsd_ofscal.py` sets the current physical position of the encoder to a specified position value. This is not limited to zeroing; you can assign any supported position value to the current pose.

### 11.1 Example: Set Current Position to 1024

```python
scs_comm_result, scs_error = packetHandler.reOfsCal(1, 1024)
```

Meaning:

```text
Set the current position of the encoder with ID 1 to 1024.
```

In 12-bit mode:

```text
1024 = 90°
```

Conversion:

```python
angle_deg = 1024 / 4096.0 * 360.0
```

### 11.2 Run the Example

Run:

```bash
python ttlsd_ofscal.py
```

After calibration, without moving the encoder or magnet, run the read example again:

```bash
python ttlsd_read.py
```

The position should be close to the value you just set, for example:

```text
position ≈ 1024
```

### 11.3 Is Calibration Saved?

Yes. The result of `reOfsCal()` is saved after power-off.

After the encoder is powered on again, the same calibration reference will still be used.

### 11.4 Typical Applications

This function is useful for:

- Setting the mechanical zero point to `0`
- Setting a joint center position to `2048`
- Setting a specific assembly pose as a known angle
- Calibrating multiple encoders after installation

---

## 12. C++ / Arduino SDK

If you use ESP32S3, ESP32, Arduino Mega2560, STM32 Arduino Core, or another MCU, you can use the C++ / Arduino SDK to read TTL Encoder E02.

C++ SDK examples are located in:

```text
example/lyttlsd/
```

Examples most relevant to TTL Encoder E02:

| Example file | Purpose | Recommended for TTL Encoder E02 |
| --- | --- | --- |
| `FeedBack.ino` | Read position, speed, voltage, temperature, and other feedback data from one device | Yes |
| `SyncRead.ino` | Read position and speed from multiple devices synchronously | Yes |
| `CalibrationOfs.ino` | Set the current position reference | Yes |
| `WritePos.ino` / `WriteSpe.ino` / `SyncWritePos.ino` / `SyncWriteSpe.ino` | Motion control examples for TTL Stepper Driver | Usually not needed |
| `RegWritePos.ino` | Delayed position command writing | Usually not needed |

!!! info "Shared SDK interface"
    The same SDK is also used by TTL Stepper Driver (A), so C++ examples may contain names such as `TTLSDClass`, `Servo`, or `motor`. For TTL Encoder E02, focus on feedback reading, synchronous reading, and reference calibration.

### 12.1 Get the C++ / Arduino SDK

[GitHub C++ SDK](https://github.com/LygionOrganization/lygion_devs_cpp)

If GitHub is not accessible, download it from this site:

[Download C++ SDK](assets/files/lygion_devs_cpp.zip)

After downloading, place the library files in the Arduino IDE `libraries` directory, or open the corresponding `.ino` example according to the SDK folder structure.

!!! tip "Arduino IDE library folder"
    A common Arduino IDE library path is `Documents/Arduino/libraries`. After copying the library files, restart Arduino IDE before opening the example sketch.

### 12.2 UART Configuration

The C++ examples use a hardware serial port to communicate with the TTL bus.

ESP32S3 example:

```cpp
Serial1.begin(1000000, SERIAL_8N1, 18, 17);
ttlsd.pSerial = &Serial1;
```

Meaning:

```text
1000000: TTL bus baud rate, default 1 Mbps
18: ESP32S3 RX pin
17: ESP32S3 TX pin
```

Arduino Mega2560 example:

```cpp
Serial1.begin(1000000);
ttlsd.pSerial = &Serial1;
```

!!! warning "Use only one serial initialization method"
    For ESP32S3, keep `Serial1.begin(1000000, SERIAL_8N1, 18, 17);`. For Mega2560, keep `Serial1.begin(1000000);`. Do not enable both at the same time.

If your encoder baud rate has been changed, replace `1000000` with the actual baud rate.

### 12.3 Read One Encoder with `FeedBack.ino`

`FeedBack.ino` can read feedback data from a TTL Encoder E02 with ID `1`. For TTL Encoder E02, the most commonly used values are position and speed:

```cpp
Pos = ttlsd.ReadPos(-1);
Speed = ttlsd.ReadSpeed(-1);
```

`ReadPos(-1)` and `ReadSpeed(-1)` read values from the feedback buffer that was updated by `FeedBack()`.

Simplified example:

```cpp
#include <lygion_devs.h>

TTLSDClass ttlsd;

void setup()
{
  Serial.begin(115200);

  // ESP32S3: RX = 18, TX = 17
  Serial1.begin(1000000, SERIAL_8N1, 18, 17);

  // Mega2560 can use:
  // Serial1.begin(1000000);

  ttlsd.pSerial = &Serial1;
  delay(1000);
}

void loop()
{
  int pos;
  int speed;

  ttlsd.FeedBack(1);   // Read feedback data from ID 1

  if (!ttlsd.getLastError()) {
    pos = ttlsd.ReadPos(-1);
    speed = ttlsd.ReadSpeed(-1);

    Serial.print("Position:");
    Serial.println(pos);
    Serial.print("Speed:");
    Serial.println(speed);
  } else {
    Serial.println("FeedBack error");
  }

  delay(100);
}
```

You can also directly read position from a specified ID:

```cpp
int pos = ttlsd.ReadPos(1);
```

Or directly read speed:

```cpp
int speed = ttlsd.ReadSpeed(1);
```

Expected serial output:

```text
Position:1200
Speed:35
```

Position and speed use the same units as the Python SDK:

```text
Position: steps, 4096 steps per turn in 12-bit mode
Speed: steps/s
```

Angle conversion:

```cpp
float angle_deg = pos / 4096.0f * 360.0f;
```

Speed conversion:

```cpp
float speed_deg_s = speed / 4096.0f * 360.0f;
```

### 12.4 Synchronous Reading with `SyncRead.ino`

`SyncRead.ino` reads position and speed from multiple TTL bus devices at the same time.

Default example:

```cpp
uint8_t ID[] = {1, 2};
```

This means the program reads devices with ID `1` and ID `2`.

If you have four TTL Encoder E02 modules with IDs `1`, `2`, `3`, and `4`, change it to:

```cpp
uint8_t ID[] = {1, 2, 3, 4};
```

Core synchronous read logic:

```cpp
ttlsd.syncReadPacketTx(ID, sizeof(ID), LY_TTLSD_PRESENT_POSITION_L, sizeof(rxPacket));

for (uint8_t i = 0; i < sizeof(ID); i++) {
  if (!ttlsd.syncReadPacketRx(ID[i], rxPacket)) {
    Serial.print("ID:");
    Serial.println(ID[i]);
    Serial.println("sync read error!");
    continue;
  }

  Position = ttlsd.syncReadRxPacketToWrod(15);
  Speed = ttlsd.syncReadRxPacketToWrod(15);

  Serial.print("ID:");
  Serial.println(ID[i]);
  Serial.print("Position:");
  Serial.println(Position);
  Serial.print("Speed:");
  Serial.println(Speed);
}
```

!!! warning "Confirm IDs before synchronous reading"
    The `ID[]` array should contain only devices that are actually connected. If it contains an ID that is not present on the bus, the read operation may fail or wait for timeout.

### 12.5 Set Position Reference with `CalibrationOfs.ino`

`CalibrationOfs.ino` sets the encoder's current physical position to a specified position value.

Example:

```cpp
ttlsd.CalibrationOfs(1, 1024);
```

Meaning:

```text
Set the current position of the encoder with ID 1 to 1024.
```

In 12-bit mode:

```text
1024 = 90°
2048 = 180°
3072 = 270°
```

Typical workflow:

```text
1. Move the mechanism to the pose you want to use as the reference.
2. Change the device ID and target position in CalibrationOfs.ino.
3. Upload the sketch.
4. Open the Serial Monitor.
5. Confirm that the reported position is close to the target value.
```

The result of `CalibrationOfs()` is saved after power-off. After the encoder is powered on again, it will still use the calibrated reference.

### 12.6 Common C++ Functions

| Function | Purpose | Usage with TTL Encoder E02 |
| --- | --- | --- |
| `ttlsd.ReadPos(ID)` | Directly read the current position of a specified ID | Common |
| `ttlsd.ReadSpeed(ID)` | Directly read the current speed of a specified ID | Common |
| `ttlsd.FeedBack(ID)` | Read multiple feedback values into the internal buffer | Common |
| `ttlsd.ReadPos(-1)` | Read position from the `FeedBack()` buffer | Common |
| `ttlsd.ReadSpeed(-1)` | Read speed from the `FeedBack()` buffer | Common |
| `ttlsd.ReadVoltage(ID)` | Read input voltage | Optional |
| `ttlsd.ReadTemper(ID)` | Read temperature | Optional |
| `ttlsd.CalibrationOfs(ID, position)` | Set the current position reference | Common |
| `ttlsd.syncReadBegin(...)` | Initialize synchronous reading | Common for multiple devices |
| `ttlsd.syncReadPacketTx(...)` | Send a synchronous read request | Common for multiple devices |
| `ttlsd.syncReadPacketRx(...)` | Receive the synchronous read response for a specified ID | Common for multiple devices |

!!! note "Motion control functions"
    Functions such as `WritePosEx()`, `WriteSpe()`, `SyncWritePosEx()`, and `SyncWriteSpe()` are mainly used for TTL Stepper Driver (A) motion control. TTL Encoder E02 is a feedback device and normally does not use these motion control functions.

### 12.7 C++ Workflow Summary

Read one encoder:

```text
1. Install the C++ / Arduino SDK.
2. Open FeedBack.ino.
3. Configure Serial1 according to your controller board.
4. Set the baud rate and device ID.
5. Upload the sketch.
6. Open the Serial Monitor.
7. Rotate the magnet and observe Position and Speed.
```

Read multiple encoders:

```text
1. Assign a unique ID to each encoder.
2. Connect all encoders to the same TTL bus.
3. Open SyncRead.ino.
4. Edit the ID[] array.
5. Upload the sketch.
6. Check the Serial Monitor output.
```

Set position reference:

```text
1. Move the mechanism to the target reference pose.
2. Open CalibrationOfs.ino.
3. Edit CalibrationOfs(ID, position).
4. Upload the sketch.
5. Read the position to verify the result.
```

### 12.8 C++ Troubleshooting

#### Q1: No output after uploading to ESP32S3

Check:

- `Serial.begin(115200);` is enabled.
- Serial Monitor baud rate is set to `115200`.
- The RX/TX pins in `Serial1.begin(1000000, SERIAL_8N1, 18, 17);` match your hardware.
- `ttlsd.pSerial = &Serial1;` is set.

#### Q2: Can I use software serial?

Not recommended.

TTL Encoder E02 uses 1 Mbps by default. Software serial is usually not stable enough at this speed. Use a hardware UART whenever possible.

#### Q3: Position reading always fails

Check:

- Device ID is correct.
- Baud rate is correct.
- Bus power is stable.
- RX/TX or the single-wire TTL conversion circuit is correct.
- There are no duplicate IDs on the same bus.

#### Q4: Why does `ReadPos(-1)` use `-1` as the ID?

`ReadPos(-1)` reads the value from the internal buffer updated by `FeedBack()`. It does not send a new read command on the bus.

`ReadPos(1)` sends a direct read command to the device with ID `1`.

---

## 13. Position, Speed, and Multi-Turn Data

### 13.1 Position Data

TTL Encoder E02 returns position in `steps`.

In 12-bit mode:

```text
1 turn = 4096 steps
0 ~ 4095 = 0° ~ 360°
```

Angle conversion:

```python
angle_deg = position / 4096.0 * 360.0
```

### 13.2 Speed Data

Speed unit:

```text
steps/s
```

Convert to degrees per second:

```python
speed_deg_s = speed_steps_s / 4096.0 * 360.0
```

### 13.3 Multi-Turn Reading

TTL Encoder E02 supports multi-turn reading. At the highest precision, the maximum position range is:

```text
0 ~ 65534
```

This corresponds to about 16 turns.

If lower precision is used, the readable turn count can increase.

!!! warning "Multi-turn count is not retained after power-off"
    After power-off, the encoder can still output the current single-turn absolute angle, but the accumulated multi-turn count is not retained. If your application depends on multi-turn position, rebuild the multi-turn reference in your host program or MCU after power-on.

---

## 14. Typical Workflows

### 14.1 Read One Encoder

Python SDK:

```text
1. Connect TTL Adapter (A).
2. Connect HC-1.25 8P Hub (A).
3. Connect TTL Encoder E02.
4. Apply DC 5~28V power.
5. Confirm the serial port name.
6. Set the port, baud rate, and ID in ttlsd_read.py.
7. Run ttlsd_read.py.
8. Rotate the magnet and observe position and speed changes.
```

C++ / Arduino SDK:

```text
1. Connect the MCU to TTL Encoder E02.
2. Open FeedBack.ino.
3. Configure UART, baud rate, and device ID.
4. Upload the sketch.
5. Open the Serial Monitor.
6. Rotate the magnet and observe Position and Speed.
```

### 14.2 Read Multiple Encoders Synchronously

Python SDK:

```text
1. Assign a unique ID to each encoder.
2. Connect all encoders to the same TTL bus.
3. Edit the ID range in sync_read.py.
4. Run sync_read.py.
5. Read position and speed from multiple encoders at the same time.
```

C++ / Arduino SDK:

```text
1. Assign a unique ID to each encoder.
2. Connect all encoders to the same TTL bus.
3. Open SyncRead.ino.
4. Edit the ID[] array.
5. Upload the sketch.
6. Check the position and speed of each device in the Serial Monitor.
```

### 14.3 Set Angle Reference

Python SDK:

```text
1. Move the mechanism to the target installation pose.
2. Edit the ID and target position value in ttlsd_ofscal.py.
3. Run ttlsd_ofscal.py.
4. Run ttlsd_read.py to verify the current position.
5. The calibration reference will be used automatically after the next power-on.
```

C++ / Arduino SDK:

```text
1. Move the mechanism to the target reference pose.
2. Open CalibrationOfs.ino.
3. Edit CalibrationOfs(ID, position).
4. Upload the sketch.
5. Read the position to confirm the result.
```

---

## 15. Troubleshooting

### Q1: No serial port is detected

Possible causes:

- CH343 / CH34X driver is not installed.
- The USB cable only supports charging and does not support data transfer.
- TTL Adapter (A) is not connected correctly.
- The system does not have permission to access the serial port.

Solutions:

- Use a USB cable that supports data transfer.
- Check whether a CH343 device appears in Windows Device Manager.
- Install the CH343 / CH34X driver if the device is not recognized on Linux or Raspberry Pi.
- On Linux, check whether the current user has serial port access permission.

---

### Q2: The serial port is visible, but the encoder cannot be read

Check:

- The encoder is connected to the HC-1.25-3P port correctly.
- The pin order is correct: `- / + / S`.
- TTL Adapter (A) has external power if needed.
- The supply voltage is within DC 5~28V.
- The port, baud rate, and ID in the code are correct.
- No duplicate IDs exist on the same bus.

!!! tip "Power supply recommendation"
    If only USB power is used, the voltage after TTL Adapter (A) may be too low for stable bus operation, especially when other devices are also connected. External DC 5~28V bus power is recommended.

---

### Q3: Communication error or unstable communication

Check:

- Duplicate IDs on the same bus.
- Baud rate mismatch.
- The target ID really exists on the bus.
- Wiring fault on one of the bus devices.
- Loose bus connector.
- Unstable bus power.

Only one device with a given ID can exist on the same TTL bus.

---

### Q4: Angle reading jumps or seems inaccurate

Check the mechanical installation first:

- The radial magnet is close to the center of the encoder IC.
- The gap between the magnet and the IC top surface is about 1mm.
- The gap is preferably not more than 1.5mm.
- The magnet rotates concentrically with minimal wobble.
- The magnet is firmly fixed.
- The encoder PCB is firmly fixed.

---

### Q5: Synchronous reading fails

Check:

- The IDs added in `sync_read.py` or `ID[]` really exist.
- All devices are connected.
- No duplicate IDs exist.
- Bus power is stable.
- Bus wiring is secure.

If only IDs `1`, `2`, and `3` are connected, but the program tries to read IDs `1` to `10`, the missing devices may cause timeout or read failure. Only include IDs that are actually connected.

---

### Q6: Why do some examples mention TTLSD or motor?

TTL Encoder E02 and TTL Stepper Driver (A) share part of the same SDK interface.

For TTL Encoder E02, you can think of the SDK as using only the feedback reading, synchronous reading, and reference calibration functions. Names such as `TTLSD` or `motor` in comments do not affect usage.

---

### Q7: Can TTL Encoder E02 share the bus with TTL servos?

Yes.

TTL Encoder E02 can share one TTL bus with Feetech STS / SMS / HLS bus servos, Lygion TTL Stepper Driver (A), and other Lygion TTL bus devices.

Requirements:

- IDs must be unique.
- Baud rates must match.
- Bus voltage must be compatible with all devices.
- Bus power must be stable when many devices are connected.

---

### Q8: Do I need to recalibrate after power-on?

Normally no.

The calibration result set by `reOfsCal()` or `CalibrationOfs()` is saved after power-off and remains valid after the next power-on.

However, accumulated multi-turn count is not saved. If your application relies on multi-turn position, rebuild the multi-turn reference in software after power-on.

---

## 16. Example Code

Python SDK:

```text
https://github.com/LygionOrganization/lygion_devs_py
```

Python examples:

```text
lyttlsd/ttlsd_read.py
lyttlsd/sync_read.py
lyttlsd/ttlsd_ofscal.py
```

C++ SDK:

```text
https://github.com/LygionOrganization/lygion_devs_cpp
```

C++ / Arduino examples:

```text
example/lyttlsd/FeedBack.ino
example/lyttlsd/SyncRead.ino
example/lyttlsd/CalibrationOfs.ino
```

---

## 17. Resources

### Feetech FD Debugging Software

- [Download FD software](../assets/files/FD.7z)

### SDK

[GitHub Python SDK](https://github.com/LygionOrganization/lygion_devs_py)

[GitHub C++ SDK](https://github.com/LygionOrganization/lygion_devs_cpp)

If GitHub is not accessible, download the SDKs from this site:

[Download Python SDK](assets/files/lygion_devs_py.zip)

[Download C++ SDK](assets/files/lygion_devs_cpp.zip)

### STEP Model

[TTL Encoder E02 STEP](assets/files/TTL-Encoder-E02.step)
