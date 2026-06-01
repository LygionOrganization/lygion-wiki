# TTL Stepper Driver (A) C++ / Arduino

TTL Stepper Driver (A) 可通过 C++ / Arduino SDK 在 ESP32S3、ESP32、Arduino Mega2560、STM32 Arduino Core 等平台上控制。

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

## 常用示例

| 示例 | 用途 |
| --- | --- |
| `FeedBack.ino` | 读取位置、速度、电压、温度等反馈 |
| `WritePos.ino` | 位置模式控制 |
| `WriteSpe.ino` | 速度模式控制 |
| `SyncRead.ino` | 同步读取多个设备 |
| `SyncWritePos.ino` | 同步写入多个目标位置 |
| `SyncWriteSpe.ino` | 同步写入多个速度 |
| `RegWritePos.ino` | 预写入后统一执行 |
| `ProgramEprom.ino` | 参数设置 |
| `CalibrationOfs.ino` | 设置当前位置基准 |

## 位置控制示意

```cpp
ttlsd.WritePosEx(1, 3200, 200, 10, 150);
```

## 速度控制示意

```cpp
ttlsd.WheelMode(1);
ttlsd.WriteSpe(1, 100, 10, 150);
delay(2000);
ttlsd.WriteSpe(1, 0, 10, 150);
```

## 调试建议

- 先读取反馈，再写入控制指令。
- 第一次运动使用较低速度和非 0 加速度。
- 多设备同步前，先单独确认每个设备 ID 和波特率。
- 软件串口不适合 1 Mbps 高速通信，建议使用硬件串口。
