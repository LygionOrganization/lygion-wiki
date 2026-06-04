# Robot Driver with ESP32S3 Lite FAQ

## I connected to `Robot`, but my phone says there is no Internet

That is expected. Stay connected and open `http://192.168.4.1/`; the hotspot is for local board access.

## The Web App does not open

Confirm that you are connected to the board's AP, use `http` rather than `https`, and try `192.168.4.1`. If using STA mode, read the current IP from the OLED and ensure the host is on the same LAN.

## The board works over USB, but servos do not move

USB powers the controller, not the peripheral power rail. Connect a compatible DC or XT30 supply and turn on the peripheral power switch.

## The servo is online but does not respond correctly

Check the servo family selected in the Web App, device ID, bus baud rate, supply voltage, torque state, and duplicate IDs.

## Which host interface should I use?

- Use **USB CDC** for reliable wired control.
- Use **HTTP** for simple request-response commands.
- Use **WebSocket** for persistent low-latency control and asynchronous feedback.
- Use the **Web App** for configuration and manual testing.

## My USB CDC command is ignored

Terminate each JSON object with a newline and keep the command within the firmware input-buffer limit.

## How do I stop a running mission?

Send:

```json
{"T":0}
```

Also design a hardware power-stop path for real mechanisms.

## Why did my saved actions or Wi-Fi settings disappear?

Clearing NVS removes saved configuration. Resetting LittleFS removes mission files. Firmware flashing may also erase stored data depending on the selected erase settings.

## Where is the authoritative command list?

See `src/Config.h` in the [official firmware repository](https://github.com/LygionOrganization/robot_driver_with_esp32s3_lite).
