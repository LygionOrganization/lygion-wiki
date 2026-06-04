# Run Python Scripts

This guide explains how to run Lygion Python SDK examples on Linux, macOS, and Windows.

## 1. Open the SDK Directory

Assume the SDK folder is named:

```text
lygion_devs_py
```

Change to its actual location:

=== "Linux / macOS"

    ```bash
    cd ~/lygion_devs_py
    ```

=== "Windows"

    ```powershell
    cd $env:USERPROFILE\Desktop\lygion_devs_py
    ```

See [Open a terminal](open-terminal.md) if you are not sure where to enter these commands.

## 2. Create and Activate a Virtual Environment

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

A successful activation usually adds `(.venv)` to the terminal prompt.

If PowerShell reports that scripts are disabled, allow activation only for the current window:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 3. Set the Serial Port

Open the example and replace the default port with the port detected on your computer:

=== "Linux"

    ```python
    portHandler = PortHandler('/dev/ttyUSB0')
    ```

=== "macOS"

    ```python
    portHandler = PortHandler('/dev/tty.usbserial-xxxx')
    ```

=== "Windows"

    ```python
    portHandler = PortHandler('COM3')
    ```

See [Find the serial port](find-serial-port.md) if you do not know the correct name.

## 4. Run the Script

=== "Linux / macOS"

    ```bash
    python3 ttlsd_ping.py
    ```

=== "Windows"

    ```powershell
    python .\ttlsd_ping.py
    ```

For a script in a subdirectory:

=== "Linux / macOS"

    ```bash
    python3 lyttlsd/ttlsd_read.py
    ```

=== "Windows"

    ```powershell
    python .\lyttlsd\ttlsd_read.py
    ```

## 5. Confirm Communication

Successful output may look like:

```text
[ID:001] ping Succeeded.
```

or:

```text
[ID:001] PresPos:1200 PresSpd:0
```

This confirms that the port opened and that the selected baud rate and device ID can communicate on the TTL bus.

## Troubleshooting

### Python is not found

Verify the installation:

=== "Linux / macOS"

    ```bash
    python3 --version
    ```

=== "Windows"

    ```powershell
    py -3 --version
    ```

See [Install Python](install-python.md) if the command fails.

### The script file is not found

Check the current directory and its files:

=== "Linux / macOS"

    ```bash
    pwd
    ls
    ```

=== "Windows"

    ```powershell
    pwd
    dir
    ```

### The serial port will not open

Check the port name, close FD and other serial applications, install the Windows driver if needed, and verify Linux permissions. See [Find the serial port](find-serial-port.md) and [Install the USB serial driver](install-usb-serial-driver.md).
