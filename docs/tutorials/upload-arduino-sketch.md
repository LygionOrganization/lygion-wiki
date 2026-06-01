# 上传 Arduino 示例程序

本文说明如何使用 Arduino IDE 上传 Lygion C++ SDK 示例程序。

## 1. 打开示例

在 Arduino IDE 中打开 `.ino` 示例，例如：

```text
example/lyttlsd/FeedBack.ino
```

第一次建议运行读取类示例，例如 `FeedBack.ino`，不要直接运行会让电机高速运动的示例。

## 2. 选择开发板

在 Arduino IDE 中选择：

```text
Tools / 工具 → Board / 开发板
```

然后选择你的开发板，例如：

- ESP32S3 Dev Module
- ESP32 Dev Module
- Arduino Mega or Mega 2560
- 你的 STM32 开发板型号

## 3. 选择端口

连接 MCU 开发板后，选择：

```text
Tools / 工具 → Port / 端口
```

选择开发板对应的串口。

!!! note "这是 MCU 的 USB 上传端口"
    这里选择的是电脑与 MCU 开发板之间的 USB 串口，不是 TTL 总线设备的串口。

## 4. 修改代码中的硬件串口

ESP32S3 示例：

```cpp
Serial.begin(115200);
Serial1.begin(1000000, SERIAL_8N1, 18, 17);
ttlsd.pSerial = &Serial1;
```

如果你的接线使用了其它 RX / TX 引脚，请修改 `18` 和 `17`。

Mega2560 示例：

```cpp
Serial.begin(115200);
Serial1.begin(1000000);
ttlsd.pSerial = &Serial1;
```

## 5. 编译并上传

点击 Arduino IDE 左上角的上传按钮。

如果上传成功，底部会显示类似：

```text
Done uploading.
```

## 6. 打开串口监视器

选择：

```text
Tools / 工具 → Serial Monitor / 串口监视器
```

将波特率设置为：

```text
115200
```

该值应与代码中的：

```cpp
Serial.begin(115200);
```

一致。

## 7. 查看输出

如果通信正常，串口监视器可能输出：

```text
Position:1200
Speed:0
```

如果失败，可能输出：

```text
FeedBack error
```

请检查：

- 设备 ID 是否正确。
- TTL 总线波特率是否为 `1000000`。
- RX / TX / GND 是否接好。
- 总线设备是否供电。
- 是否存在重复 ID。
