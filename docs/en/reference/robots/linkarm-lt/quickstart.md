# LinkArm-LT Quick Start

## 1. Secure the Arm

Use both supplied clamps, spaced as far apart as practical, or bolt the arm to a stable base.

!!! danger "Do not run the arm loose on a desk"
    Motion shifts the center of gravity and can overturn an unsecured arm.

## 2. Check Before Power-On

Clear the workspace, route cables safely, verify that no unknown boot mission or remote controller is active, and connect a stable DC 9-12.6 V supply rated for at least 3 A.

!!! warning "The arm may move immediately after boot"
    A boot mission, ESP-NOW leader, HTTP client, or WebSocket client can command motion.

## 3. Connect to the Web Console

1. Join the `Robot` Wi-Fi network.
2. Enter password `12345678`.
3. Stay connected even if the device reports no Internet access.
4. Open `http://192.168.4.1`.

Change the default access-point name and password when several robots operate nearby.

## 4. First Motion Test

Click `INIT`, then test one direction at low speed and a small gripper movement. Do not rapidly alternate between FPV and Cartesian modes during the first test.

