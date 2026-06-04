# Power and Wiring Fundamentals

TTL bus devices require both communication and power. Many apparent communication failures are actually caused by insufficient power, incorrect wire order, or duplicate IDs.

## Three-Wire TTL Bus

A typical TTL bus connector carries:

```text
+   Positive supply
-   Supply return / GND
S   Single-wire TTL signal
```

Confirm the connector orientation and pin order. Do not rely on wire color alone.

## USB Is Not an Actuator Supply

TTL Adapter (A) uses USB primarily for communication. USB may power some low-current devices during configuration, but it is not recommended as the main supply for:

- Bus servos
- Stepper motor drivers
- Wheel-drive modules
- Robot joint actuators

Use an external supply that meets the product specification.

## Choose a Voltage Compatible with Every Device

When several products share one powered bus, the supply voltage must be safe for all of them. For example:

- An encoder may accept 5-28 V.
- A servo may require 9-12.6 V.
- A stepper driver and motor may use 12-25.2 V.

If all three share one supply, choose the common safe range, such as 9-12.6 V. Alternatively, use Lygion hubs to share communication while powering groups at different voltages:

- [TTL-5264 8P Hub (A)](../reference/bus-devices/hub-boards/ttl-5264-8p-hub-a.md)
- [HC-1.25 8P Hub (A)](../reference/bus-devices/hub-boards/hc-1.25-8p-hub-a.md)

[Power grouping and isolation](power-grouping-and-decoupling.md){ .md-button }

!!! warning "Never connect a low-voltage device directly to a high-voltage bus"
    A device rated for a maximum of 12.6 V must not be connected to a 24 V powered group.

## Group High-Current or Mixed-Voltage Devices

Use hubs or separate adapters to divide the power path by voltage, current demand, or mechanical section while keeping the TTL communication signal and GND common.

## Before Applying Power

- Confirm that the voltage is within every connected device's allowed range.
- Confirm that the supply has enough current capacity.
- Verify the `+ / - / S` pin order.
- Check for duplicate device IDs.
- Verify stepper motor phase wiring.
- Confirm limit switches are connected to the intended inputs.
