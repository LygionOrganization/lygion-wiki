#include <Arduino.h>
#include <lygion_devs.h>

/*
  SW69-TTL ESP32 / Arduino 示例

  功能：
  1. 读取 TTL Encoder E02 的绝对位置。
  2. 将转向电机驱动器当前位置同步到编码器对应位置。
  3. 使用角度命令控制转向关节。
  4. 使用速度模式控制行走电机。

  使用前请先完成文档中的 FD 配置：
  - 编码器 ID = 10
  - 转向电机驱动器 ID = 11，位置模式
  - 行走电机驱动器 ID = 12，速度模式，建议开启心跳保护

  ESP32S3 / ESP32 接线示例：
  - MCU RX GPIO5 -> TTL Adapter (A) RX
  - MCU TX GPIO4 -> TTL Adapter (A) TX
  - MCU GND       -> TTL Adapter (A) GND
*/

TTLSDClass ttlsd;

const uint8_t ENCODER_ID = 10;
const uint8_t TURNING_ID = 11;
const uint8_t WALKING_ID = 12;

const int TTL_RX_PIN = 5;
const int TTL_TX_PIN = 4;
const uint32_t DEBUG_BAUD = 115200;
const uint32_t TTL_BAUD = 1000000;

const float PI_VALUE = 3.1415926f;
const float RATIO = (72.0f / 20.0f) * 5.181818182f;
const int ENCODER_ONE_CIRCLE = 4096;
// FD 中位校准后，转向机械中位通常对应编码器读数 2047 或 2048。
// 如果你的设备在机械中位读到的是其它值，请改成实测中位读数。
const int ENCODER_CENTER = 2048;
const int STEPPER_ONE_CIRCLE = 3200;
const float JOINT_TOTAL_STEPS = STEPPER_ONE_CIRCLE * RATIO;
const int JOINT_MID = (int)(JOINT_TOTAL_STEPS / 2.0f);
// 程序中 0° 转向目标对应的电机位置。
const int STEERING_ZERO = (int)JOINT_TOTAL_STEPS;
const float RAD2STEPS = JOINT_TOTAL_STEPS / (2.0f * PI_VALUE);
const float ENCODER_TO_STEPS = JOINT_TOTAL_STEPS / ENCODER_ONE_CIRCLE;

const uint16_t TURNING_SPEED = 400;
const uint8_t TURNING_ACC = 15;
const uint16_t MOTOR_CURRENT = 200;
const uint8_t WALKING_ACC = 15;

const uint32_t WALKING_COMMAND_PERIOD_MS = 100;

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

  Serial.print("Offset calibration succeeded. ID=");
  Serial.print(deviceId);
  Serial.print(" position=");
  Serial.println(position);
  return true;
}

bool servoPositionCtrl(uint8_t deviceId, uint16_t position, uint16_t speed, uint8_t acc, uint16_t current)
{
  ttlsd.WritePosEx(deviceId, position, speed, acc, current);
  if (ttlsd.getLastError()) {
    Serial.print("Write position failed. ID=");
    Serial.println(deviceId);
    return false;
  }
  return true;
}

bool jointInit(uint8_t encoderId, uint8_t turningId)
{
  int encoderPosition = 0;
  int encoderSpeed = 0;
  if (!readPositionSpeed(encoderId, encoderPosition, encoderSpeed)) {
    return false;
  }

  // 编码器已经用 FD 做过中位校准，所以这里只需要计算当前读数相对中位的偏移。
  int encoderDelta = encoderPosition - ENCODER_CENTER;
  long motorPosition = lroundf(JOINT_MID + encoderDelta * ENCODER_TO_STEPS);
  motorPosition = constrain(motorPosition, 0L, 65534L);

  Serial.print("Encoder position=");
  Serial.print(encoderPosition);
  Serial.print(" delta=");
  Serial.print(encoderDelta);
  Serial.print(" -> motor position=");
  Serial.println(motorPosition);

  return setPosition(turningId, (uint16_t)motorPosition);
}

bool jointRadCtrl(uint8_t deviceId, float rad, uint16_t speed, uint8_t acc, uint16_t current)
{
  long position = lroundf(rad * RAD2STEPS + STEERING_ZERO);
  position = constrain(position, 0L, 65534L);

  Serial.print("Steering target position=");
  Serial.println(position);

  return servoPositionCtrl(deviceId, (uint16_t)position, speed, acc, current);
}

bool jointDegCtrl(uint8_t deviceId, float deg, uint16_t speed, uint8_t acc, uint16_t current)
{
  float rad = deg * PI_VALUE / 180.0f;

  Serial.print("Steering target deg=");
  Serial.println(deg);

  return jointRadCtrl(deviceId, rad, speed, acc, current);
}

bool walkingMotorCtrl(uint8_t deviceId, int16_t speed, uint8_t acc, uint16_t current)
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
    walkingMotorCtrl(WALKING_ID, speed, WALKING_ACC, MOTOR_CURRENT);
    delay(WALKING_COMMAND_PERIOD_MS);
  }

  walkingMotorCtrl(WALKING_ID, 0, WALKING_ACC, MOTOR_CURRENT);
}

void runDemoOnce()
{
  Serial.println("SW69-TTL ESP32 demo start");

  if (!jointInit(ENCODER_ID, TURNING_ID)) {
    Serial.println("Joint init failed. Check encoder ID, wiring, power, and baudrate.");
    return;
  }

  jointDegCtrl(TURNING_ID, 0.0f, TURNING_SPEED, TURNING_ACC, MOTOR_CURRENT);
  delay(1500);

  jointDegCtrl(TURNING_ID, 45.0f, TURNING_SPEED, TURNING_ACC, MOTOR_CURRENT);
  delay(1500);

  jointDegCtrl(TURNING_ID, -45.0f, TURNING_SPEED, TURNING_ACC, MOTOR_CURRENT);
  delay(1500);

  jointDegCtrl(TURNING_ID, 0.0f, TURNING_SPEED, TURNING_ACC, MOTOR_CURRENT);
  delay(1000);

  Serial.println("Lift the drive wheel before running the wheel test.");
  delay(1000);

  driveWheelFor(50, 1500);
  delay(500);

  driveWheelFor(-50, 1500);
  delay(500);

  walkingMotorCtrl(WALKING_ID, 0, WALKING_ACC, MOTOR_CURRENT);
  Serial.println("SW69-TTL ESP32 demo finished");
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
  walkingMotorCtrl(WALKING_ID, 0, WALKING_ACC, MOTOR_CURRENT);
  delay(1000);
}
