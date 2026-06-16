# TTL Node (A) Quick Start

## What You Need

- TTL Node (A)
- A data-capable USB Type-C cable
- A Windows, Linux, or macOS computer, Raspberry Pi, or Jetson
- A DC 9-12.6 V supply when driving servos or PWM loads

## Choose a Power Method

| Function | USB only | USB + external power |
| --- | :---: | :---: |
| Communicate and configure | Yes | Yes |
| Read S.BUS and control RGB LEDs | Yes | Yes |
| Drive bus servos | No | Yes |
| Use PWM power outputs | No | Yes |

!!! danger "Connect external power only through a powered bus connector"
    Supply 9-12.6 V through HX-5264-3P or PH2.0-3P. GH1.25-3P contains only TTL data and ground.

## Confirm Communication

### FD on Windows

1. Connect the node and identify its COM port.
2. Open FD and select `1000000` baud.
3. Search for devices. A factory-default node normally appears as `TTL-Node-A` with ID `0`.
4. Use [Configure with FD](fd-configuration.md) to change its ID or baud rate.

### Python

1. [Install Python](../../../tutorials/install-python.md).
2. [Find the serial port](../../../tutorials/find-serial-port.md).
3. Download the [Python SDK](../../../assets/files/lygion_devs_py.zip).
4. Run `lynode/ttln_ping.py` or `lynode/ttln_adc.py` after setting the port and device ID.

!!! warning "Configure devices one at a time"
    Factory-default nodes all use ID `0`. Assign unique IDs before placing multiple nodes or servos on the same bus.

