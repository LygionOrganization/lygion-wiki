# 安装 Arduino IDE

Arduino IDE 是 MCU C++ 路线中最适合新手的开发工具。它可以用于打开 `.ino` 示例、选择开发板、编译并上传程序。

## 1. 适用用户

如果你使用以下开发板，可以先从 Arduino IDE 开始：

- ESP32S3
- ESP32
- Arduino Mega2560
- Arduino Due
- 部分 STM32 Arduino Core 支持的开发板

## 2. 下载并安装

请从 Arduino 官方网站下载 Arduino IDE 2.x。

安装完成后，打开 Arduino IDE。

## 3. 安装开发板支持包

### ESP32 / ESP32S3

1. 打开 Arduino IDE。
2. 进入 `File / 文件 → Preferences / 首选项`。
3. 在 `Additional boards manager URLs` 中添加 ESP32 开发板管理地址。
4. 打开 `Tools / 工具 → Board / 开发板 → Boards Manager`。
5. 搜索 `esp32`。
6. 安装 Espressif Systems 提供的 ESP32 支持包。

!!! note "开发板支持包地址可能会更新"
    ESP32 开发板管理地址可能随 Arduino 和 Espressif 版本变化。若安装失败，请参考 Espressif 官方 Arduino-ESP32 文档。

### Arduino Mega2560

Arduino Mega2560 通常不需要额外安装开发板包，Arduino IDE 默认支持。

### STM32

STM32 需要安装对应的 STM32 Arduino Core。不同开发板差异较大，请优先参考你所用开发板厂商的说明。

## 4. 安装 Lygion C++ SDK

下载 C++ SDK：

- [C++ SDK 下载](../downloads/index.md#c-sdk)

将库文件复制到 Arduino 的 libraries 目录。常见路径：

=== "Windows"

    ```text
    Documents\Arduino\libraries
    ```

=== "macOS"

    ```text
    ~/Documents/Arduino/libraries
    ```

=== "Linux"

    ```text
    ~/Arduino/libraries
    ```

复制完成后，重启 Arduino IDE。

## 5. 打开示例程序

常见示例路径：

```text
example/lyttlsd/FeedBack.ino
example/lyttlsd/SyncRead.ino
example/lyttlsd/CalibrationOfs.ino
```

第一次建议打开 `FeedBack.ino`，先读取设备状态。

## 6. 选择开发板和端口

在 Arduino IDE 中选择：

```text
Tools / 工具 → Board / 开发板
```

然后选择你的开发板。

再选择：

```text
Tools / 工具 → Port / 端口
```

选择开发板对应的串口。

!!! tip "这里的端口是 MCU 开发板的 USB 串口"
    这个端口用于给 MCU 上传程序和查看调试输出，不是 TTL 总线设备的串口。

## 7. 下一步

安装完成后，继续阅读：

- [MCU C++ 路线：跑通第一个 Demo](../quickstart/cpp-first-demo.md)
- [上传 Arduino 示例程序](upload-arduino-sketch.md)
- [打开串口监视器](serial-monitor.md)
