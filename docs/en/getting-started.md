# Getting Started

This guide introduces the basic workflow for using Lygion TTL bus devices, including wiring, power supply, device ID configuration, parameter setup with FD software, Python SDK usage, and C++ / Arduino SDK usage.

Before using Lygion TTL encoders, TTL stepper drivers, node modules, bus servos, or robot modules based on the TTL bus, we recommend reading this guide first. It will help you understand the basic concepts of bus communication, device power supply, and ID configuration.

!!! note "Scope"
    This guide mainly applies to **Lygion TTL bus devices**.

    Lygion TTL bus devices can be used on the same TTL bus together with Feetech STS / HLS series TTL bus servos. However, each device on the bus must have a unique ID.

---

## 1. Basic Concepts

Multiple TTL bus devices can be connected to the same bus. The controller communicates with each device by using its device ID.

For example, if several modules are connected to one TTL bus, the controller sends commands to a specific ID, and only the device with that ID should respond.

!!! warning "Do not connect multiple new devices at the same time"
    Many bus devices may have the same factory default ID, for example `1`.

    If multiple devices with the same ID are connected to the same bus, communication conflicts may occur. This can cause search errors, abnormal feedback, failed control commands, or no response from the devices.

    When setting up new devices, connect and configure them one by one. Assign a unique ID to each device before connecting them together on the same bus.

---

## 2. Wiring

Lygion TTL bus devices can be controlled by a PC / SBC, or by an embedded controller such as ESP32 or STM32.

### 2.1 Control from a PC / SBC via USB

If you are using a PC, Raspberry Pi, Jetson, RK board, or other single-board computer, we recommend using [TTL Adapter (A)](bus-devices/ttl-adapter-a.md) to connect to Lygion TTL bus devices.

TTL Adapter (A) includes a USB-to-TTL bus interface. After connecting it to the computer, the system will recognize it as a serial port. You can then communicate with the bus devices using FD software, the Python SDK, or other serial tools.

![TTL Adapter USB Connection](assets/images/g01.png){ .img-rounded width="720" }

Typical connection:

```text
PC / SBC - USB Port
        │
        │ USB Cable
        │
TTL Adapter (A)
        │
        │ TTL Bus
        │
TTL Bus Device(s)
```

The USB cable is mainly used for communication. It should not be treated as the main power source for bus devices.

Some low-power devices or a single device may allow basic operations such as reading parameters or changing the ID through USB only. However, USB power is not recommended for driving motors, servos, or other actuators. Actuator devices require an external power supply that matches their voltage and current requirements.

!!! warning "USB power is not enough for actuator operation"
    When TTL Adapter (A) is connected only through USB, the voltage and current provided by the USB port are usually not enough for bus servos, stepper motor drivers, or other actuator devices.

    If you need to move a motor, servo, or actuator, always connect a proper external power supply.

### 2.2 Control from an MCU UART

If you are using ESP32, STM32, or another embedded controller, you can connect the MCU UART to [TTL Adapter (A)](bus-devices/ttl-adapter-a.md).

The TTL Adapter (A) converts the MCU’s **dual-wire UART** signals into a **single-wire TTL bus signal**, allowing control of Lygion TTL bus devices or compatible TTL bus servos.

Typical connection:

![TTL Adapter UART Connection](assets/images/g02.png){ .img-rounded }

| TTL Adapter (A) | MCU |
| --- | --- |
| RX | RX |
| TX | TX |
| GND | GND |

The UART interface of TTL Adapter (A) uses **3.3V TTL logic level**.

!!! warning "Check the UART logic level"
    The UART interface of TTL Adapter (A) is 3.3V.

    If your MCU uses 5V UART logic, make sure its IO pins are compatible with 3.3V input. If necessary, add a level shifting circuit.

!!! tip "MCU-to-TTL Adapter wiring"
    - Connect MCU RX → TTL Adapter (A) RX
    
    - Connect MCU TX → TTL Adapter (A) TX
    
    - Connect MCU GND → TTL Adapter (A) GND

---

## 3. Power Supply

TTL bus devices require a suitable power supply according to the device type and actual load.

When selecting a power supply, consider the following:

- Whether the voltage matches the device specification
- Whether the current rating is sufficient for peak load
- How many devices share the same power supply
- Whether the devices include motors, servos, drivers, or other high-current loads
- Whether the application may involve stall, acceleration, heavy load startup, or other high-current conditions

![TTL Bus Power Supply](assets/images/g03.png){ .img-rounded }

For example, if several stepper motor drivers or high-torque servos are connected to the same bus, the external power supply must provide enough current margin for all connected devices.

!!! tip "Leave enough current margin"
    Motors, servos, and drivers may draw much higher current during startup, acceleration, stall, or sudden load changes.

    Do not choose the power supply only based on average current. Always leave enough current margin based on the actual load and the number of devices.

---

## 4. Grouped Power Supply and Communication Decoupling

The Lygion TTL bus system supports grouped power supply. This means that the communication bus and the device power supply can be separated.

This is useful in the following situations:

- Many devices are connected to the same bus
- Different devices require different operating voltages
- Servos, stepper drivers, or other high-current devices need independent power supplies
- You want to keep all devices on one communication bus while managing power in separate groups
- You want to reduce the current load on a single power path

TTL Adapter (A) provides GH1.25-3P communication ports on both sides. These ports are mainly used for TTL bus communication expansion and are not intended for high-current power distribution.

You can connect TTL Adapter (A) to the following hub boards:

- [TTL-5264 8P Hub (A)](bus-devices/ttl-5264-8p-hub-a.md)
- [HC-1.25 8P Hub (A)](bus-devices/hc-1.25-8p-hub-a.md)

### 4.1 Choosing the Right Hub

| Hub Type | Suitable Devices | Description |
| --- | --- | --- |
| TTL-5264 8P Hub (A) | Stepper drivers, bus servos, high-current modules | Better suited for devices with higher current requirements |
| HC-1.25 8P Hub (A) | Encoders, small node modules, low-power devices | Compact connector, suitable for signal-level and low-power devices |

Examples:

- If you need to connect multiple TTL stepper motor drivers, use TTL-5264 8P Hub (A).
- If you need to connect multiple TTL encoders, such as for a dexterous hand or multi-joint feedback system, use HC-1.25 8P Hub (A).

### 4.2 Basic Rule for Grouped Power Supply

A typical TTL bus includes:

| V+ | GND | S |
| --- | --- | --- |
| Power positive | Power ground | Signal bus |

If multiple power supplies are used, the V+ lines between different power groups can be separated, but GND and S must remain connected.

Between different power groups:

| V+ | GND | S |
| --- | --- | --- |
| Not connected | Must be connected | Must be connected |

This keeps all devices on the same communication bus while allowing different device groups to use separate power supplies.

!!! warning "All power groups must share ground"
    If different power groups do not share GND, the communication signal will not have a common reference level. This may cause unstable communication or complete communication failure.

    In most grouped power supply setups, keep GND connected and only separate V+ between power groups.

### 4.3 Mixing Devices with Different Voltages

By separating power from communication, devices with different operating voltages can be used on the same TTL bus.

For example, one TTL bus may include:

- A group of 12V bus servos
- A group of 24V stepper motor drivers
- A group of low-power TTL encoders

These devices can share the same S signal line and common GND, while each group uses its own V+ power input.

!!! note "Simple explanation"
    You can think of the TTL bus as one shared data line.

    As long as the signal line and ground are connected correctly, different devices can be powered by different power supplies.

    This allows unified control while avoiding excessive current through a single power path.

---

## 5. Before Control: Set Unique Device IDs

Before controlling multiple bus devices, each device must have a unique ID.

Recommended workflow:

1. Connect only one device to be configured.
2. Use FD software, the Python SDK, or the C++ SDK to search for the device.
3. Change the device ID.
4. Record the device model, installation position, and assigned ID.
5. Disconnect the current device.
6. Connect the next device.
7. Repeat the process until all device IDs are configured.
8. Connect all devices to the same bus for unified control.

Recommended ID record table:

| Device Name | Position | ID | Notes |
| --- | --- | --- | --- |
| TTL Stepper Driver (A) | Left wheel drive | 1 | Velocity mode |
| TTL Stepper Driver (A) | Right wheel drive | 2 | Velocity mode |
| TTL Encoder E02 | Joint 1 | 11 | Absolute angle feedback |
| TTL Node (A) | End module | 21 | RGB / S.BUS |

!!! warning "Avoid ID conflicts"
    Two devices on the same bus must not use the same ID.

    If two devices share the same ID, they may respond to the same command at the same time, causing communication errors or abnormal control behavior.

### 5.1 Main ID and Secondary ID

Some devices support a secondary ID or sync ID for synchronized response.

When setting a secondary ID, it is also recommended to keep only the device being configured on the bus. If multiple devices are connected and some of them already have a secondary ID, more than one device may respond to the same command. This can cause unexpected parameter writing or control results.

!!! note "Configure key parameters one device at a time"
    When changing key parameters such as ID, secondary ID, baud rate, operating mode, or limit settings, connect only one device to the bus.

    After all parameters are configured, multiple devices can then be connected together for system-level control.

---

## 6. Parameter Setup with FD Software

Windows users can use FD software to search devices, check status, modify parameters, and perform basic control.

Download:

- [Download FD Software](assets/files/FD.7z)

### 6.1 Connect the Device

Before using FD software, complete the following steps:

1. Connect TTL Adapter (A) to the computer with a USB cable.
2. Connect TTL Adapter (A) to the TTL bus device to be configured.
3. Connect an external power supply according to the device requirements.
4. Make sure the device is powered on correctly.

### 6.2 Check the Serial Port

After connecting TTL Adapter (A), Windows should recognize a new COM port.

To check the port number:

1. Right-click the Windows Start menu.
2. Open Device Manager.
3. Expand **Ports (COM)**.
4. Look for a device name similar to:

```text
USB-Enhanced-SERIAL CH343 (COMX)
```

`COMX` is the COM port number assigned by Windows, such as COM3, COM5, or COM12.

### 6.3 Open FD Software

After opening FD software:

1. Select the COM port detected above.
2. Set the baud rate. Most bus devices use `1000000`. Some `SCS` servo models use `500000`.
3. Click **Open**.
4. Click **Search**.
5. Wait for the device to appear in the device list on the left.
6. After the device appears, click **Stop**.
7. Select the target device from the device list.

!!! note "Why click Stop after searching?"
    During search, FD software continuously sends query commands to the bus.

    After the device is found, click **Stop**. Otherwise, continuous searching may affect later debugging or control operations.

### 6.4 Search for Devices

FD software searches bus devices starting from lower IDs.

If the device ID is small, such as the factory default ID `1`, it usually appears quickly. If the device was previously set to a larger ID, the search may take longer.

The maximum number of devices supported on the same TTL bus depends on the protocol, power supply, cable length, and communication stability.

### 6.5 Change the Device ID

After the device is found, you can change its ID in FD software.

Steps:

1. Click the target device in the device list on the left.
2. Go to the **Programming** page.
3. Find the `ID` parameter.
4. Click the value field of the ID parameter.
5. Enter the new ID in the lower-right input area.
6. Click **Save**.
7. Click **Search** again.
8. Select the device with the new ID from the device list.

The valid ID range is usually:

```text
1 ~ 252
```

!!! warning "Select the new ID after changing it"
    After the ID is changed, the old ID is no longer valid.

    Search again and select the new ID before reading status or sending control commands.

### 6.6 Configure the Next Device

When setting IDs for multiple devices:

1. Keep FD software open.
2. Disconnect the current device.
3. Connect the next device to be configured.
4. Click **Search**.
5. Select the device.
6. Change its ID.
7. Save and record the new ID.

Configure devices one by one to avoid communication conflicts caused by duplicate factory default IDs.

!!! warning "Do not change unknown parameters"
    The **Programming** page in FD software contains internal device parameters.

    Do not change a parameter unless you understand its function. Incorrect settings may cause the device to stop working normally, move in the wrong direction, ignore limits, or fail to communicate.

---

## 7. Parameter Setup with the Python SDK

For PC, Raspberry Pi, Jetson, RK boards, or other devices that can run Python, you can use the Lygion Python SDK to configure parameters and control devices.

Supported platforms include:

- Windows
- Linux
- macOS
- Raspberry Pi
- Jetson
- RK series single-board computers

The Python SDK mainly depends on the serial communication library `pyserial`.

### 7.1 Download the SDK

[GitHub Python SDK](https://github.com/LygionOrganization/lygion_devs_py)

If GitHub is not accessible, you can also download the SDK from this site:

[Local Python SDK Download](assets/files/lygion_devs_py.zip)

### 7.2 Install Python

Windows users need to install [Python](https://www.python.org/downloads/windows/) first.

Python 3.10 or later is recommended. During installation, make sure to enable:

```text
Add Python to PATH
```

After installation, check the version in a terminal:

```bash
python --version
pip --version
```

Linux / macOS usually includes Python by default. You can check with:

```bash
python3 --version
pip3 --version
```

### 7.3 Create a Virtual Environment

Go to the SDK directory, then create and activate a Python virtual environment.

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 7.4 Install Dependencies

Install the serial communication dependency:

```bash
pip install pyserial
```

### 7.5 Confirm the Serial Port Name

Serial port names are different on different operating systems.

| System | Common Serial Port Name |
| --- | --- |
| Windows | COM3, COM5, COM12 |
| Linux | /dev/ttyUSB0, /dev/ttyACM0 |
| macOS | /dev/tty.usbserial-*, /dev/tty.usbmodem-* |
| Raspberry Pi GPIO UART | /dev/serial0 or /dev/ttyAMA0 |

Windows users can check the COM port in Device Manager.

Linux users can run the following commands before and after connecting the USB device:

```bash
ls /dev/ttyUSB*
ls /dev/ttyACM*
```

For Raspberry Pi, Jetson, or RK boards using onboard UART, make sure UART is enabled in the system and check the correct port name and permissions.

!!! note "Linux serial port permission"
    If the serial port cannot be opened on Linux, the current user may not have permission to access it.

    You can add the user to the `dialout` group, or temporarily run the program with `sudo`.

### 7.6 Set Device ID with Broadcast ID

Taking TTL Stepper Driver (A) as an example, you can refer to the parameter configuration example in the SDK:

[lygion_devs_py/lyttlsd/ttlsd_eprom.py](https://github.com/LygionOrganization/lygion_devs_py/blob/main/lyttlsd/ttlsd_eprom.py)

In some cases, you may not know the current ID of a device. You can use broadcast `ID 254` to send a setting command to the device currently connected to the bus.

Example:

```python
scs_comm_result, scs_error = packetHandler.SetID(254, 1)

if scs_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(scs_comm_result))
elif scs_error != 0:
    print("%s" % packetHandler.getRxPacketError(scs_error))
```

This example sets the responding device ID to `1`.

!!! danger "Connect only one device when using broadcast ID"
    Broadcast ID `254` may affect all devices on the current bus that support broadcast commands.

    If multiple devices are connected, using broadcast ID to change the ID may set all of them to the same ID, causing communication conflicts.

    Before using broadcast ID to modify parameters, make sure only one device is connected to the bus.

### 7.7 Modify Serial Port and Baud Rate

Before running a Python example, update the following values according to your setup:

- Serial port name
- Baud rate
- Target device ID
- Parameters to be written

Example for Windows:

```python
DEVICENAME = "COM5"
BAUDRATE = 1000000
```

Example for Linux:

```python
DEVICENAME = "/dev/ttyUSB0"
BAUDRATE = 1000000
```

Default baud rates may vary by product. Always refer to the corresponding product documentation.

---

## 8. Parameter Setup with the C++ / Arduino SDK

For ESP32, STM32, Arduino, and other embedded platforms, you can use the Lygion C++ SDK or Arduino examples.

[GitHub C++ SDK](https://github.com/LygionOrganization/lygion_devs_cpp)

If GitHub is not accessible, you can also download the SDK from this site:

[Local C++ SDK Download](assets/files/lygion_devs_cpp.zip)

### 8.1 Supported Development Environments

The C++ / Arduino SDK is suitable for:

- Arduino IDE
- PlatformIO
- ESP32 Arduino Core
- Other embedded platforms with Arduino-style serial communication

### 8.2 Install the SDK

For Arduino IDE, place the SDK library folder into the Arduino `libraries` directory.

Common paths:

Windows:

```text
Documents/Arduino/libraries/
```

macOS:

```text
~/Documents/Arduino/libraries/
```

For PlatformIO, place the SDK folder into the project `lib` directory:

```text
your_project/
├─ src/
├─ lib/
│  └─ lygion_devs_cpp/
└─ platformio.ini
```

### 8.3 Reference Example

Taking TTL Stepper Driver (A) as an example, refer to:

[lyttlsd/ProgramEprom/ProgramEprom.ino](https://github.com/LygionOrganization/lygion_devs_cpp/blob/main/example/lyttlsd/ProgramEprom/ProgramEprom.ino)

This example shows how to modify device parameters using C++ / Arduino code, such as changing a device from ID `1` to ID `2`.

You can also use broadcast ID `254` for parameter configuration, but only when a single target device is connected to the bus.

!!! danger "Use broadcast ID carefully in embedded programs"
    Whether you use the Python SDK or the C++ SDK, broadcast ID affects all supported devices on the current bus.

    When using broadcast ID to modify key parameters such as ID or baud rate, make sure only one target device is connected.

### 8.4 ESP32-S3 UART Initialization

ESP32-S3 usually provides multiple hardware serial ports, such as:

- Serial
- Serial1
- Serial2

If you use custom UART pins, specify the RX and TX pins when initializing the serial port.

Example:

```cpp
Serial1.begin(1000000, SERIAL_8N1, 18, 17);
```

Parameter meaning:

| Parameter | Description |
| --- | --- |
| 1000000 | Baud rate |
| SERIAL_8N1 | 8 data bits, no parity, 1 stop bit |
| 18 | RX pin |
| 17 | TX pin |

Do not rely only on:

```cpp
Serial1.begin(1000000);
```

If only the baud rate is specified, the board uses its default UART pins. These default pins may not be connected to TTL Adapter (A), which can make the program appear to run normally while the device does not respond.

!!! tip "MCU-to-TTL Adapter wiring"
    - Connect MCU RX → TTL Adapter (A) RX
    
    - Connect MCU TX → TTL Adapter (A) TX
    
    - Connect MCU GND → TTL Adapter (A) GND

---

## 9. Troubleshooting

### 9.1 FD Software Cannot Find the Device

Check the following:

- TTL Adapter (A) is correctly connected to the computer
- A COM port appears in Device Manager
- The correct COM port is selected in FD software
- The baud rate is correct
- The bus device is powered
- TX / RX / GND wiring is correct
- No duplicate IDs exist on the bus
- The cable is not too long or poorly connected

### 9.2 The Device Is Found but Does Not Move Correctly

Possible causes:

- Only USB is connected, but no external device power is supplied
- Power supply voltage does not match the device requirement
- Power supply current is insufficient
- Motor or servo load is too high
- Device is in the wrong operating mode
- Speed, acceleration, torque, or related parameters are not configured correctly

### 9.3 The Device Disappears After Changing ID

After changing the ID, the old ID becomes invalid.

Search again, find the new ID, and select it before reading status or sending control commands.

### 9.4 Communication Becomes Unstable After Connecting Multiple Devices

Check the following:

- Duplicate device IDs
- Insufficient power supply current
- Whether all power groups share GND
- Communication cable length
- Poor contact in the hub or cables
- Whether one device uses a different baud rate from the others

---

## 10. Recommended First-Time Setup Workflow

If this is your first time using Lygion TTL bus devices, follow this workflow:

1. Read the voltage, current, and interface specifications of the product.
2. Connect only one device before parameter configuration is complete.
3. Connect TTL Adapter (A) to the computer.
4. Connect the required external power supply.
5. Use FD software to search for the device.
6. Change the device ID.
7. Record the device ID and installation position.
8. Use FD software or the SDK to test basic control.
9. Repeat the process for other devices.
10. After all IDs are configured, connect all devices to the same bus for system-level testing.

---

## 11. Summary

After completing this guide, you should understand:

- How to connect TTL bus devices through USB or MCU UART
- Why bus devices need an external power supply
- How to use hubs for bus expansion and grouped power supply
- Why each device needs a unique ID before multiple devices are connected
- How to change device IDs using FD software
- How to configure basic parameters with the Python SDK and C++ SDK
- How to troubleshoot common communication and power issues

Product-specific documents will focus on the features, parameters, and control methods of each product. The basic wiring and ID configuration workflow will not be repeated in every product document.
