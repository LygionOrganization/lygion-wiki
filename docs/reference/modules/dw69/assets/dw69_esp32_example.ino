#include <Arduino.h>
#include <lygion_devs.h>

/*
  DW69 ESP32 / Arduino 示例

  功能：
  1. 通过 TTL Stepper Driver (A) 的速度模式控制 DW69 驱动轮。
  2. 演示低速正转、停止、低速反转、停止。
  3. 周期性发送速度指令，适配 FD 中配置的心跳保护。

  使用前请先完成 FD 配置：
  - 驱动器 ID 与 WHEEL_DRIVER_ID 保持一致。
  - 运行模式设置为 1，也就是速度模式。
  - 建议开启心跳保护，例如心跳保护时间设置为 20，约等于 2 s。

  ESP32S3 / ESP32 接线示例：
  - MCU RX GPIO5 -> TTL Adapter (A) RX
  - MCU TX GPIO4 -> TTL Adapter (A) TX
  - MCU GND       -> TTL Adapter (A) GND

  注意：
  - 电机驱动器必须接入外部电源，不能只依赖 USB 供电。
  - 第一次运行前，请将车轮抬离桌面或地面。
*/

TTLSDClass ttlsd;

// DW69 对应的 TTL Stepper Driver (A) 设备 ID。
// 如果总线上只有一个驱动器，可保持默认 ID 1；如果有多个设备，请改成 FD 中配置的实际 ID。
const uint8_t WHEEL_DRIVER_ID = 1;

const int TTL_RX_PIN = 5;
const int TTL_TX_PIN = 4;
const uint32_t DEBUG_BAUD = 115200;
const uint32_t TTL_BAUD = 1000000;

// 第一次测试建议使用较低速度。
// 速度为正数时电机向一个方向旋转，速度为负数时反向旋转，速度为 0 时停止。
const int16_t TEST_SPEED = 50;

// 加速度参数不建议在调试时设置为 0。
// 0 表示接近最高加速度，可能造成启动冲击、抖动或失步。
const uint8_t WHEEL_ACC = 15;

// 相电流参数。
// 相电流(A) 约等于 3.3 * 2 * (current / 1000)。
// current = 200 时，相电流约为 1.32 A。
const uint16_t MOTOR_CURRENT = 200;

// 如果在 FD 中开启了心跳保护，程序需要周期性发送速度指令。
// 这里使用 100 ms 周期，远小于 2 s 心跳保护时间。
const uint32_t COMMAND_PERIOD_MS = 100;

bool wheelSpeedCtrl(uint8_t deviceId, int16_t speed, uint8_t acc, uint16_t current)
{
  ttlsd.WriteSpe(deviceId, speed, acc, current);
  if (ttlsd.getLastError()) {
    Serial.print("Write wheel speed failed. ID=");
    Serial.println(deviceId);
    return false;
  }
  return true;
}

void driveWheelFor(int16_t speed, uint32_t durationMs)
{
  Serial.print("Wheel speed=");
  Serial.print(speed);
  Serial.print(" durationMs=");
  Serial.println(durationMs);

  uint32_t startMs = millis();
  while (millis() - startMs < durationMs) {
    if (!wheelSpeedCtrl(WHEEL_DRIVER_ID, speed, WHEEL_ACC, MOTOR_CURRENT)) {
      break;
    }
    delay(COMMAND_PERIOD_MS);
  }

  wheelSpeedCtrl(WHEEL_DRIVER_ID, 0, WHEEL_ACC, MOTOR_CURRENT);
}

void runDemoOnce()
{
  Serial.println("DW69 wheel demo start");
  Serial.println("Lift the wheel before running the test.");
  delay(1000);

  // 低速正转 1.5 s。
  driveWheelFor(TEST_SPEED, 1500);
  delay(500);

  // 低速反转 1.5 s。
  driveWheelFor(-TEST_SPEED, 1500);
  delay(500);

  // 明确发送停止指令。
  wheelSpeedCtrl(WHEEL_DRIVER_ID, 0, WHEEL_ACC, MOTOR_CURRENT);
  Serial.println("DW69 wheel demo finished");
}

void setup()
{
  Serial.begin(DEBUG_BAUD);
  delay(1000);

  Serial1.begin(TTL_BAUD, SERIAL_8N1, TTL_RX_PIN, TTL_TX_PIN);
  ttlsd.pSerial = &Serial1;
  delay(1000);

  runDemoOnce();
}

void loop()
{
  // 保持停止指令，避免调试时车轮意外继续转动。
  wheelSpeedCtrl(WHEEL_DRIVER_ID, 0, WHEEL_ACC, MOTOR_CURRENT);
  delay(1000);
}
