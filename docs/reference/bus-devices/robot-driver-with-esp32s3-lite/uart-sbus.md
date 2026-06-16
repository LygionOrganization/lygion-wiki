# UART 透传与 S.BUS

UART0 可以承担三种互斥用途：

1. 默认串口透传，让 FD 软件直接访问总线舵机。
2. JSON 指令通信，供 Raspberry Pi 或其他 MCU 控制驱动板。
3. S.BUS 输入，读取航模遥控接收机。

改变用途前应明确当前固件配置，避免多个功能同时占用 UART0。

## FD 串口透传

1. 给驱动板连接与舵机匹配的外部电源。
2. 将开关拨到 `ON`。
3. 使用 Type-C 数据线连接驱动板的 `UART` 接口与电脑。
4. 打开 FD 软件。
5. FD 软件端波特率始终选择 `1M`。
6. 设置驱动板与舵机通信的实际波特率。

例如舵机波特率为 500 Kbps：

```json
{"T":10,"baud":500000}
```

可以在 Web 控制台选择 `500K`，也可以通过 USB CDC、HTTP 或 WebSocket 发送上述指令。

让设备每次开机自动设置 500 Kbps：

```json
{"T":303,"name":"boot","json":"{\"T\":10,\"baud\":500000}"}
```

!!! note "两段波特率含义不同"
    FD 软件到驱动板的 UART0 链路固定使用 1 Mbps；驱动板到舵机的总线波特率由 `T:10` 配置。

## UART JSON 通信

UART0 默认开启透传。切换为 JSON 指令通信：

```json
{"T":605,"sf":0}
```

恢复透传：

```json
{"T":605,"sf":1}
```

让设备开机后自动关闭透传：

```json
{"T":303,"name":"boot","json":"{\"T\":605,\"sf\":0}"}
```

切换后，HAT 接口或 UART Type-C 可以接收每行一条的 JSON 指令。

## S.BUS 接线

使用 HAT 接口连接航模遥控接收机：

| 驱动板 | 接收机 |
| --- | --- |
| 5V | 电源输入 |
| GND | GND |
| ESP32-RX | S.BUS 信号 |

板载 5V 电源最高支持 5A，但仍应确认接收机的允许输入电压和接线定义。

## 启用 S.BUS 固件功能

在 `Config.h` 中添加：

```cpp
#define UART0_AS_SBUS
```

编译并上传后，UART0 用于 S.BUS。默认项目在 `main.cpp` 的 `loop()` 中包含读取示例：

```cpp
#ifdef UART0_AS_SBUS
if (sbus.Read()) {
  sbusData = sbus.data();

  for (int8_t i = 0; i < sbusData.NUM_CH; i++) {
    Serial.print(sbusData.ch[i]);
    Serial.print("\t");
  }

  Serial.print(sbusData.lost_frame);
  Serial.print("\t");
  Serial.println(sbusData.failsafe);
}
#endif
```

## 通道映射示例

不同遥控器的中位、端点和通道顺序可能不同。先打印原始通道值，再根据实际范围归一化：

```cpp
float speed_limit = 1.0f;

if (sbusData.ch[4] < 300) {
  speed_limit = 0.33f;
} else if (sbusData.ch[4] == 1002) {
  speed_limit = 0.66f;
} else if (sbusData.ch[4] > 1700) {
  speed_limit = 1.0f;
}

float speed_input =
    constrain(float(sbusData.ch[2] - SBUS_MID) / SBUS_RAN, -1.0f, 1.0f);
float turn_input =
    -constrain(float(sbusData.ch[3] - SBUS_MID) / SBUS_RAN, -1.0f, 1.0f);

float left_speed =
    speed_input * speed_limit * 6000.0f -
    turn_input * 0.33f * 6000.0f;
float right_speed =
    speed_input * speed_limit * 6000.0f +
    turn_input * 0.33f * 6000.0f;
```

!!! warning "先处理失控保护"
    实际机器人中，应在输出电机指令前检查 `lost_frame` 和 `failsafe`，并在信号丢失时主动停止执行器。

编译环境与上传方法见[PlatformIO 二次开发](advanced-development.md)。
