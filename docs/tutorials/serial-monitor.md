# 打开串口监视器

串口监视器用于查看 MCU 程序通过 `Serial.print()` 输出的调试信息。

## 1. Arduino IDE

打开方式：

```text
Tools / 工具 → Serial Monitor / 串口监视器
```

或点击右上角的串口监视器图标。

将波特率设置为：

```text
115200
```

该值需要与代码一致：

```cpp
Serial.begin(115200);
```

## 2. PlatformIO

在 VS Code 下方工具栏点击：

```text
Monitor
```

或在终端中运行：

```bash
pio device monitor
```

`platformio.ini` 中建议设置：

```ini
monitor_speed = 115200
```

## 3. 串口监视器和 TTL 总线波特率的区别

常见代码：

```cpp
Serial.begin(115200);
Serial1.begin(1000000, SERIAL_8N1, 18, 17);
```

含义：

| 代码 | 用途 |
| --- | --- |
| `Serial.begin(115200)` | MCU 和电脑之间的调试串口 |
| `Serial1.begin(1000000, ...)` | MCU 和 TTL 总线设备之间的通信串口 |

!!! warning "不要把 115200 改成 1000000"
    串口监视器通常看 `Serial` 输出，波特率应设置为 `115200`。

    TTL 总线设备默认是 `1000000`，这是 `Serial1` 与设备通信使用的波特率。

## 4. 没有输出怎么办？

请检查：

- 程序是否上传成功。
- 串口监视器端口是否选择正确。
- 波特率是否设置为 `115200`。
- 程序中是否有 `Serial.begin(115200);`。
- 是否需要按一下开发板复位键。

## 5. 有输出但读取失败怎么办？

说明 MCU 和电脑之间的调试串口正常，但 MCU 和 TTL 总线设备之间通信失败。

请检查：

- `ttlsd.pSerial = &Serial1;` 是否正确。
- `Serial1` 的 RX / TX 引脚是否与实际接线一致。
- TTL Adapter (A) 的 RX / TX / GND 是否连接正确。
- 总线设备 ID、波特率、供电是否正确。
