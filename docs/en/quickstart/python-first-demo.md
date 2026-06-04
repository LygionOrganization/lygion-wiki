# Python First Demo

This tutorial takes you from an unopened SDK to a successful first TTL bus read. By the end, you will have verified the computer, TTL Adapter (A), USB serial driver, device ID, baud rate, bus wiring, and power.

It applies to Windows, macOS, Linux, Raspberry Pi, Jetson, RK boards, and other systems that run Python.

```text
Computer / Raspberry Pi / Jetson / other SBC
        | USB
        v
TTL Adapter (A)
        | TTL bus
        v
TTL Encoder E02 / TTL Stepper Driver (A) / compatible TTL bus device
```

![USB connection](../../assets/images/g01.png){ .img-rounded width="450" }

!!! note "Use the tab for your operating system"
    Commands are grouped into Linux, macOS, and Windows tabs. Run only the commands for your system.

## 1. Prepare the Hardware

| Item | Purpose |
| --- | --- |
| [TTL Adapter (A)](../reference/bus-devices/ttl-adapter-a/index.md) | Converts the computer's USB connection to the Lygion TTL bus |
| One TTL bus device | For example, TTL Stepper Driver (A), TTL Encoder E02, or a compatible bus servo |
| USB Type-C data cable | Must support data, not charging only |
| External power supply | Must match the connected bus device |
| Computer or SBC | Windows, macOS, Linux, Raspberry Pi, Jetson, or similar |

For the first test, connect only one new device. Several factory-new devices may share the same default ID.

!!! warning "Do not use USB as the main actuator supply"
    USB is suitable for communication and limited low-power testing. Apply a compatible external supply before operating a stepper motor, servo, wheel module, or other actuator. See [Power and wiring fundamentals](../tutorials/power-and-wiring-basics.md).

## 2. Confirm USB Serial Detection

Connect TTL Adapter (A). Most current systems install the driver automatically.

=== "Linux"

    ```bash
    lsusb
    ```

=== "macOS"

    If no `/dev/tty.usb*` or `/dev/cu.usb*` port appears later, install the appropriate USB serial driver.

=== "Windows"

    Open Device Manager and check for a new COM port. Install the driver if the adapter appears as an unknown device.

See [Install the USB serial driver](../tutorials/install-usb-serial-driver.md) when the adapter is not detected.

## 3. Open a Command-Line Window

=== "Linux"

    Press `Ctrl + Alt + T` or open **Terminal** from the application menu.

=== "macOS"

    Press `Command + Space`, search for **Terminal**, and press Enter.

=== "Windows"

    Right-click the Start button and open **Terminal** or **PowerShell**.

See [Open a terminal, PowerShell, or Command Prompt](../tutorials/open-terminal.md) for more detail.

## 4. Verify Python

=== "Linux / macOS"

    ```bash
    python3 --version
    ```

=== "Windows"

    ```powershell
    py -3 --version
    ```

Use Python 3.9 or later when possible. If the command does not print a Python version, follow [Install Python](../tutorials/install-python.md).

## 5. Get the Python SDK

Clone the SDK:

=== "Linux / macOS"

    ```bash
    git clone https://github.com/LygionOrganization/lygion_devs_py.git
    cd lygion_devs_py
    ```

=== "Windows"

    ```powershell
    git clone https://github.com/LygionOrganization/lygion_devs_py.git
    cd lygion_devs_py
    ```

You can also [download the Python SDK ZIP](../../assets/files/lygion_devs_py.zip) and extract it to an easy-to-find location.

## 6. Create a Virtual Environment

Run these commands from the SDK directory:

=== "Linux / macOS"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

=== "Windows"

    ```powershell
    py -3 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

After activation, the prompt normally begins with `(.venv)`.

If PowerShell blocks the activation script, allow it for the current window:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

See [Run Python scripts](../tutorials/run-python-scripts.md) for a fuller explanation.

## 7. Install the Python Dependency

Run this while the virtual environment is active:

=== "Linux / macOS"

    ```bash
    python3 -m pip install --upgrade pip
    python3 -m pip install pyserial
    ```

=== "Windows"

    ```powershell
    python -m pip install --upgrade pip
    python -m pip install pyserial
    ```

## 8. Find the Serial Port

=== "Linux"

    ```bash
    ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
    ```

    A typical result is `/dev/ttyUSB0`. If access is denied:

    ```bash
    sudo usermod -aG dialout $USER
    ```

    Log out and back in before retrying.

=== "macOS"

    ```bash
    ls /dev/tty.usb* /dev/cu.usb* 2>/dev/null
    ```

    Prefer a `/dev/cu.usbserial-xxxx` device when available.

=== "Windows"

    Open **Device Manager -> Ports (COM & LPT)** and find an entry such as:

    ```text
    USB-Enhanced-SERIAL CH343 (COM3)
    ```

See [Find the serial port](../tutorials/find-serial-port.md) if you need help identifying it.

## 9. Confirm Device ID and Baud Rate

Typical factory settings are:

| Setting | Typical default |
| --- | --- |
| Device ID | `1` |
| Baud rate | `1000000` (1 Mbps) |

Some compatible SCS servos may use `500000`. Check the product documentation when the typical defaults do not work.

!!! warning "Every device on one bus needs a unique ID"
    Connect only one device while testing or assigning a new ID. Duplicate IDs cause reply collisions.

See [Device IDs and baud rates](../tutorials/device-id-and-baudrate.md).

## 10. Configure the Example

Open the example script and set the detected serial port:

=== "Linux"

    ```python
    portHandler = PortHandler('/dev/ttyUSB0')
    ```

=== "macOS"

    ```python
    portHandler = PortHandler('/dev/cu.usbserial-xxxx')
    ```

=== "Windows"

    ```python
    portHandler = PortHandler('COM3')
    ```

Confirm the baud rate and device ID:

```python
portHandler.setBaudRate(1000000)
DEV_ID = 1
```

For the first test, change only the serial port unless you know the device uses different settings.

## 11. Run a Read-Only Test

Start with a `ping` or read example. Exact filenames can vary by SDK release.

=== "Linux / macOS"

    ```bash
    python3 ttlsd_ping.py
    ```

=== "Windows"

    ```powershell
    python .\ttlsd_ping.py
    ```

Successful output may look like:

```text
[ID:001] ping Succeeded.
```

You can then try a feedback example:

=== "Linux / macOS"

    ```bash
    python3 ttlsd_read.py
    ```

=== "Windows"

    ```powershell
    python .\ttlsd_read.py
    ```

Example output:

```text
[ID:001] PresPos:1200 PresSpd:0
```

If those filenames are not present, look for examples containing `ping`, `read`, `sync_read`, or `feedback`. Avoid motion examples until read-only communication works.

## 12. Continue with Your Product

| Product | Next guide |
| --- | --- |
| TTL Encoder E02 | [Read the encoder with Python](../reference/bus-devices/ttl-encoder-e02/python-quickstart.md) |
| TTL Stepper Driver (A) | [Control the driver with Python](../reference/bus-devices/ttl-stepper-driver-a/python-quickstart.md) |
| TTL Adapter (A) | [Drivers and serial ports](../reference/bus-devices/ttl-adapter-a/drivers-and-ports.md) |

## Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| No serial port | Charge-only USB cable, missing driver, USB issue | Use a data cable, reconnect, install the driver |
| Port will not open | Wrong port, another app uses it, Linux permission issue | Verify the port, close serial tools, fix permissions |
| Ping fails | Wrong ID or baud rate, bad bus wiring, no device power | Check ID, rate, `+ / - / S`, and external power |
| Reads are corrupted | Duplicate IDs, poor connection, unstable power | Test one device, reseat cables, verify the supply |
| Actuator does not move | No external power, low current, wrong mode or active limit | Verify the actuator supply and product settings |

For a systematic checklist, see [Communication troubleshooting](../tutorials/communication-troubleshooting.md).
