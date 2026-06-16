# 安装 PlatformIO

PlatformIO 是集成在 VS Code 中的嵌入式开发环境，适合需要长期维护 MCU 工程的用户。本页只用于快速完成安装；如果你要修改完整固件，请阅读[VS Code + PlatformIO 复杂项目开发](platformio-development/index.md)。

如果你是第一次使用 MCU，建议先使用 [Arduino IDE](install-arduino-ide.md)。如果你已经熟悉 VS Code，PlatformIO 会更适合工程化开发。

## 1. 安装 VS Code

先安装 Visual Studio Code。

安装完成后打开 VS Code。

## 2. 安装 PlatformIO 插件

1. 打开 VS Code 左侧 Extensions / 扩展。
2. 搜索：

```text
PlatformIO IDE
```

3. 点击 Install / 安装。
4. 安装完成后重启 VS Code。

左侧出现小蚂蚁图标，说明 PlatformIO 已安装。

## 3. 创建或打开工程

### 创建新工程

1. 点击 PlatformIO 图标。
2. 选择 `New Project`。
3. 填写工程名称。
4. 选择开发板，例如 ESP32S3 Dev Module。
5. 选择框架，例如 Arduino。
6. 创建工程。

### 打开已有工程

如果 SDK 或示例已经是 PlatformIO 工程，直接选择：

```text
File → Open Folder
```

打开工程文件夹。

## 4. platformio.ini 示例

ESP32S3 + Arduino 框架示例：

```ini
[env:esp32-s3-devkitc-1]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
monitor_speed = 115200
```

如果你使用其它开发板，需要把 `board` 改成对应型号。

## 5. 上传和打开串口监视器

常用按钮：

| 功能 | 说明 |
| --- | --- |
| Build | 编译工程 |
| Upload | 编译并上传到开发板 |
| Monitor | 打开串口监视器 |
| Upload and Monitor | 上传后自动打开串口监视器 |

串口监视器波特率通常使用：

```text
115200
```

该值需要与代码中的：

```cpp
Serial.begin(115200);
```

一致。

## 6. 下一步

- [VS Code + PlatformIO 复杂项目开发](platformio-development/index.md)
- [MCU C++ 路线：跑通第一个 Demo](../quickstart/cpp-first-demo.md)
- [MCU UART 接线基础](mcu-uart-wiring.md)
- [打开串口监视器](serial-monitor.md)
