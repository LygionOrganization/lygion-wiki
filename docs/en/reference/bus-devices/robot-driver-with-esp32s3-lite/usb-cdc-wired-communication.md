# USB CDC Wired Communication

USB CDC exposes the board as a serial device and accepts newline-terminated JSON commands. It is a good choice for reliable wired control from a PC, Raspberry Pi, Jetson, or another USB host.

## Prepare Python

```bash
python -m pip install pyserial
```

Find the board's serial port, such as `COM7` on Windows or `/dev/ttyACM0` on Linux.

## Send a JSON Command

```python
import json
import serial
import time

PORT = "COM7"
BAUD = 1000000  # USB CDC ignores the requested UART baud rate

ser = serial.Serial(PORT, BAUD, timeout=0.5)

def send_json(data):
    message = json.dumps(data) + "\n"
    ser.write(message.encode("utf-8"))

time.sleep(2)
send_json({"T": 202, "line": 1, "text": "USB CDC", "update": 1})
```

!!! note "The newline is required"
    The firmware processes a USB CDC JSON command after receiving `\n`.

## Read Responses

```python
line = ser.readline().decode("utf-8").strip()
if line:
    response = json.loads(line)
    print(response)
```

## Troubleshooting

- Confirm the correct serial port.
- Close other applications using the same port.
- Wait briefly after opening the port so the board can enumerate.
- Terminate every JSON object with a newline.
- Keep an individual command below the firmware command-buffer limit.

The official repository includes runnable examples under `python_example/usb_cdc`.
