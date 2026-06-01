# TTL Stepper Driver (A) Python 控制

本页按学习顺序介绍 TTL Stepper Driver (A) 常用 Python 示例。

## 准备工作

先完成：

- [安装 Python](../../../tutorials/install-python.md)
- [查找串口设备](../../../tutorials/find-serial-port.md)
- [运行 Python 脚本](../../../tutorials/run-python-scripts.md)

## 公共初始化结构

```python
import sys
import os
import time

sys.path.append("..")
from lydevs_sdk import *

portHandler = PortHandler('/dev/ttyUSB0')
packetHandler = TTLSDClass(portHandler)

if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    quit()

if portHandler.setBaudRate(1000000):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()
```

请根据系统修改串口名称。

## 1. ping 测试通信

```python
model_number, result, error = packetHandler.ping(1)
```

如果成功，说明串口、波特率和 ID 基本正确。

## 2. 读取位置和速度

```python
position, speed, result, error = packetHandler.ReadPosSpeed(1)
print(position, speed)
```

建议先确认能稳定读取，再运行控制动作。

## 3. 位置控制

```python
packetHandler.WritePosEx(1, 3200, 200, 10, 150)
```

参数含义：

```text
ID = 1
目标位置 = 3200
速度参数 = 200
加速度参数 = 10
电流参数 = 150
```

!!! warning "不要一开始使用过高速度"
    建议第一次测试使用保守参数，例如 `speed=100~200`，`acc=10~50`。

## 4. 边运动边读取状态

```python
packetHandler.WritePosEx(1, 3200, 200, 10, 150)

while True:
    position, speed, result, error = packetHandler.ReadPosSpeed(1)
    moving, result, error = packetHandler.ReadMoving(1)
    print(position, speed, moving)
    if moving == 0:
        break
    time.sleep(0.05)
```

## 5. 速度模式

```python
packetHandler.WheelMode(1)
packetHandler.WriteSpec(1, 100, 10, 150)
time.sleep(2)
packetHandler.WriteSpec(1, 0, 10, 150)
```

速度可以为正数、负数或 0。

## 6. 同步读取多个设备

```python
groupSyncRead = GroupSyncRead(packetHandler, LY_TTLSD_PRESENT_POSITION_L, 4)

for scs_id in [1, 2, 3]:
    groupSyncRead.addParam(scs_id)

groupSyncRead.txRxPacket()

groupSyncRead.clearParam()
```

只添加真实存在的 ID。

## 7. 同步写入多个设备

```python
for scs_id in [1, 2, 3]:
    packetHandler.SyncWritePosEx(scs_id, 3200, 200, 10, 150)

packetHandler.groupSyncWrite.txPacket()
packetHandler.groupSyncWrite.clearParam()
```

适合多关节同时启动、多滑台同步运动等场景。

## 8. 设置当前位置基准

```python
packetHandler.reOfsCal(1, 0)
```

该操作可将当前实际位置设置为指定位置值。

!!! note "掉电保存说明"
    对 TTL Stepper Driver (A)，当前位置基准设置通常用于应用层初始化流程。实际是否掉电保存请以具体固件版本说明为准。
