# Robots

This section contains setup, control, integration, calibration, and troubleshooting documentation for complete Lygion robot systems. These guides combine the mechanical structure, electronics, firmware features, and host-side control workflow for each robot.

## Products

| Product | Focus | Guide |
| --- | --- | --- |
| LinkArm-M | Robotic arm controlled through a Python SDK and CLI; suitable for scripting, education, experiments, and AI integration. | [Open guide](linkarm-m/index.md) |
| LinkArm-LT | Robotic arm platform with Web console, action scripts, JSON commands, and wireless synchronized teaching. | [Open guide](linkarm-lt/index.md) |

## How to Read These Guides

1. Start from the quick-start page for the product and complete power, connection, and basic motion checks.
2. For regular use, continue with configuration, calibration, and firmware recovery.
3. For integration work, read the SDK, JSON command, action scripting, and host communication pages.

## Related Tutorials

- [Install Python](../../tutorials/install-python.md)
- [Find the Serial Port](../../tutorials/find-serial-port.md)
- [Power and Wiring](../../tutorials/power-and-wiring-basics.md)
- [Communication Troubleshooting](../../tutorials/communication-troubleshooting.md)

!!! tip "Validate the robot by itself before system integration"
    Before connecting a robot arm to a mobile base, vision system, or AI workflow, confirm standalone motion, zero position, limits, emergency stop behavior, and power stability.
