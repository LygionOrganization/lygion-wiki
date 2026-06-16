# PlatformIO Troubleshooting

## PlatformIO Keeps Initializing

Restart VS Code, allow the first-time downloads to finish, and check the PlatformIO output panel. Avoid installing multiple extensions that bundle competing PlatformIO environments.

## pio Is Not Found

Use a PlatformIO terminal or the VS Code status-bar actions. A missing global `pio` command does not necessarily mean the extension is broken.

## No Build Button Appears

Open the directory containing `platformio.ini`, trust the workspace, and wait for extension initialization.

## The First Build Cannot Download Packages

Check proxy, DNS, firewall, certificate, and registry access. Retry after confirming that the package host is reachable.

## Header Not Found

Check the include spelling, `lib_deps`, local `lib/` layout, selected environment, and conditional build flags. Clean and rebuild after correcting dependencies.

## Upload Port Missing or Busy

Use a data-capable cable, install the USB serial driver, close other serial applications, and confirm the correct USB connector. On Linux, verify serial-device permissions.

## Upload Waits at Connecting

Enter the board's download mode using its `BOOT`/`RESET` sequence or dedicated download connector, then retry.

## Firmware Uploads but Does Not Run

Check the serial boot log, flash and partition settings, USB mode, filesystem compatibility, and whether the project expects configuration files in `data/`.

## Robot Behavior Is Abnormal

Disconnect actuator power. Verify pin definitions, bus baud rate, device IDs, calibration, direction limits, startup tasks, and persisted configuration before trying again.

!!! danger "Do not debug motion by repeated power cycling"
    Repeated uncontrolled starts can damage the robot or its surroundings. Restore a known firmware/configuration pair and test with actuators disabled first.

