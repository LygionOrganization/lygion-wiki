# Web Console

Connect to the controller's `Robot` access point with password `12345678`, then open `http://192.168.4.1`. The console is also available through the device's LAN address when STA mode is configured.

The web interface provides:

- device information and bus baud-rate settings
- Wi-Fi AP and STA configuration
- STS/SMS, HLS, and SCS servo controls
- automation-script creation and playback
- a JSON command console

!!! warning "Use one baud rate across the bus"
    The controller and every connected bus device must use the same baud rate.

If a page opens but controls do not respond, reload it, verify power and bus wiring, check the browser console, and confirm that no other host is issuing conflicting commands.

