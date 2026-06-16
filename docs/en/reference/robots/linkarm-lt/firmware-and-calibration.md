# Firmware Recovery and Midpoint Calibration

!!! danger "Disconnect actuator power before flashing"
    Do not run the arm immediately after replacing firmware. Restore and verify calibration first.

Use the firmware package and flashing tool supplied for the exact hardware revision. Connect the designated download USB interface, select the documented flash addresses and options, enter download mode, and verify the completed write before rebooting.

## Midpoint Calibration { #midpoint-calibration }

If the RGB indicator stays yellow or the boot pose is clearly wrong, the midpoint file may be missing or invalid.

1. Secure and support the arm.
2. Place every joint in the documented reference pose.
3. Record the raw midpoint values using the calibration procedure.
4. Save and back up the calibration file.
5. Restart while keeping clear of the workspace.
6. Test one low-speed movement at a time.

!!! danger "The arm may restart twice during calibration"
    Keep people and objects away until the process has fully completed.

