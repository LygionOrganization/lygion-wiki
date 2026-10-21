# Power, connectors and onboard resources

## Package contents

RoboCore S3 is available in two kits. Kit 1 includes the board and basic accessories listed below. Kit 2 adds User Interface Module (A) and its connecting cable to everything in Kit 1.

### Kit 1

![Kit 1: board, antenna, USB data cable and power accessories](../../../../reference/bus-devices/robocore-s3/assets/kit-1.webp){ .img-rounded width="720" loading="lazy" }

| Item | Quantity | Purpose |
| --- | --- | --- |
| RoboCore S3 board | 1 | Robot control and device communication |
| DC5521 female socket with quick-connect terminals | 1 | Accepts DC5521 / DC5525 power plugs |
| XT30U female cable, 30 cm | 1 | Cable rated for 10A; connects to the included DC5521 socket without soldering |
| USB-A to USB-C data cable, 1 m | 1 | Firmware download and PC/host communication |
| 2.4GHz bulkhead antenna | 1 | Panel mounting lets you position the antenna outside a metal robot enclosure for wireless communication |

10A is the rating of the included XT30U cable; also respect the ratings of the supply, socket, connectors and connected devices.

### Kit 2

![Kit 2: all Kit 1 items plus the UI module and connecting cable](../../../../reference/bus-devices/robocore-s3/assets/kit-2.webp){ .img-rounded width="720" loading="lazy" }

Includes **everything in Kit 1**, plus:

| Item | Quantity | Purpose |
| --- | --- | --- |
| User Interface Module (A) | 1 | Includes a five-way switch, a 0.91-inch OLED display and a buzzer for local input, display and audible alerts |
| User Interface Module (A) connecting cable | 1 | Connects RoboCore S3 to User Interface Module (A) |

See [User Interface Module (A)](#user-interface-module-a) below for connection and usage details.

!!! warning "Connect the external antenna before wireless use"
    Attach the antenna before using Wi-Fi or ESP-NOW. Operating without it degrades wireless communication and may cause the ESP32-S3 module to heat up. For a metal enclosure, use the bulkhead mounting to place the antenna outside.

![Bulkhead antenna installation on a metal robot enclosure](../../../../reference/bus-devices/robocore-s3/assets/antenna-installation.webp){ .img-rounded width="720" loading="lazy" }

Installation example; the robot and enclosure are not included in either kit. The photo illustrates antenna placement, not an internal wiring diagram.

## Dimensions and mounting

![RoboCore S3 outline and mounting-hole dimensions in mm](../../../../reference/bus-devices/robocore-s3/assets/dimensions.webp){ .img-rounded width="720" loading="lazy" }

Dimensions are in mm. Use the four mounting holes and leave clearance for connectors, cables and the antenna.

| Item | Specification |
| --- | --- |
| Board size | 47 × 52 mm |
| Mounting holes | 4 |
| Hole diameter | 3 mm |
| Hole center spacing | 40 × 45 mm |
| Controller module | ESP32-S3-WROOM-1U-MCR8N8; 8 MB flash, 8 MB PSRAM |
| Development | Open-source examples for PlatformIO and Arduino IDE |

![RoboCore S3 rear side and four mounting holes](../../../../reference/bus-devices/robocore-s3/assets/board-back.webp){ .img-rounded width="600" loading="lazy" }

## Power

### Actuator supply and current

RoboCore S3 accepts **5–48V** through the XT30 power contacts of the CAN 2+2 connector, the 5264-3P TTL connector, or the XH2.54-4P device RS485 connector. Select the voltage for the connected devices first, then check the combined current demand.

| Connector | Voltage / purpose | Continuous current limit |
| --- | --- | --- |
| XT30 power contacts | Input for the board and bus devices, 5–48V | 10A input |
| 5264-3P TTL | Supports power input; actuator voltage follows the system supply | 6A output |
| XH2.54-4P device RS485 | Supports power input; actuator voltage follows the system supply | 6A output |
| GH1.25-3P | Board-to-board TTL communication and common ground for power decoupling | No actuator power supply |

The TTL and device RS485 connectors **do not convert voltage for individual devices**. For example, a 24V XT30 input produces 24V actuator outputs. When powered through XT30, both outputs and the board share its 10A input limit; they cannot both supply 6A simultaneously. Also respect the ratings of the supply, cables and adapter sockets.

!!! warning "Match the supply to every powered device"
    A 48V-rated board does not make low-voltage servos compatible with 48V. Wire with power off and check polarity, pin labels and device ratings. Include motor startup and stall current in the power budget.

For independently powered device groups, use GH1.25-3P with a bus hub to decouple communication from actuator power. See [Power grouping and decoupling](../../../tutorials/power-grouping-and-decoupling.md).

### Flexible power connections { #flexible-power }

![A hub powers RoboCore S3 and carries TTL communication through one 5264-3P cable](../../../../reference/bus-devices/robocore-s3/assets/simple_power.webp){ .img-rounded width="720" loading="lazy" }

Connect the supply to a compatible bus hub, then link the hub to RoboCore S3 with **one 5264-3P cable** for both board power and TTL communication. The hub supplies the actuators directly, so their high current does not pass through RoboCore S3. This suits higher-power systems and reduces wiring around the controller. The XH2.54-4P device RS485 connector also accepts power input; choose the connection for your device bus.

- Stay within the board's **5–48V** input range and the rated voltage of the hub and every device sharing the supply.
- Respect supply, hub, connector and cable current ratings. The 6A values above are bus-port output limits, not a rating for every wiring arrangement.
- The XT30, 5264-3P and XH2.54-4P actuator power contacts share a supply rail. Do not directly parallel independent supplies.

This differs from **GH1.25-3P power grouping**: 5264-3P carries both power and communication, while GH1.25-3P carries only TTL communication and common ground, with the board and actuator groups powered separately. The hub, drivers, motors and external supply are sold separately.

### Connecting USB and XT30 together

USB and XT30 can be connected simultaneously. USB provides board communication, firmware download or board power; XT30 supplies actuator power. Board power does not backfeed into the computer through USB. **USB alone does not power the actuator connectors.**

The two Type-C ports share VBUS inside the board; they are not isolated power inputs. Do not use two independent USB supplies as a parallel power arrangement.

Board-only consumption is below 0.2W at standby and below 0.7W when running the Wi-Fi Web application. These figures exclude external devices and do not describe instantaneous peak consumption.

### Auxiliary 5V and 3.3V

These outputs serve low-power peripherals and are separate from the TTL / RS485 actuator outputs.

| Output | Source | Usage limits |
| --- | --- | --- |
| GH1.25-5P 5V | SCT2A27 integrated LDO | 200mA-class supply; keep load at or below 200mA. Loaded voltage depends on LDO headroom |
| Expansion 3.3V | AMS1117-3.3S supplied by 5V0 | 1A-class total output shared by the board and peripherals; available peripheral current is also thermally limited |

**A 1A connector and PCB trace rating does not mean 1A is available to peripherals.** Reserve 3.3V current for the ESP32-S3, IMU, transceivers and other onboard loads. Use a separate regulator for larger loads, with a common ground as required by the communication interface. RoboCore S3 does not power a Raspberry Pi.

Treat auxiliary 5V and 3.3V as outputs. Do not apply actuator supply voltage to them or directly parallel them with another device's power output.

??? info "Circuit details: 5V0 and 5V are different nets"
    U15 SCT2A27 generates **5V0** through its switching output and inductor L2. Its DC-DC supports 2A continuous output, but this is not the external auxiliary 5V connector rating.

    - **Auxiliary 5V:** 5V0 feeds U15 VBIAS. The integrated 200mA LDO supplies GH1.25-5P through the LDO pin. Its input is already approximately 5V, leaving insufficient regulation headroom. Do not assume an exact 5V output at 200mA; check the peripheral's acceptable supply range.
    - **3.3V:** U13 AMS1117-3.3S regulates 5V0 down to 3.3V. Dissipation is approximately `(5 − 3.3) × total output current`: 0.85W at 0.5A or 1.7W at 1A. Sustained capacity depends on board load, ambient temperature and cooling. Subtracting average board consumption from 1A does not establish a peripheral peak-current budget.

    See the [SCT2A27 manufacturer datasheet](https://www.silicontent.com/uploads/20250604/3729c2375b93fd8db1c210f6d7f306ab.pdf). Chip ratings and current available to external peripherals are different quantities.

### Protection scope

| Circuit | Protection and limits |
| --- | --- |
| Board DC-DC branch | Current limiting, undervoltage, output overvoltage and thermal protection; these do not imply actuator-output protection |
| USB | ESD protection on data lines; the power path blocks board power from feeding back into the computer |
| CAN and device RS485 | Resettable fuses and transient clamps on signal lines |
| External RS485 (GH1.25-5P) | Resettable fuses on signal lines |
| Single-wire TTL | Resettable fuse and clamps on the signal line |

The actuator power path has no overall reverse-polarity cutoff or overcurrent disconnect. Signal protection does not replace power protection; provide an external fuse or current-limited supply as required by the system. RESET and software stop commands do not disconnect actuator power.

## Connectors and resources

Board front, with both Type-C ports facing down. Numbers match the table below. Open the image to inspect the connector labels. The IMU is listed separately without a front-view number.

![RoboCore S3 onboard resources, with 13 numbers matching the table](../../../../reference/bus-devices/robocore-s3/assets/board-resources.svg){ .img-rounded width="720" loading="lazy" }

[Open the full-size numbered diagram](../../../../reference/bus-devices/robocore-s3/assets/board-resources.svg)

| No. | Resource | Signals | Use |
| --- | --- | --- | --- |
| 01 | ESP32-S3 controller | ESP32-S3-WROOM-1U-MCR8N8 | 8 MB flash / 8 MB PSRAM; control firmware and wireless communication |
| 02 | IPEX1 antenna connector | External 2.4 GHz antenna | Connect the antenna before Wi-Fi or ESP-NOW use |
| 03 | PH1.25-10P expansion | IO6 SDA, IO7 SCL, IO2, IO9, IO10, IO11, IO12, IO21, 3.3V, GND | Lygion User Interface Module (A) |
| 04 | CAN 2+2 | CAN H/L and XT30 power contacts | Board power input; CAN communication on RX13/TX14 in CAN position |
| 05 | CAN/RS485 selector | IO13 RX / IO14 TX | Select the external communication circuit |
| 06 | GH1.25-5P | RS485 A/B, GND, 5V output | External RS485 on RX13/TX14 in 485 position |
| 07 | 5264-3P | IO4 TX / IO5 RX via single-wire TTL circuit | TTL bus devices; supports power input; power follows the system supply |
| 08 | XH2.54-4P | IO4 TX / IO5 RX via RS485 circuit | RS485 bus devices; supports power input; power follows the system supply |
| 09 | GH1.25-3P | Single-wire TTL | Board-to-board TTL communication and power decoupling |
| 10 | Type-C USB | IO19 USB D−, IO20 USB D+ | Native ESP32-S3 USB, including host USB CDC communication |
| 11 | Type-C UART | TXD0 / RXD0 via USB-to-UART | Firmware download and debugging, with automatic download circuit |
| 12 | BOOT button | IO0, active low | Enter download mode together with RESET |
| 13 | RESET button | EN, active low | Holds the MCU in reset while pressed; restarts on release, without disconnecting board power |
| — | QMI8658A six-axis onboard IMU | IO6 SDA / IO7 SCL | Three-axis acceleration and angular velocity; shares I²C with external OLED |

## CAN/RS485 selector

!!! warning "External communication and the device bus use different GPIO pairs"
    **CAN position: IO13 RX / IO14 TX communicate over the CAN 2+2 connector.**
    **485 position: the same IO13 RX / IO14 TX communicate over GH1.25-5P RS485.**
    These two external interfaces cannot use this GPIO pair simultaneously. The switch selects the physical circuit; firmware must also use the corresponding CAN or UART protocol. Stop communication before switching.

External RS485 on IO13/IO14 is independent of bus-device RS485 on IO4/IO5. **Bus-device RS485 and single-wire TTL share IO4 TX / IO5 RX**, including the UART data and baud rate. They are not independent serial ports; avoid duplicate IDs and reply collisions when both are connected. The CAN/RS485 selector does not affect this device-bus GPIO pair.

The CAN example uses 500 kbps and needs a matching peer and common ground. The board has a 120Ω CAN termination resistor; account for existing termination across the entire network. The external RS485 example uses 115200 8N1 and automatic hardware direction control. Coordinate half-duplex access between peers. See [Arduino examples](arduino.md). Switching to 485 does not automatically create a factory JSON gateway.

## User Interface Module (A)

![Connected external UI module with OLED, five-way switch and buzzer](../../../../reference/bus-devices/robocore-s3/assets/ui-module-connected.webp){ .img-rounded width="720" loading="lazy" }

Kit 2 includes this module and its connecting cable. Connect it to PH1.25-10P for a five-way switch, a 0.91-inch OLED display and buzzer alerts. These components are on the external module.

| Function | GPIO / settings |
| --- | --- |
| Up / Down / Left / Right / OK | IO10 / IO11 / IO12 / IO9 / IO2, active low |
| Buzzer | IO21 |
| OLED | SDA6 / SCL7, SSD1306 128×32, address 0x3C |
| Onboard IMU | Same I²C bus; driver probes 0x6A / 0x6B |

The `User_Interface_Module_A` sketch debounces keys, beeps briefly and displays the pressed key. Buttons remain available if the OLED is missing. Initialize Wire once and keep its pins consistent across OLED and onboard IMU drivers.

## Download and USB communication

- **Type-C UART:** the automatic download circuit uses DTR/RTS from the tool; normally no manual BOOT sequence is needed.
- **Type-C USB:** to enter download mode manually, hold BOOT, press and release RESET, then release BOOT and select the enumerated USB port.
- **Normal operation:** native USB CDC exchanges JSON with a host and avoids the UART bridge bottleneck. Actual throughput depends on firmware and host processing; it is not an actuator execution rate.

Use a data-capable cable, identify the actual port and close competing serial monitors. See [firmware recovery](firmware.md).
