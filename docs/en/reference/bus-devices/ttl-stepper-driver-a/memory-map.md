# TTL Stepper Driver (A) Memory Map and Phase Calculator

This page is for lower-level configuration and troubleshooting. Most users should start with the normal motion APIs first, then come here when they need to change IDs, baud rates, protection behavior, operating mode, or the driver phase byte.

TTL Stepper Driver (A) uses the FT-SCS bus protocol. Factory serial settings are:

```text
Baud rate: 1 Mbps
Data bits: 8
Parity: none
Stop bits: 1
Default ID: 1
```

Two-byte values are stored little-endian: the low byte is at the lower address, and the high byte is at the next address.

!!! warning "Be careful with EPROM writes"
    EPROM settings affect communication and low-level behavior. Record the original values before changing ID, baud rate, operating mode, phase, or protection parameters. If you write these values from code, make sure you understand the write-lock behavior.

## Phase Calculator

The driver phase byte is at address `18 / 0x12`. It is a 1-byte bit field. Use the calculator below to build the decimal value to write, or enter an existing decimal value to decode it.

<div class="ttlsd-phase-tool" data-ttlsd-phase-tool data-phase-locale="en">
  <div class="ttlsd-phase-grid">
    <div class="ttlsd-phase-panel">
      <h3>Build the value</h3>
      <label>
        <span>Direction phase BIT0</span>
        <select data-phase-bit="0">
          <option value="0">0: forward</option>
          <option value="1">1: reverse</option>
        </select>
      </label>
      <label>
        <span>Step code M2M1M0 BIT3-BIT1</span>
        <select data-phase-microstep>
          <option value="0">000: 15 rpm</option>
          <option value="2">001: 7.5 rpm</option>
          <option value="4">010: undefined / reserved</option>
          <option value="6">011: 3.75 rpm</option>
          <option value="8">100: 0.94 rpm</option>
          <option value="10">101: 0.47 rpm</option>
          <option value="12">110: undefined / reserved</option>
          <option value="14">111: undefined / reserved</option>
        </select>
      </label>
      <label>
        <span>Speed-mode behavior BIT4</span>
        <select data-phase-bit="4">
          <option value="0">0: speed 0 means stop</option>
          <option value="1">1: speed 0 means maximum speed</option>
        </select>
      </label>
      <label>
        <span>Limit / home input phase BIT5</span>
        <select data-phase-bit="5">
          <option value="0">0: low level active</option>
          <option value="1">1: high level active</option>
        </select>
      </label>
      <label>
        <span>Target-current behavior BIT6</span>
        <select data-phase-bit="6">
          <option value="0">0: current 0 means default current</option>
          <option value="1">1: current 0 means zero current</option>
        </select>
      </label>
      <label>
        <span>Heartbeat BIT7</span>
        <select data-phase-bit="7">
          <option value="0">0: disabled</option>
          <option value="1">1: enabled</option>
        </select>
      </label>
    </div>

    <div class="ttlsd-phase-panel">
      <h3>Result</h3>
      <dl class="ttlsd-phase-result">
        <div>
          <dt>Decimal value</dt>
          <dd data-phase-dec>0</dd>
        </div>
      </dl>
      <label>
        <span>Decode an existing value</span>
        <input data-phase-input type="text" inputmode="numeric" placeholder="For example: 161">
      </label>
      <p class="ttlsd-phase-hint" data-phase-message>Enter a decimal value from 0 to 255 to decode it.</p>
      <ul class="ttlsd-phase-breakdown" data-phase-breakdown></ul>
    </div>
  </div>
</div>


## Memory Areas

| Address range | Area | Access | What it is used for |
| --- | --- | --- | --- |
| `0x00-0x04` | Version information | Read-only | Firmware and driver version data |
| `0x05-0x27` | EPROM configuration | Read / write | ID, baud rate, operating mode, phase, and protection settings |
| `0x28-0x37` | SRAM control | Read / write | Runtime commands such as torque enable, acceleration, target position, current, and speed |
| `0x38-0x43` | SRAM feedback | Read-only | Position, speed, voltage, temperature, status, and movement feedback |
| `0x53-0x56` | Factory parameters | Read-only | Current, speed, and acceleration limits |

## Version Information

| DEC | HEX | Name | Bytes | Default | Access | Range | Unit | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `0x00` | Firmware major version | 1 | 8 | Read-only |  |  |  |
| 1 | `0x01` | Firmware minor version | 1 | -- | Read-only | `0-39` |  |  |
| 2 | `0x02` | Endianness marker | 1 | 0 | Read-only |  |  | `0` means little-endian storage |
| 3 | `0x03` | Driver major version | 1 | 10 | Read-only |  |  |  |
| 4 | `0x04` | Driver minor version | 1 | -- | Read-only |  |  |  |

## EPROM Configuration

!!! note "Address columns"
    The HEX column below is normalized from the DEC address. If an older table shows a mismatch around addresses `35-38`, confirm against your firmware documentation or by reading the device.

| DEC | HEX | Name | Bytes | Default | Access | Range | Unit | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | `0x05` | ID | 1 | 1 | Read / write | `0-253` | ID | Main device ID. Each device on the bus needs a unique main ID. |
| 6 | `0x06` | Baud rate | 1 | 0 | Read / write | `0-7` |  | `0-7` map to `1000000`, `500000`, `250000`, `128000`, `115200`, `76800`, `57600`, `38400` |
| 7 | `0x07` | Secondary ID | 1 | 0 | Read / write | `0-253` | ID | Used only for write commands. Useful for follower-mode synchronization. |
| 8 | `0x08` | Return level | 1 | 1 | Read / write | `0-1` |  | `0`: only read and ping return a packet. `1`: all commands return a packet. |
| 9 | `0x09` | Minimum angle limit | 2 | 0 | Read / write | `0-65534` | steps | Use `0` for multi-turn absolute position control. |
| 11 | `0x0B` | Maximum angle limit | 2 | 0 | Read / write | `0-65534` | steps | Use `0` for multi-turn absolute position control. |
| 13 | `0x0D` | Maximum temperature | 1 | 70 | Read / write | `0-100` | deg C |  |
| 14 | `0x0E` | Maximum input voltage | 1 | 250 | Read / write | `0-254` | 0.2 V | `250 x 0.2 = 50.0 V` |
| 15 | `0x0F` | Minimum input voltage | 1 | 40 | Read / write | `0-254` | 0.1 V |  |
| 16 | `0x10` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 17 | `0x11` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 18 | `0x12` | Driver phase | 1 | -- | Read / write | `0-254` |  | Special behavior byte. Do not change it unless you know which behavior you need. |
| 19 | `0x13` | Release conditions | 1 | -- | Read / write | `0-254` |  | Each bit enables or disables a protection behavior. |
| 20 | `0x14` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 21 | `0x15` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 22 | `0x16` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 23 | `0x17` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 24 | `0x18` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 25 | `0x19` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 26 | `0x1A` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 27 | `0x1B` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 28 | `0x1C` | Default current | 2 | -- | Read / write | `0-1000` | 1% | Loaded into target current at address `44 / 0x2C` after power-up. |
| 30 | `0x1E` | Angle resolution | 1 | 1 | Read / write | `1-128` |  | Multiplier for the sensor's minimum angle resolution. |
| 31 | `0x1F` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 32 | `0x20` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 33 | `0x21` | Operating mode | 1 | 0 | Read / write | `0-3` |  | `0`: position mode. `1`: constant-speed mode. `2`: follower mode. |
| 34 | `0x22` | Protection current | 1 | -- | Read / write | `0-100` | 0.1% |  |
| 35 | `0x23` | Protection time | 1 | -- | Read / write | `0-254` | 10 ms |  |
| 36 | `0x24` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 37 | `0x25` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 38 | `0x26` | Heartbeat timeout | 1 | -- | Read / write | `0-254` | 100 ms |  |

## SRAM Control

| DEC | HEX | Name | Bytes | Default | Access | Range | Unit | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | `0x28` | Torque enable | 1 | 0 | Read / write | `0-1` |  | Write `0` to disable motor output. Write `1` to enable motor output. |
| 41 | `0x29` | Acceleration | 1 | 0 | Read / write | `0-254` | 100 microsteps/s^2 | Actual acceleration = acceleration `(41)` x acceleration multiplier `(86)`. `0` means maximum acceleration. |
| 42 | `0x2A` | Target position | 2 | 0 | Read / write | `0-65534` | steps | Absolute position target. Step unit = microsteps x angle resolution. |
| 44 | `0x2C` | Target current | 2 | Default current `(28)` | Read / write | `0-1000` | 0.1% | `BIT10` is the direction bit. |
| 46 | `0x2E` | Running speed | 2 | Factory maximum | Read / write | `-32767-32767` | 50 microsteps/s | Maximum running speed. In speed mode, `BIT15` is the direction bit. |
| 48 | `0x30` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 49 | `0x31` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 50 | `0x32` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 51 | `0x33` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 52 | `0x34` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 53 | `0x35` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 54 | `0x36` | Undefined | 1 | -- | Read / write | -- | -- |  |
| 55 | `0x37` | Write lock | 1 | 1 | Read / write | `0-1` |  | Write `0` to unlock EPROM writes so they are saved after power-off. Write `1` to lock EPROM writes so changes are not saved. |

## SRAM Feedback

| DEC | HEX | Name | Bytes | Default | Access | Range | Unit | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 56 | `0x38` | Present position | 2 | -- | Read-only | -- | steps | Current absolute position. Step unit = microsteps x angle resolution. |
| 58 | `0x3A` | Present speed | 2 | -- | Read-only | -- | 50 microsteps/s | `BIT15` is the direction bit. |
| 60 | `0x3C` | Output pulse rate | 2 | -- | Read-only | -- | pulses/ms | Current output pulse rate. `BIT10` is the direction bit. |
| 62 | `0x3E` | Present voltage | 1 | -- | Read-only | -- | 0.1 V | Driver input voltage. |
| 63 | `0x3F` | Present temperature | 1 | -- | Read-only | -- | deg C | Driver internal temperature. |
| 64 | `0x40` | Async-write flag | 1 | 0 | Read-only | -- |  | Flag used with asynchronous write commands. |
| 65 | `0x41` | Driver status | 1 | 0 | Read-only | -- |  | A bit set to `1` means the corresponding fault or condition is active. |
| 66 | `0x42` | Moving flag | 1 | 0 | Read-only | -- |  | `1` while moving, `0` after the motor has reached the target and stopped, `2` for fly-jump hold trigger. |
| 67 | `0x43` | Current target position | 2 | -- | Read-only | -- | steps | The active target position. |

## Factory Parameters

| DEC | HEX | Name | Bytes | Default | Access | Range | Unit | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 83 | `0x53` | Maximum current limit `(x4)` | 1 | -- | Read-only | -- | -- | -- |
| 84 | `0x54` | Maximum speed limit | 1 | -- | Read-only | -- | -- | `x20` |
| 85 | `0x55` | Acceleration limit | 1 | -- | Read-only | -- | -- | -- |
| 86 | `0x56` | Acceleration multiplier | 1 | -- | Read-only | -- | -- | -- |

## Special Bytes

### Driver Phase `0x12`

| Bit | Weight | Meaning | `0` | `1` |
| --- | --- | --- | --- | --- |
| BIT0 | 1 | Direction phase | Forward | Reverse |
| BIT1 | 2 | Step code M0 | See M2M1M0 table | See M2M1M0 table |
| BIT2 | 4 | Step code M1 | See M2M1M0 table | See M2M1M0 table |
| BIT3 | 8 | Step code M2 | See M2M1M0 table | See M2M1M0 table |
| BIT4 | 16 | Speed-mode behavior | Speed `0` means stop | Speed `0` means maximum speed |
| BIT5 | 32 | Limit / home input phase | Low level active | High level active |
| BIT6 | 64 | Target-current behavior | Target current `0` means default current | Target current `0` means zero current |
| BIT7 | 128 | Heartbeat | Disabled | Enabled |

M2M1M0 code:

| M2M1M0 | Decimal contribution | Meaning |
| --- | --- | --- |
| `000` | `0` | 15 rpm |
| `001` | `2` | 7.5 rpm |
| `011` | `6` | 3.75 rpm |
| `100` | `8` | 0.94 rpm |
| `101` | `10` | 0.47 rpm |

### Driver Status `0x41`

For status bits, `0` means normal and `1` means the condition is active.

| Bit | Weight | Meaning | Recovery |
| --- | --- | --- | --- |
| BIT0 | 1 | Over-voltage / under-voltage | Voltage returns to the valid range |
| BIT1 | 2 | Target out of range | Target returns to the valid range |
| BIT2 | 4 | Over-temperature | Temperature returns to the valid range |
| BIT3 | 8 | Over-current trigger, FALT low detected | Re-enable torque output |
| BIT4 | 16 | Automatic current limiting | Update the target |
| BIT5 | 32 | Limit switch triggered | Leave the limit after debounce |
| BIT6 | 64 | Target out of range | Target returns to the valid range |
| BIT7 | 128 | Home switch triggered | Leave the home switch after debounce |

### Release Conditions `0x13`

For release-condition bits, `0` means disabled and `1` means enabled.

| Bit | Weight | Meaning |
| --- | --- | --- |
| BIT0 | 1 | Voltage protection: disables torque output and recovers automatically when voltage is valid |
| BIT1 | 2 | Reserved |
| BIT2 | 4 | Over-temperature protection: disables torque output and recovers automatically after cooling |
| BIT3 | 8 | Reserved |
| BIT4 | 16 | Current-limit protection: when there is no target update and the motor has stopped, output current is reduced to the protection value |
| BIT5 | 32 | Reserved |
| BIT6 | 64 | Limit protection: decelerates to stop; move away in the opposite direction to recover |
| BIT7 | 128 | Reserved |
