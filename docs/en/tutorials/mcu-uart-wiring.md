# MCU UART Wiring

This guide explains the basic wiring required to control Lygion TTL bus devices from an MCU with the C++ / Arduino SDK.

## Connection Options

### MCU with TTL Adapter (A)

```text
MCU hardware UART
   | RX / TX / GND
   v
TTL Adapter (A)
   | Single-wire TTL bus
   v
TTL bus device
```

This is the easiest option for prototypes and first tests.

### MCU with a Custom Single-Wire TTL Circuit

```text
MCU hardware UART
   |
   v
UART-to-single-wire TTL circuit
   |
   v
TTL bus device
```

Use this option for a custom controller board or production design.

## Wire an MCU to TTL Adapter (A)

| MCU UART | TTL Adapter (A) |
| --- | --- |
| RX | RX |
| TX | TX |
| GND | GND |

!!! note "This differs from a conventional USB-to-UART adapter"
    The adapter's UART pins connect to its onboard single-wire conversion circuit. An external MCU therefore normally uses `RX to RX` and `TX to TX`. Confirm the circuit before applying this rule to another adapter.

## Logic Level

The TTL Adapter (A) UART uses:

```text
3.3 V TTL logic
```

| Controller | Typical compatibility |
| --- | --- |
| ESP32 / ESP32S3 | Compatible 3.3 V logic |
| 3.3 V STM32 board | Usually compatible |
| Arduino Mega2560 | 5 V I/O; verify input tolerance |
| Custom 5 V MCU | Use a level shifter unless confirmed compatible |

!!! warning "Do not drive a non-tolerant 3.3 V input with a 5 V UART"
    An incompatible signal voltage can damage the hardware.

## Configure the Hardware UART

### ESP32S3

```cpp
Serial.begin(115200);
Serial1.begin(1000000, SERIAL_8N1, 18, 17);
ttlsd.pSerial = &Serial1;
```

| Value | Purpose |
| --- | --- |
| `115200` | USB debug serial rate |
| `1000000` | Default TTL bus rate |
| `18` | ESP32S3 RX pin |
| `17` | ESP32S3 TX pin |

### Arduino Mega2560

```cpp
Serial.begin(115200);
Serial1.begin(1000000);
ttlsd.pSerial = &Serial1;
```

`Serial1` normally uses `RX1 = 19` and `TX1 = 18`.

## TTL Bus Wiring

A typical three-wire bus connector carries:

```text
+   Positive supply
-   Supply return / GND
S   Single-wire TTL signal
```

Verify the connector orientation, share GND between all devices, and use an external supply for actuators.

## First-Wiring Checklist

1. Connect one TTL bus device.
2. Run a read-only example.
3. Add the actuator load only after feedback works.
4. Assign a unique ID to each device before building a multi-device bus.

Software UARTs are not recommended because the default 1 Mbps bus rate requires reliable high-speed timing.
