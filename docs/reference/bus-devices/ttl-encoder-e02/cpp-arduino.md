# TTL Encoder E02 C++ / Arduino

TTL Encoder E02 可通过 C++ / Arduino SDK 在 ESP32S3、ESP32、Arduino Mega2560、STM32 Arduino Core 等平台上读取。

## 获取 SDK

- [Github (C++ SDK)](https://github.com/LygionOrganization/lygion_devs_cpp)

如果你无法访问 Github，也可以从本站下载，下载入口：

- [C++ / Arduino SDK](../../../assets/files/lygion_devs_cpp.zip)

## 串口初始化

ESP32S3 示例：

```cpp
Serial1.begin(1000000, SERIAL_8N1, 18, 17);
ttlsd.pSerial = &Serial1;
```

Mega2560 示例：

```cpp
Serial1.begin(1000000);
ttlsd.pSerial = &Serial1;
```

!!! warning "只保留一种串口初始化方式"
    如果使用 ESP32S3，请保留带 RX/TX 引脚的初始化。如果使用 Mega2560，请保留普通 `Serial1.begin(1000000)`。

## 读取单个编码器

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
    Serial.print("Position:");
    Serial.println(pos);
    Serial.print("Speed:");
    Serial.println(speed);
  } else {
    Serial.println("read error");
  }

  delay(100);
}
```

## 角度换算

```cpp
float angle_deg = pos / 4096.0f * 360.0f;
float speed_deg_s = speed / 4096.0f * 360.0f;
```

## 同步读取多个编码器

同步读取前，先确认每个设备 ID 不重复。

```cpp
uint8_t ID[] = {1, 2, 3};
```

只把真实存在的 ID 放入数组。
