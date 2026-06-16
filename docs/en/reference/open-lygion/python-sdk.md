# Python SDK

The Lygion Python SDK is intended for Windows, Linux, macOS, Raspberry Pi, Jetson, and other host-side environments that need to access Lygion TTL bus devices.

- [Lygion Python SDK on GitHub](https://github.com/LygionOrganization/lygion_devs_py)
- [Download the Python SDK](../../assets/files/lygion_devs_py.zip)

## Get the SDK

Use Git when you want the latest repository version:

```bash
git clone https://github.com/LygionOrganization/lygion_devs_py.git
cd lygion_devs_py
```

If GitHub is not available, download and extract the ZIP package from this Wiki.

[Download Python SDK](../../assets/files/lygion_devs_py.zip){ .md-button }

## Prepare the Environment

The SDK generally requires Python 3 and a serial communication package. These tutorials cover the common setup steps:

- [Install Python](../../tutorials/install-python.md)
- [Find the Serial Port](../../tutorials/find-serial-port.md)
- [Run Python Scripts](../../tutorials/run-python-scripts.md)
- [Device IDs and Baud Rates](../../tutorials/device-id-and-baudrate.md)
- [Power and Wiring](../../tutorials/power-and-wiring-basics.md)

Create a virtual environment inside the SDK directory and install the serial dependency:

=== "Windows"

    ```powershell
    py -3 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install pyserial
    ```

=== "macOS / Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install pyserial
    ```

## Example Areas

The repository organizes examples by device type. Before running an example, update its serial port name, device ID, and baud rate for your hardware.

| Device / task | Example area |
| --- | --- |
| TTL Node (A) | [`lynode`](https://github.com/LygionOrganization/lygion_devs_py/tree/main/lynode) |
| TTL Stepper Driver (A) | `lyttlsd` examples |
| TTL Encoder E02 | Encoder readout and parameter examples |
| Device parameter setup | `*_eprom.py` examples |

!!! warning "Read before you write"
    Start with scan or feedback examples. Run motion or parameter-writing examples only after the serial port, ID, baud rate, and power supply are confirmed.

## Typical Debug Flow

1. Connect only one new device to avoid factory-default ID conflicts.
2. Read feedback through the FD utility or SDK.
3. Confirm the device ID and baud rate.
4. Update example code with the correct serial port and ID.
5. Test motion or outputs with low speed and small commands first.

Related tools:

- [FD Device Utility](../../tutorials/fd-tool.md)
- [TTL Adapter (A) SDKs and Tools](../bus-devices/ttl-adapter-a/sdk-and-tools.md)
- [TTL Node (A) SDKs and Tools](../bus-devices/ttl-node-a/sdk-and-tools.md)
