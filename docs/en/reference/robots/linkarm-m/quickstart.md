# LinkArm-M Quick Start

## 1. Secure and Inspect the Arm

Fasten the arm to a desk or chassis, clear its workspace, and make sure cables cannot be pulled or pinched.

## 2. Connect Power and USB

Connect a 12 V supply rated for at least 3 A, then connect a data cable to the **TTL Node (A) Type-C port**. The SDK uses `500000` baud.

## 3. Install the SDK

```bash
git clone https://github.com/LygionOrganization/linkarm_python_sdk.git
cd linkarm_python_sdk
python -m venv venv
```

Activate the environment for your operating system, then run:

```bash
python -m pip install -r requirements.txt
```

## 4. Configure the Arm

Find the serial port and edit `arm_config.json`:

```json
{
  "linkarm": {
    "default_device_serial_ports": "COM7",
    "serial_baudrate": 500000,
    "servo_middle": [513, 508, 327, 632]
  }
}
```

Replace the port and use the four midpoint values printed on your arm. Do not copy the example values.

## 5. Read Before Moving

```bash
python linkarm.py status
```

Then test a small movement:

```bash
python linkarm.py gripper -1
python linkarm.py gripper 0
python linkarm.py joint 3 -1 --reliable
```

!!! danger "The first command may initialize the whole arm"
    Recheck the midpoint values, mounting, power, and workspace before sending any motion command.

