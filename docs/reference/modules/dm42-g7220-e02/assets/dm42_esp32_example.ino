#include <Arduino.h>
#include <lygion_devs.h>

/*
  DM42-G7220-E02 ESP32 / Arduino 示例

  功能：
  1. 读取 TTL Encoder E02 的绝对位置。
  2. 根据编码器读数同步关节步进电机驱动器当前位置。
  3. 使用角度命令控制关节转到 0°、+45°、-45°、0°。

  使用前请先完成 FD 配置：
  - 编码器 ID 与 ENCODER_ID 保持一致。
  - 关节电机驱动器 ID 与 JOINT_DRIVER_ID 保持一致。
  - 关节电机驱动器运行模式为 0，也就是位置模式。
  - 编码器已完成中位校准，机械中位通常对应编码器读数 2047 或 2048。

  ESP32S3 / ESP32 接线示例：
  - MCU RX GPIO5 -> TTL Adapter (A) RX
  - MCU TX GPIO4 -> TTL Adapter (A) TX
  - MCU GND       -> TTL Adapter (A) GND

  注意：
  - 电机驱动器必须接入外部电源，不能只依赖 USB 供电。
  - 第一次运行前，请固定执行器本体，并确认输出端附近没有障碍物。
*/

TTLSDClass ttlsd;

// TTL Encoder E02 的设备 ID，用于读取关节输出端的绝对角度。
const uint8_t ENCODER_ID = 2;

// 关节步进电机对应的 TTL Stepper Driver (A) 设备 ID。
const uint8_t JOINT_DRIVER_ID = 1;

const int TTL_RX_PIN = 5;
const int TTL_TX_PIN = 4;
const uint32_t DEBUG_BAUD = 115200;
const uint32_t TTL_BAUD = 1000000;

const float PI_VALUE = 3.1415926f;

// DM42-G7220-E02 的传动比：
// 72 / 20 为同步带传动级减速比，5.181818182 为 4240BY-G5.2 电机减速器减速比。
const float RATIO = (72.0f / 20.0f) * 5.181818182f;

// E02 编码器单圈位置范围为 0~4095。
const int ENCODER_ONE_CIRCLE = 4096;

// FD 中位校准后，关节机械中位通常对应编码器读数 2047 或 2048。
// 如果你的设备在机械中位读到的是其它值，请改成实测中位读数。
const int ENCODER_CENTER = 2048;

// TTL Stepper Driver (A) 默认 1/32 微步时，电机轴单圈对应 3200 个位置计数。
const int STEPPER_ONE_CIRCLE = 3200;

// 关节输出端转一圈对应的电机位置计数。
const float JOINT_TOTAL_STEPS = STEPPER_ONE_CIRCLE * RATIO;

// 关节机械中位对应的电机位置值。
const int JOINT_MID = (int)(JOINT_TOTAL_STEPS / 2.0f);

// 程序中 0° 目标角度对应的电机位置。
const int JOINT_ZERO = (int)JOINT_TOTAL_STEPS;

// 关节弧度值到电机位置值的换算系数。
const float RAD2STEPS = JOINT_TOTAL_STEPS / (2.0f * PI_VALUE);

// 编码器每变化 1 个计数，对应的电机位置变化量。
const float ENCODER_TO_STEPS = JOINT_TOTAL_STEPS / ENCODER_ONE_CIRCLE;

// 第一次测试建议使用较低速度和非 0 加速度。
const uint16_t JOINT_SPEED = 400;
const uint8_t JOINT_ACC = 15;

// 相电流参数。
// 相电流(A) 约等于 3.3 * 2 * (current / 1000)。
// current = 200 时，相电流约为 1.32 A。
const uint16_t MOTOR_CURRENT = 200;

bool readPositionSpeed(uint8_t deviceId, int &position, int &speed)
{
  position = ttlsd.ReadPos(deviceId);
  if (ttlsd.getLastError()) {
    Serial.print("Read position failed. ID=");
    Serial.println(deviceId);
    return false;
  }

  speed = ttlsd.ReadSpeed(deviceId);
  if (ttlsd.getLastError()) {
    Serial.print("Read speed failed. ID=");
    Serial.println(deviceId);
    return false;
  }

  return true;
}

bool setPosition(uint8_t deviceId, uint16_t position)
{
  ttlsd.CalibrationOfs(deviceId, position);
  delay(10);

  Serial.print("Position synchronized. ID=");
  Serial.print(deviceId);
  Serial.print(" position=");
  Serial.println(position);
  return true;
}

bool jointInit(uint8_t encoderId, uint8_t driverId)
{
  int encoderPosition = 0;
  int encoderSpeed = 0;
  if (!readPositionSpeed(encoderId, encoderPosition, encoderSpeed)) {
    return false;
  }

  // 编码器已经在 FD 中完成中位校准，这里只计算当前读数相对中位的偏移。
  int encoderDelta = encoderPosition - ENCODER_CENTER;
  long motorPosition = lroundf(JOINT_MID + encoderDelta * ENCODER_TO_STEPS);
  motorPosition = constrain(motorPosition, 0L, 65534L);

  Serial.print("Encoder position=");
  Serial.print(encoderPosition);
  Serial.print(" delta=");
  Serial.print(encoderDelta);
  Serial.print(" -> motor position=");
  Serial.println(motorPosition);

  return setPosition(driverId, (uint16_t)motorPosition);
}

bool jointPositionCtrl(uint8_t deviceId, uint16_t position, uint16_t speed, uint8_t acc, uint16_t current)
{
  ttlsd.WritePosEx(deviceId, position, speed, acc, current);
  if (ttlsd.getLastError()) {
    Serial.print("Write joint position failed. ID=");
    Serial.println(deviceId);
    return false;
  }
  return true;
}

bool jointRadCtrl(uint8_t deviceId, float rad, uint16_t speed, uint8_t acc, uint16_t current)
{
  long position = lroundf(rad * RAD2STEPS + JOINT_ZERO);
  position = constrain(position, 0L, 65534L);

  Serial.print("Joint target position=");
  Serial.println(position);

  return jointPositionCtrl(deviceId, (uint16_t)position, speed, acc, current);
}

bool jointDegCtrl(uint8_t deviceId, float deg, uint16_t speed, uint8_t acc, uint16_t current)
{
  float rad = deg * PI_VALUE / 180.0f;

  Serial.print("Joint target deg=");
  Serial.println(deg);

  return jointRadCtrl(deviceId, rad, speed, acc, current);
}

void runDemoOnce()
{
  Serial.println("DM42-G7220-E02 joint demo start");

  if (!jointInit(ENCODER_ID, JOINT_DRIVER_ID)) {
    Serial.println("Joint init failed. Check encoder ID, wiring, power, and baudrate.");
    return;
  }

  jointDegCtrl(JOINT_DRIVER_ID, 0.0f, JOINT_SPEED, JOINT_ACC, MOTOR_CURRENT);
  delay(1500);

  jointDegCtrl(JOINT_DRIVER_ID, 45.0f, JOINT_SPEED, JOINT_ACC, MOTOR_CURRENT);
  delay(1500);

  jointDegCtrl(JOINT_DRIVER_ID, -45.0f, JOINT_SPEED, JOINT_ACC, MOTOR_CURRENT);
  delay(1500);

  jointDegCtrl(JOINT_DRIVER_ID, 0.0f, JOINT_SPEED, JOINT_ACC, MOTOR_CURRENT);
  Serial.println("DM42-G7220-E02 joint demo finished");
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
  delay(1000);
}
