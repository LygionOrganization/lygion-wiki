# Build, Upload, and Debug

## Common Commands

```bash
pio run
pio run -t upload
pio device monitor
pio run -t clean
```

Specify an environment with `-e <environment>` when the project defines more than one.

## Build

Build before connecting hardware whenever possible. Read errors from the first meaningful compiler or linker message; later messages are often consequences.

## Upload Safely

1. Secure the robot and clear its workspace.
2. Disconnect actuator power when the firmware can be tested without it.
3. Close serial monitors and tools that may hold the port.
4. Confirm the target environment and upload port.
5. Upload, then observe the boot log before enabling motion.

Set `upload_port` only when automatic detection is unreliable. Some boards require holding `BOOT`, pressing `RESET`, or using a dedicated USB-UART download connector.

## Serial Logs

Match `monitor_speed` to the firmware baud rate. Log initialization stages, configuration validity, bus failures, and safety-state transitions. Avoid flooding high-frequency control loops with logs.

Verify changes in stages: boot, communications, one peripheral, one low-speed actuator movement, and finally the integrated workflow.

