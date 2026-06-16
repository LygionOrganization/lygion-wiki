# LinkArm-M CLI Control

!!! danger "Check the arm before every motion command"
    Secure the base, clear the workspace, verify calibration, and keep an emergency power disconnect within reach.

View available commands:

```bash
python linkarm.py --help
python linkarm.py status
```

Typical controls include:

```bash
python linkarm.py gripper -1
python linkarm.py joint 3 -1 --reliable
python linkarm.py joints <j1> <j2> <j3> <j4> --reliable
```

The CLI also exposes inverse kinematics, forward kinematics, an interactive shell, batch execution, and JSON output. Use `--help` from the installed SDK as the authoritative command reference because option names can change between releases.

LinkArm-M Cartesian distances use millimeters and joint angles use radians unless the command help states otherwise.

