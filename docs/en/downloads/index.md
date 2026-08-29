# Downloads

This page collects SDKs, utilities, CAD files, and project resources referenced throughout the documentation. Product-specific images, CAD files, and examples are still maintained in each product's `assets/` directory; this page provides the common entry points.

## SDKs and Utilities

| Type | GitHub / source | Local download | Guide |
| --- | --- | --- | --- |
| Python SDK | [lygion_devs_py](https://github.com/LygionOrganization/lygion_devs_py) | [lygion_devs_py.zip](../../assets/files/lygion_devs_py.zip) | [Python First Demo](../quickstart/python-first-demo.md) |
| C++ / Arduino SDK | [lygion_devs_cpp](https://github.com/LygionOrganization/lygion_devs_cpp) | [lygion_devs_cpp.zip](../../assets/files/lygion_devs_cpp.zip) | [C++ / Arduino First Demo](../quickstart/cpp-first-demo.md) |
| FD Device Utility | - | [FD.7z](../../assets/files/FD.7z) | [FD Device Utility](../tutorials/fd-tool.md) |

## TTL Bus Device Models

| Product | CAD file |
| --- | --- |
| TTL Adapter (A) | [ttl-adapter-a.step](../../reference/bus-devices/ttl-adapter-a/assets/ttl-adapter-a.step) |
| TTL Encoder E02 | [TTL-Encoder-E02.step](../../reference/bus-devices/ttl-encoder-e02/assets/TTL-Encoder-E02.step) |
| TTL Stepper Driver (A) | [TTL Stepper Driver STEP](../../reference/bus-devices/ttl-stepper-driver-a/assets/TTL_SD_Simple%20Assembly.step) |
| Robot Driver with ESP32S3 Lite | [Robot Driver with ESP32S3 Lite.step](<../../reference/bus-devices/robot-driver-with-esp32s3-lite/assets/Robot Driver with ESP32S3 Lite.step>) |
| SC-0090-C043 TTL bus servo | [SC-0090-C043.step](../../reference/bus-devices/bus-servos/assets/SC-0090-C043.step) |
| SC-0090-C049 TTL bus servo | [SC-0090-C049.step](../../reference/bus-devices/bus-servos/assets/SC-0090-C049.step) |
| SC-1500-C023 TTL bus servo | [SC-1500-C023.step](../../reference/bus-devices/bus-servos/assets/SC-1500-C023.step) |
| SC-1500-C024 TTL bus servo | [SC-1500-C024.stp](../../reference/bus-devices/bus-servos/assets/SC-1500-C024.stp) |
| 0090 series servo horns | [Round](../../reference/bus-devices/bus-servos/assets/arms-0090/cycle.stp) · [Half-arm](../../reference/bus-devices/bus-servos/assets/arms-0090/haftarm.stp) · [Single-arm](../../reference/bus-devices/bus-servos/assets/arms-0090/onearm.stp) · [Cross](../../reference/bus-devices/bus-servos/assets/arms-0090/tenarm.stp) |

## Robot Module Models

| Product | CAD file |
| --- | --- |
| SW69-TTL Steering Wheel Module | [SW69-TTL_STEP.step](../../reference/modules/sw69-ttl/assets/SW69-TTL_STEP.step) |
| 4240BY-G5.2 Stepper Motor | [4240BY-G5.2.step](../../reference/modules/4240by-g5-2/assets/4240BY-G5.2.step) |
| DW69 Drive Wheel | [DW69 [SP01].step](<../../reference/modules/dw69/assets/DW69 [SP01].step>) · [DW69 [SP02][SP03].step](<../../reference/modules/dw69/assets/DW69 [SP02][SP03].step>) |
| DM42-G7220-E02 Joint Actuator | [DW42-G7220-E02.step](../../reference/modules/dm42-g7220-e02/assets/DW42-G7220-E02.step) |
| 3M 72T Timing Pulley | [SP3M72-E02.step](../../reference/modules/pulley-3m-72t/assets/SP3M72-E02.step) |

## Open Project Models

| Project | File |
| --- | --- |
| 3D3S Omnidirectional Chassis | [3D3S_Chassis.step](../../reference/open-lygion/assets/3D3S_Chassis.step) |
| 6x6 Rover | [6x6-rover.zip](../../reference/open-lygion/assets/6x6-rover.zip) |
| 5+1 DOF Robotic Arm | [5-plus-1-dof-robotic-arm.step](../../reference/open-lygion/assets/5-plus-1-dof-robotic-arm.step) |
| Open Leader Arm | [open_leader_arm.step](../../reference/open-lygion/assets/open_leader_arm.step) |
| Self-locking Gripper | [self-locking-gripper.step](../../reference/open-lygion/assets/self-locking-gripper.step) |
| OpenLygion 4WD AL | [OpenLygion 4WD AL.step](<../../reference/open-lygion/assets/OpenLygion 4WD AL.step>) |
| OpenLygion 4WD SheetMetal | [OpenLygion 4WD SheetMetal.step](<../../reference/open-lygion/assets/OpenLygion 4WD SheetMetal.step>) |
| OpenLygion Balance | [OpenLygion Balance.step](<../../reference/open-lygion/assets/OpenLygion Balance.step>) |

## Common Entry Points

- [TTL Bus Devices](../reference/bus-devices/index.md)
- [Robots](../reference/robots/index.md)
- [Open Lygion](../reference/open-lygion/index.md)
- [Tutorials](../tutorials/index.md)

!!! note "Single source for CAD files"
    STEP, STP, ZIP, and other model files are maintained once in each product's `assets/` directory. The Chinese and English download pages both link to those shared files to avoid version drift.
