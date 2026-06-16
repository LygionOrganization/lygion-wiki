# LinkArm-M Python SDK

Import `RobotController` from the cloned SDK and load the arm-specific configuration.

```python
from linkarm import RobotController

robot = RobotController("arm_config.json")
print(robot.get_status())
```

The API supports gripper control, individual and coordinated joint movement, current-pose reads, inverse kinematics, forward kinematics, and reliable motion sequences that wait for completion.

!!! warning "Use the installed SDK as the API reference"
    Method names and arguments may change. Inspect the current examples and Python help before deploying an application.

For robust automation:

- validate configuration before connecting
- start with read-only operations
- enforce workspace and joint limits
- use timeouts for reliable moves
- serialize commands per arm
- stop on communication or kinematics errors
- keep motion logic separate from perception and planning

