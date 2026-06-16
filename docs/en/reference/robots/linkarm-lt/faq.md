# LinkArm-LT Troubleshooting

## The Arm Is Unstable

Use both clamps or a bolted base. Increase clamp spacing and verify that the supporting surface is rigid.

## The Arm Moves at Boot

Check boot missions, ESP-NOW follower mode, and active HTTP/WebSocket clients. Disconnect actuator power before changing startup behavior.

## The RGB Indicator Stays Yellow

Restore or recreate the midpoint calibration file before commanding motion.

## The Web Console Does Not Open

Confirm connection to the `Robot` network, keep the no-Internet Wi-Fi connection, open `http://192.168.4.1`, and disable VPN or proxy routing temporarily.

## Motion Is Weak on USB Power

Connect the specified external DC supply. USB is not sufficient for normal servo operation.

## Host Communication Fails

Verify the correct USB port or IP address, close competing serial clients, check the JSON newline framing, and confirm that port `80` is reachable for HTTP/WebSocket.

## The Pose Is Wrong after Flashing

Stop motion and restore midpoint calibration before further testing.

