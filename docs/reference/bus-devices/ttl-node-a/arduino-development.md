# TTL Node (A) Arduino 开发

本页以 Robot Driver with ESP32S3 Lite 或通用 ESP32-S3 开发板为例，介绍如何使用 `lygion_devs` 库控制 TTL Node (A)。

## 准备环境

1. [安装 Arduino IDE](../../../tutorials/install-arduino-ide.md)。
2. 安装 ESP32 开发板支持，并选择 `ESP32S3 Dev Module`。
3. 下载 [C++ / Arduino SDK](../../../assets/files/lygion_devs_cpp.zip)。
4. 将解压后的库目录放入 Arduino 的 `libraries` 目录。
5. 重启 Arduino IDE，从 `example/lyttln` 打开示例。

在线源码：[lygion_devs_cpp/example/lyttln](https://github.com/LygionOrganization/lygion_devs_cpp/tree/main/example/lyttln)

## 串口初始化

以下示例使用 ESP32-S3 的 `Serial1`，RX 为 GPIO 5，TX 为 GPIO 4，波特率与 TTL Node (A) 的出厂设置一致：

```cpp
#include <lygion_devs.h>

NodeClass node;

void setup() {
  Serial1.begin(1000000, SERIAL_8N1, 5, 4);
  node.pSerial = &Serial1;
  delay(1000);
}

void loop() {
}
```

!!! note "引脚和串口按主控板修改"
    上述 GPIO 配置适用于文档示例使用的 ESP32-S3 接线。使用其他开发板时，需要根据硬件修改串口和引脚。Arduino Mega 2560 可使用 `Serial1.begin(1000000);`。

## 修改设备 ID

EEPROM 参数写入前需要解锁，写入后应重新锁定。以下示例把 ID `1` 改为 `2`：

```cpp
#include <lygion_devs.h>

NodeClass node;

void setup() {
  Serial1.begin(1000000, SERIAL_8N1, 5, 4);
  node.pSerial = &Serial1;
  delay(1000);

  node.unLockEprom(1);
  node.writeByte(1, LY_NODE_ID, 2);
  delay(200);
  node.LockEprom(2);
}

void loop() {
}
```

!!! warning "锁定时使用新 ID"
    ID 写入成功后，设备地址已经改变，因此 `LockEprom()` 需要传入新 ID。修改参数时只连接一个目标设备最稳妥。

## 读取总线电压

```cpp
void loop() {
  float voltage = node.adcPowVol(0);

  if (!node.getLastError()) {
    Serial.print("voltage: ");
    Serial.println(voltage);
  } else {
    Serial.println("ADC read error");
  }

  delay(100);
}
```

完整示例：`example/lyttln/ttln_adc/ttln_adc.ino`

## 控制 PWM 输出

`pwmCtl(node_id, channel, value)` 的通道为 `1` 或 `2`，数值范围为 `0~1000`。

```cpp
node.pwmCtl(0, 1, 0);     // 通道 1 关闭
node.pwmCtl(0, 2, 500);   // 通道 2 约 50% 占空比
node.pwmCtl(0, 1, 1000);  // 通道 1 为 100% 占空比
```

!!! danger "PWM 负载需要外部供电"
    使用 PWM 输出前，需从 HX-5264-3P 或 PH2.0-3P 接入 9~12.6V 电源，并确认负载电流不超过每路 3A。感性负载还应考虑启动电流和反向电动势。

完整示例：`example/lyttln/ttln_pwm/ttln_pwm.ino`

## 控制 RGB 灯

每个颜色分量范围为 `0~7`。先设置单个通道，再调用 `ledFlush()` 刷新：

```cpp
node.ledSingleCtrl(0, 1, 7, 0, 0);  // RGB1：红色
node.ledSingleCtrl(0, 2, 0, 0, 7);  // RGB2：蓝色
node.ledFlush(0, 2);

delay(1000);

node.ledAllCtrl(0, 2, 0, 0, 0);     // 关闭全部 RGB
```

参数含义：

| 函数 | 说明 |
| --- | --- |
| `ledSingleCtrl(id, channel, r, g, b)` | 设置单组 RGB 数据 |
| `ledFlush(id, count)` | 刷新指定数量的 RGB 通道 |
| `ledAllCtrl(id, count, r, g, b)` | 同时设置多组 RGB |

完整示例：`example/lyttln/ttln_rgb/ttln_rgb.ino`

## 读取 S.BUS

```cpp
void loop() {
  if (node.sbusFlush(0)) {
    Serial.print("status: ");
    Serial.println(node.sbusStatus());

    for (int channel = 1; channel <= node.subsGetNum(); channel++) {
      Serial.print("ch");
      Serial.print(channel);
      Serial.print(": ");
      Serial.println(node.sbusGetch(channel));
    }
  } else {
    Serial.println("S.BUS buffer error");
  }

  delay(100);
}
```

`sbusFlush(id)` 成功后再读取状态和通道值。SDK 当前提供 1~16 通道数据。

完整示例：`example/lyttln/ttln_sbus/ttln_sbus.ino`

## 示例目录

| 示例 | 用途 |
| --- | --- |
| `ttln_eprom` | 修改 ID 等 EEPROM 参数 |
| `ttln_adc` | 读取总线输入电压 |
| `ttln_pwm` | 控制两路 PWM 电源输出 |
| `ttln_rgb` | 控制两组 RGB 灯 |
| `ttln_sbus` | 读取 S.BUS 状态和通道数据 |

## 常见问题

- 无响应：确认代码中的 ID 和波特率与设备一致。
- 能通信但舵机不转：USB 供电不足以驱动舵机，需要外部电源。
- ESP32-S3 无法通信：检查 RX/TX 引脚、单线 TTL 接口电路和共地。
- RGB 设置后不变化：调用 `ledFlush()`，或使用 `ledAllCtrl()`。
- S.BUS 数据无变化：确认接收机已配对，并检查 S.BUS、5V 和 GND 接线。
