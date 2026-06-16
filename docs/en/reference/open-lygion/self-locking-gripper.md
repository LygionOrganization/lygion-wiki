# Self-locking Gripper

Self-locking Gripper is a mechanical end-effector project designed around a self-locking gripper structure. The current Wiki page provides the main image and STEP model.

![Self-locking Gripper](../../../reference/open-lygion/assets/self-locking-gripper.webp){ .img-rounded width="520" }

[Download STEP Model](../../../reference/open-lygion/assets/self-locking-gripper.step){ .md-button }

## Resources

| File | Description |
| --- | --- |
| [`self-locking-gripper.step`](../../../reference/open-lygion/assets/self-locking-gripper.step) | Mechanical STEP model |

## Notes

- The self-locking structure is useful when the gripper needs to hold position without continuous force.
- Before mounting it on an arm, test travel range, servo direction, and gripping force independently.
- For software bring-up, see the [Python SDK](python-sdk.md), [C++ SDK](cpp-sdk.md), and [Power and Wiring](../../tutorials/power-and-wiring-basics.md).
