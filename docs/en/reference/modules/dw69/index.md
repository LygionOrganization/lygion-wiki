# DW69 Drive Wheel

DW69 is a 69 mm drive wheel assembly for small mobile robot bases, teaching platforms, and experimental chassis. The page below explains how to configure the wheel motor with TTL Stepper Driver (A), run a safe first test, and use the Python or ESP32 Arduino examples.

![DW69 drive wheel and driver wiring](../../../../reference/modules/dw69/assets/dw69-wiring.webp){ .img-rounded }

## Highlights

- 69 mm class drive wheel for compact mobile bases.
- Designed for robot chassis integration with a motor, bracket, and driver.
- Multiple STEP assemblies are available for different mechanical integration needs.
- Works with [TTL Stepper Driver (A)](../../bus-devices/ttl-stepper-driver-a/index.md) when TTL bus speed control is required.

## Typical Uses

- Differential-drive robot bases
- Three-wheel or four-wheel mobile platforms
- Educational mobile robots
- Custom wheel-drive mechanisms

## Mechanical Resources

| Resource | Notes |
| --- | --- |
| `DW69 [SP01].step` | One DW69 assembly model |
| `DW69 [SP02][SP03].step` | Another DW69 assembly model |
| `DW69.pdf` | Mechanical drawing |
| `DW69.dxf` | DXF drawing |

!!! note "Use CAD for final integration"
    Before machining a chassis plate or printing a bracket, check wheel clearance, screw access, and interference in the STEP model.

## Configure with FD

Use FD on Windows to configure the TTL Stepper Driver (A) before running code.

### What You Need

| Item | Purpose |
| --- | --- |
| DW69 wheel and motor | The wheel mechanism under test |
| TTL Stepper Driver (A) | Drives the stepper motor |
| TTL Adapter (A) | Connects the PC USB port to the TTL bus |
| External DC power supply | Powers the driver and motor |
| Windows PC | Runs the FD device utility |

!!! warning "Lift the wheel first"
    Keep the wheel off the desk or floor during the first test. Let it touch the ground only after direction, speed, and stop behavior are confirmed.

### Wiring

1. Connect the DW69 motor to TTL Stepper Driver (A) with the 4-pin motor cable.
2. Connect TTL Stepper Driver (A) to TTL Adapter (A) with the 5264 3-pin TTL bus cable.
3. Connect external power to TTL Stepper Driver (A).
4. Connect TTL Adapter (A) to the PC with USB.
5. Open FD, select the adapter serial port, and set baud rate to `1000000`.
6. Click `Open`, then `Search`. The driver should appear as `TTL_SD01`.

![DW69 FD search result](../../../../reference/modules/dw69/assets/fd-wheel-search-cn.webp){ .img-rounded }

### Recommended Parameters

Set these parameters on the driver's `Programming` page:

| Parameter | Suggested value | Meaning |
| --- | ---: | --- |
| ID | `1` | Fine for a single-wheel test. Use unique IDs on a shared bus. |
| Driver phase | `152` | Recommended phase setting for this wheel drive setup. |
| Operating mode | `1` | Speed mode for continuous wheel rotation. |
| Heartbeat timeout | `20` | Unit is 100 ms, so this is about 2 seconds. |

![DW69 FD wheel parameters](../../../../reference/modules/dw69/assets/fd-wheel-params-cn.webp){ .img-rounded }

!!! note "Screenshot IDs are examples"
    The screenshots show where to edit the values. The ID shown in the screenshot may differ from the ID you choose for your own device.

After saving parameters, power-cycle the driver. This makes sure the phase and mode settings are applied cleanly.

![DW69 FD save parameters](../../../../reference/modules/dw69/assets/fd-wheel-save-cn.webp){ .img-rounded }

### First Speed Test

On the `Debug` page, start with conservative values:

| Parameter | Suggested value | Meaning |
| --- | ---: | --- |
| Acceleration | `15` | Avoid `0` for normal bring-up; `0` means near-maximum acceleration. |
| Speed | `100` or lower | Start slow, then increase after the wheel runs smoothly. |
| Torque/current | `200` | About 1.32 A phase current. |
| Target | Any value | Ignored in speed mode. |

Approximate phase current:

```text
phase current (A) ≈ 3.3 × 2 × current / 1000
```

With current `200`:

```text
3.3 × 2 × 200 / 1000 = 1.32 A
```

Click `Set`. The wheel should rotate continuously. If heartbeat protection is enabled and no new speed command is sent, the driver should stop the wheel after about 2 seconds.

![DW69 FD speed test](../../../../reference/modules/dw69/assets/fd-wheel-test-cn.webp){ .img-rounded }

## Python Example

The Python example drives the wheel forward, stops, drives it backward, and stops again. It periodically resends the speed command so heartbeat protection does not stop the wheel during the timed run.

Before running it:

- Install the Lygion Python SDK.
- Change `PORT_NAME` to your actual serial port.
- Change `WHEEL_DRIVER_ID` to the ID saved in FD.
- Make sure the driver is in speed mode.

[Download Python example](../../../../reference/modules/dw69/assets/dw69_example.py){ .md-button }

## ESP32 Arduino Example

The Arduino example uses `Serial1` on ESP32 or ESP32S3 and sends speed commands through `WriteSpe()`.

Before uploading it:

- Install the Lygion C++ / Arduino SDK.
- Connect ESP32 RX/TX/GND to TTL Adapter (A).
- Change `WHEEL_DRIVER_ID` if your driver ID is not `1`.
- Make sure the driver is in speed mode.

[Download ESP32 Arduino example](../../../../reference/modules/dw69/assets/dw69_esp32_example.ino){ .md-button }

## Troubleshooting

| Symptom | Likely cause | What to check |
| --- | --- | --- |
| Wheel does not move | Wrong mode, no external power, or motor phase wiring issue | Confirm mode `1`, external power, and A/B phase wiring |
| Wheel moves briefly, then stops | Heartbeat protection is active but commands are not resent | Keep the periodic send loop in the example |
| Wheel vibrates or only makes noise | Speed or acceleration too high, current too low, or load too heavy | Lower speed, use non-zero acceleration, and check load |
| Direction is reversed | Motor phase order or installation direction differs from your coordinate system | Negate the speed value in software |

## Downloads

| Resource | File |
| --- | --- |
| STEP model SP01 | [DW69 [SP01].step](<../../../../reference/modules/dw69/assets/DW69 [SP01].step>) |
| STEP model SP02/SP03 | [DW69 [SP02][SP03].step](<../../../../reference/modules/dw69/assets/DW69 [SP02][SP03].step>) |
| Mechanical drawing PDF | [DW69.pdf](../../../../reference/modules/dw69/assets/DW69.pdf) |
| DXF drawing | [DW69.dxf](../../../../reference/modules/dw69/assets/DW69.dxf) |
| Python example | [dw69_example.py](../../../../reference/modules/dw69/assets/dw69_example.py) |
| ESP32 Arduino example | [dw69_esp32_example.ino](../../../../reference/modules/dw69/assets/dw69_esp32_example.ino) |

## Related Pages

- [TTL Stepper Driver (A)](../../bus-devices/ttl-stepper-driver-a/index.md)
- [TTL Stepper Driver (A): Operating Modes](../../bus-devices/ttl-stepper-driver-a/operating-modes.md)
- [FD Device Utility](../../../tutorials/fd-tool.md)
