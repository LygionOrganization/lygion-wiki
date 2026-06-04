# TTL-5264 8P Hub (A)

TTL-5264 8P Hub (A) fans out one TTL bus into eight 5264-3P connectors. It is suited to Lygion stepper drivers, compatible Feetech bus servos, and other TTL devices using 5264-3P connections.

[Power grouping and isolation guide](../../../tutorials/power-grouping-and-decoupling.md){ .md-button }

## Features

- Eight 5264-3P TTL bus connectors
- DC5521 power input
- KF301-2P terminal power input
- Board-to-board TTL communication connector for cascading hubs
- Separate hubs can use separate supply voltages
- Power indicator
- Approximate size: `44 x 21 x 14 mm`

## Interfaces

| No. | Interface | Purpose |
| --- | --- | --- |
| 1 | KF301-2P terminal | Power input connected to the DC5521 input; use either input |
| 2 | Power indicator | Shows whether power is present |
| 3 | Mounting holes | Four holes, approximately 3 mm diameter |
| 4 | DC5521 input | DC 5-25.2 V power input |
| 5 | Single-wire TTL interconnect | Carries communication between hubs |
| 6 | Eight 5264-3P connectors | Connect TTL bus devices |

!!! note "The hub does not regulate voltage"
    Apply a voltage that is safe for every servo, joint, wheel module, driver, or other device connected to that powered group.
