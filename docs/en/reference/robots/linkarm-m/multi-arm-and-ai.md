# Multiple Arms and AI Integration

Give every LinkArm-M its own serial port and configuration file. Never copy midpoint values between physical arms.

On Linux, stable `/dev/serial/by-id/` paths are preferable to changing `/dev/ttyUSB*` numbers. On other systems, identify devices by USB serial number when possible.

The CLI's JSON output and batch mode can serve as a narrow tool interface for a higher-level application or AI agent. Expose validated operations such as:

- read status and pose
- open or close the gripper
- move one joint within limits
- move to a validated Cartesian target
- stop the current sequence

Keep safety checks outside the language model: enforce limits, timeouts, collision zones, command schemas, and operator authorization in deterministic code. Serialize commands for each arm and coordinate shared-workspace motion centrally.

