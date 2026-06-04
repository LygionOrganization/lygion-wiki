# Power Grouping and Power Isolation

This guide explains how to use Lygion hubs, including **TTL-5264 8P Hub (A)** and **HC-1.25 8P Hub (A)**, to organize wiring and power multiple groups of TTL bus devices.

When a robot contains several servos, joints, wheel motors, encoders, or driver boards, avoid routing every device through one long daisy chain. A more robust design shares the communication bus while dividing power according to voltage, load, and mechanical section.

## 1. When to Group Power

Use separate powered groups when any of the following applies:

- The system contains many TTL bus devices.
- Different products require different voltages, such as 12 V servos and 24 V stepper drivers.
- High-current devices cause voltage dips during startup, acceleration, or stall.
- A robot arm, legged robot, or mobile base needs cleaner cable routing.
- One load group should not disturb sensors or devices in another group.

!!! tip "Design rule"
    Devices can share the same TTL signal without sharing one positive supply rail. Group power by voltage, current demand, device type, or physical location.

## 2. What Power Isolation Means

![Hub power grouping](../../assets/images/g03.png){ .img-rounded }

A typical three-pin TTL bus connection carries:

```text
+   Positive supply
-   Supply return / GND
S   TTL bus signal
```

When all devices are daisy-chained through the same three conductors, both signal and power follow the same path. With long cables or high current, this can cause:

- Lower voltage at distant devices
- Voltage dips when motors start
- High-current actuators disturbing sensors or encoders
- One failed group affecting the entire bus
- Excessive cable or connector heating

Power isolation keeps the TTL signal shared while allowing each device group to receive power through a separate input or supply.

```text
Communication: one shared TTL bus
Power: separate supply paths for each load group
```

!!! warning "All groups must share GND"
    Every supply return and the controller GND must be connected. Without a common reference, the TTL signal may fail, produce errors, or damage hardware.

## 3. Lygion Hub Options

| Product | Interfaces | Typical use |
| --- | --- | --- |
| [TTL-5264 8P Hub (A)](../reference/bus-devices/hub-boards/ttl-5264-8p-hub-a.md) | 5264-3P, DC5521, KF301-2P, GH-1.25-3P | 5264-3P stepper drivers and bus servos, cascaded hubs, and mixed-voltage powered groups |
| [HC-1.25 8P Hub (A)](../reference/bus-devices/hub-boards/hc-1.25-8p-hub-a.md) | HC-1.25-3P, HX-5264-3P, GH-1.25-3P | Compact devices and lightweight wiring |

Both products fan out one TTL bus into multiple connectors. Choose the hub that matches the device connector and current requirements.

## 4. TTL-5264 8P Hub (A)

TTL-5264 8P Hub (A) distributes a TTL bus to eight 5264-3P connectors. It is suited to Lygion stepper drivers, compatible bus servos, and other devices using the same connector.

### Main Features

- Eight 5264-3P device connectors
- DC5521 and KF301-2P power inputs
- Board-to-board TTL communication connector for cascading hubs
- Separate supplies can power separate hub groups
- Power indicator
- Approximate size: `44 x 21 x 14 mm`

### Interfaces

| No. | Interface | Purpose |
| --- | --- | --- |
| 1 | KF301-2P terminal | Power input connected to the DC5521 input; use either input |
| 2 | Power indicator | Shows whether the hub is powered |
| 3 | Mounting holes | Four holes, approximately 3 mm diameter |
| 4 | DC5521 input | Accepts DC 5-25.2 V |
| 5 | Single-wire TTL interconnect | Carries the communication bus between hubs |
| 6 | Eight 5264-3P connectors | Connect TTL bus devices |

!!! note "A hub does not regulate voltage"
    The hub only distributes signals and power. It does not step voltage up or down. The applied voltage must be safe for every device in that powered group.

## 5. HC-1.25 8P Hub (A)

HC-1.25 8P Hub (A) distributes the TTL bus to eight compact HC-1.25-3P connectors. It is intended for small robots, dexterous hands, legged robots, and other space-constrained systems.

### Main Features

- Eight HC-1.25-3P device connectors
- HX-5264-3P connection for TTL Adapter (A) or a compatible controller
- GH-1.25-3P communication-only connection for cascading or power isolation
- Power indicator
- Approximate size: `39 x 21 mm`
- Four mounting holes, approximately 2.6 mm diameter

### Interfaces

| No. | Interface | Purpose |
| --- | --- | --- |
| 1 | HX-5264-3P | Communication and power connection to TTL Adapter (A) or a compatible controller |
| 2 | Eight HC-1.25-3P connectors | Connect compact TTL bus devices |
| 3 | Power indicator | Shows whether the hub is powered |
| 4 | GH-1.25-3P | Communication-only connection to an adapter or another hub |
| 5 | Mounting holes | Four holes, approximately 2.6 mm diameter |

!!! warning "GH-1.25-3P is for communication only"
    Do not use this connector as the power input for devices on the hub. Apply power through a connector or input explicitly designed to carry it.

## 6. Common Wiring Topologies

### One Powered Group

Use one group when all devices accept the same voltage and the total current is modest:

```text
Controller / TTL Adapter (A)
        |
        v
       Hub
        |
        +-- TTL device 1
        +-- TTL device 2
        +-- TTL device 3
        +-- TTL device 4
```

This is suitable for a few encoders, low-power devices, or an initial communication test.

### Different Voltages on One Communication Bus

Use separate powered hubs when device groups require different voltages:

```text
TTL Adapter (A)
        | TTL signal + GND
        |
        +-- Hub A, 12 V supply -- Device group A
        |
        +-- Hub B, 24 V supply -- Device group B
```

!!! warning "Do not mix voltage classes on one connected positive rail"
    If every `+` pin on a hub is connected, all devices on that hub must tolerate the same supply voltage.

### Shared Communication, Isolated Positive Supplies

Connect only the TTL signal and GND between separately powered hubs:

```text
Controller
   |
   v
Hub A <- Supply A
   +-- Device A1
   +-- Device A2

Hub B <- Supply B
   +-- Device B1
   +-- Device B2

Between Hub A and Hub B:
S connected
GND connected
+ not connected
```

This topology lets one group be powered down independently and reduces the effect of large load transients on other groups.

## 7. Recommended Examples

### Group 5264-3P Devices

```text
PC / MCU / TTL Adapter (A)
        |
        v
TTL-5264 8P Hub (A) <- group supply
        |
        +-- 5264-3P device 1
        +-- 5264-3P device 2
        +-- 5264-3P device 3
        +-- 5264-3P device 4
```

For a larger system, cascade communication to multiple hubs and power each group independently. Keep high-current devices in their own group, use a unique ID for every device, and confirm that signal and GND connect across all hubs.

### Fan Out HC-1.25-3P Devices

```text
TTL Adapter (A)
        |
        v
HC-1.25 8P Hub (A) <- group supply
        |
        +-- HC-1.25-3P device 1
        +-- HC-1.25-3P device 2
        +-- HC-1.25-3P device 3
        +-- HC-1.25-3P device 4
```

This arrangement is suited to compact encoders, small bus servos, dexterous hands, and lightweight mechanisms. Use the GH-1.25-3P connection when only the shared communication bus should continue to another group.

## 8. Before Applying Power

- Verify the allowed voltage of every connected device.
- Verify polarity and the `+ / - / S` pin order.
- Separate devices that require different voltages.
- Connect all supply returns and controller GND.
- Assign a unique ID to every device on the shared TTL bus.
- Confirm that supplies, wires, and connectors can carry the expected current.
- Clear the mechanism of cables, tools, and fragile objects before enabling actuators.

!!! danger "Avoid hot-plugging high-current actuators"
    Disconnect power before plugging or unplugging servos, motors, stepper drivers, and wheel modules. Hot-plugging can produce inrush current, arcing, or intermittent contacts that damage connectors and devices.

## 9. Frequently Asked Questions

### Can every device use one hub?

Yes, when all devices use the same voltage, the total current is modest, and cables are short. Split the system into multiple powered groups when device count or actuator current increases.

### Must separate supplies share GND?

Yes. The TTL signal needs one electrical reference shared by the controller and all device groups.

### Can I connect only the S signal?

No. Connect GND with S. A signal without a common ground reference is unreliable.

### Can IDs repeat on different hubs?

No. Hubs that share the TTL communication signal are one logical bus, so every device ID must be unique. See [Device IDs and baud rates](device-id-and-baudrate.md).

### Why isolate high-current devices?

Startup, sudden stops, stalls, and rapid acceleration can produce voltage dips and cable losses. Separating those loads reduces resets and communication errors in controllers, sensors, and encoders.

## Related Guides

- [Device IDs and baud rates](device-id-and-baudrate.md)
- [Power and wiring fundamentals](power-and-wiring-basics.md)
- [Communication troubleshooting](communication-troubleshooting.md)
- [FD device utility](fd-tool.md)
