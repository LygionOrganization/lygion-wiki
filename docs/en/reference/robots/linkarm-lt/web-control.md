# LinkArm-LT Web Control

## Network Modes

In AP mode, connect directly to the default `Robot` network and open `http://192.168.4.1`. In STA mode, connect the arm to an existing LAN and use the assigned IP address. AP and STA can operate at the same time.

The saved Wi-Fi password is intentionally not displayed as plain text in the page.

## Control Modes

FPV control moves the end effector relative to its current orientation. Cartesian control moves along the configured X, Y, and Z axes. Start at low speed and use one control mode consistently.

!!! warning "Avoid high-rate mixed control"
    Rapidly alternating FPV, Cartesian, script, and remote commands can create discontinuous targets.

The console also provides device information, Wi-Fi settings, mission management, and a JSON command panel for immediate testing.

