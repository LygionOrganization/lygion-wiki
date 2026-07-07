# 3M 72T Timing Pulley

The 3M 72T Timing Pulley is a 72-tooth pulley for 3M-pitch timing belts. It is designed for robot joints, turntables, belt reductions, and output shafts where synchronized belt transmission is needed.

## Highlights

- 3M timing belt profile.
- 72-tooth pulley for larger output-side diameter or belt reduction stages.
- Includes mounting features for an E02 encoder setup.
- STEP, PDF, and DXF files are available for design and machining checks.

## Typical Uses

- Robot joint output pulley
- Belt-driven rotary stages
- Swing arms and turntables
- Output-side angle sensing with a TTL Encoder E02

## Mechanical Interface

| Item | Value |
| --- | --- |
| Belt profile | 3M |
| Tooth count | 72T |
| Encoder mounting holes | 8 x M3 x 0.5 |
| Encoder mounting PCD | Ø60 |
| Auxiliary mounting holes | 6 x M4 x 0.7 through |
| Reference center bore | Ø23 |

!!! note "Use the drawing for final design"
    Pulley center distance, belt length, and shaft alignment are sensitive to small errors. Use the CAD model and drawing before machining or assembly.

## Encoder Use

The pulley can be used with [TTL Encoder E02](../../bus-devices/ttl-encoder-e02/index.md) when output-side absolute angle feedback is required.

When installing the encoder:

- Align the magnet center with the encoder IC center as closely as possible.
- Keep the magnet-to-IC distance within the encoder installation requirement.
- Secure the encoder PCB so it cannot move during operation.
- Use a unique encoder ID on the TTL bus.

## Downloads

| Resource | File |
| --- | --- |
| STEP model | [SP3M72-E02.step](../../../../reference/modules/pulley-3m-72t/assets/SP3M72-E02.step) |
| Mechanical drawing PDF | [SP3M72-E02.pdf](../../../../reference/modules/pulley-3m-72t/assets/SP3M72-E02.pdf) |
| DXF drawing | [SP3M72-E02.dxf](../../../../reference/modules/pulley-3m-72t/assets/SP3M72-E02.dxf) |

## Related Pages

- [TTL Encoder E02](../../bus-devices/ttl-encoder-e02/index.md)
- [TTL Encoder E02: Hardware Installation](../../bus-devices/ttl-encoder-e02/hardware-installation.md)
- [Downloads](../../../downloads/index.md)
