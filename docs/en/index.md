# Lygion Wiki

Lygion Wiki is the product documentation and developer center for Lygion Robotics hardware. It is written for engineers, makers, educators, and system integrators who need to connect a device, verify communication, and move from a first test to a working robot.

Use this site to find wiring guidance, software setup instructions, SDK examples, product specifications, and troubleshooting steps.

## Start Here

Choose the route that matches your controller:

| Development route | Best for | Connection | Start tutorial |
| --- | --- | --- | --- |
| Python | PC, macOS, Raspberry Pi, Jetson, RK boards, and other Linux SBCs | USB -> TTL Adapter (A) -> TTL bus | [Run the first Python demo](quickstart/python-first-demo.md) |
| C++ / Arduino | ESP32S3, ESP32, STM32, Arduino, and custom MCU boards | MCU UART -> TTL Adapter (A) or a single-wire TTL interface | [Run the first C++ demo](quickstart/cpp-first-demo.md) |

!!! tip "Which route should I choose?"
    Choose **Python** when your controller runs a desktop or Linux operating system. Choose **C++ / Arduino** when your controller is a microcontroller.

## Common Tasks

### Configure a device without writing code

FD is a Windows utility for scanning TTL bus devices, changing IDs and baud rates, viewing feedback, editing parameters, and updating firmware.

![FD device utility](assets/images/fd-01-en.png){ .img-rounded width="450" }

[Use the FD utility](tutorials/fd-tool.md){ .md-button }

### Develop with Python

| Task | Guide |
| --- | --- |
| Connect a TTL bus device for the first time | [Python first demo](quickstart/python-first-demo.md) |
| Fix an unrecognized TTL Adapter (A) | [Install the USB serial driver](tutorials/install-usb-serial-driver.md) |
| Open a command-line window | [Open a terminal, PowerShell, or Command Prompt](tutorials/open-terminal.md) |
| Install or verify Python | [Install Python](tutorials/install-python.md) |
| Find the serial port name | [Find the serial port](tutorials/find-serial-port.md) |
| Run an SDK example | [Run Python scripts](tutorials/run-python-scripts.md) |

### Develop with C++ / Arduino

| Task | Guide |
| --- | --- |
| Connect a TTL bus device to an MCU | [C++ first demo](quickstart/cpp-first-demo.md) |
| Develop with Arduino IDE | [Install Arduino IDE](tutorials/install-arduino-ide.md) |
| Develop with VS Code and PlatformIO | [Install PlatformIO](tutorials/install-platformio.md) |
| Wire an MCU UART to the bus | [MCU UART wiring](tutorials/mcu-uart-wiring.md) |
| Build and upload an `.ino` example | [Upload an Arduino example](tutorials/upload-arduino-sketch.md) |
| View MCU debug output | [Use a serial monitor](tutorials/serial-monitor.md) |

### Find Product Documentation

| Product | What it does |
| --- | --- |
| [TTL Adapter (A)](reference/bus-devices/ttl-adapter-a/index.md) | Converts USB or an MCU UART into a single-wire TTL bus interface |
| [TTL Stepper Driver (A)](reference/bus-devices/ttl-stepper-driver-a/index.md) | Controls a bipolar stepper motor over the TTL bus |
| [TTL Encoder E02](reference/bus-devices/ttl-encoder-e02/index.md) | Reports absolute angle and speed over the TTL bus |

## Recommended Reading Order

1. Complete the [Python](quickstart/python-first-demo.md) or [C++ / Arduino](quickstart/cpp-first-demo.md) first demo.
2. Read the reference page for your product.
3. Use the [tutorial library](tutorials/index.md) when you need help with wiring, power, serial ports, IDs, or baud rates.
4. Get SDKs, utilities, and CAD files from the [download center](downloads/index.md).

## Links

- [Lygion Robotics website](https://lygion.ai)
- [Lygion Organization on GitHub](https://github.com/LygionOrganization/)
- [Chinese documentation](../)
