# TTL Adapter (A) Power and Wiring

The adapter supports USB communication, MCU UART communication, and the single-wire TTL bus. Wiring depends on how the adapter is used.

## Computer or SBC over USB

```text
PC / Raspberry Pi / Jetson / Mac
        | USB
        v
TTL Adapter (A)
        | TTL bus
        v
TTL bus device(s)
```

USB carries communication. Apply an external supply for actuator-class devices.

## External Supply

Apply external power through the DC5521 input:

| Item | Specification |
| --- | --- |
| Input voltage | DC 5-25.2 V |
| Input connector | DC5521 |

!!! warning "The supply voltage must be safe for every connected device"
    The adapter distributes the applied voltage to the bus. It does not regulate it for low-voltage devices.

## MCU UART Connection

| TTL Adapter (A) | MCU |
| --- | --- |
| TX | TX |
| RX | RX |
| GND | GND |

This straight-through connection differs from many conventional USB-to-UART modules because the adapter UART feeds its onboard single-wire TTL conversion circuit.

## Power Groups

Use multiple adapters or hubs when a system contains mixed voltages, several high-torque servos or stepper drivers, or long cable runs with significant voltage drop.

- [Power and wiring fundamentals](../../../tutorials/power-and-wiring-basics.md)
- [Power grouping and isolation](../../../tutorials/power-grouping-and-decoupling.md)
