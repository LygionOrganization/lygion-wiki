# Read TTL Encoder E02 with C++ / Arduino

The C++ / Arduino SDK supports the encoder from ESP32S3, ESP32, Arduino Mega2560, STM32 Arduino Core, and other compatible MCU platforms.

- [C++ SDK on GitHub](https://github.com/LygionOrganization/lygion_devs_cpp)
- [Download the C++ / Arduino SDK](../../../../assets/files/lygion_devs_cpp.zip)

## Initialize the UART

ESP32S3:

```cpp
Serial1.begin(1000000, SERIAL_8N1, 18, 17);
ttlsd.pSerial = &Serial1;
```

Mega2560:

```cpp
Serial1.begin(1000000);
ttlsd.pSerial = &Serial1;
```

Keep only the initialization that matches your board and wiring.

## Read One Encoder

```cpp
#include <lygion_devs.h>

TTLSDClass ttlsd;

void setup()
{
  Serial.begin(115200);
  Serial1.begin(1000000, SERIAL_8N1, 18, 17);
  ttlsd.pSerial = &Serial1;
  delay(1000);
}

void loop()
{
  int pos = ttlsd.ReadPos(1);
  int speed = ttlsd.ReadSpeed(1);

  if (!ttlsd.getLastError()) {
    float angle_deg = pos / 4096.0f * 360.0f;
    float speed_deg_s = speed / 4096.0f * 360.0f;
    Serial.print("Angle: ");
    Serial.println(angle_deg);
    Serial.print("Speed: ");
    Serial.println(speed_deg_s);
  } else {
    Serial.println("Read error");
  }

  delay(100);
}
```

For a multi-encoder synchronous read, first assign a unique ID to every encoder and include only connected IDs in the read list.
