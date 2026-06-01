# TTL Encoder E02 Python 读取

TTL Encoder E02 与 TTL Stepper Driver (A) 复用了部分 SDK 接口。对于编码器，主要使用位置读取、速度读取、同步读取和基准设置功能。

## 准备工作

先完成：

- [安装 Python](../../../tutorials/install-python.md)
- [查找串口设备](../../../tutorials/find-serial-port.md)
- [运行 Python 脚本](../../../tutorials/run-python-scripts.md)

## 通用初始化结构

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

请把 `/dev/ttyUSB0` 改成你的实际串口。

## 读取单个编码器

示例：读取 ID 1 的位置和速度。

```python
while True:
    position, speed, result, error = packetHandler.ReadPosSpeed(1)
    if result != COMM_SUCCESS:
        print(packetHandler.getTxRxResult(result))
    else:
        angle_deg = position / 4096.0 * 360.0
        print(f"pos={position}, angle={angle_deg:.2f} deg, speed={speed}")
    time.sleep(0.1)
```

位置单位为 steps。12bit 精度下：

```text
一圈 = 4096 steps
```

速度单位为：

```text
steps/s
```

角速度换算：

```python
speed_deg_s = speed / 4096.0 * 360.0
```

## 同步读取多个编码器

如果你有 ID 1、2、3 三个编码器：

```python
groupSyncRead = GroupSyncRead(packetHandler, LY_TTLSD_PRESENT_POSITION_L, 4)

for scs_id in [1, 2, 3]:
    groupSyncRead.addParam(scs_id)

result = groupSyncRead.txRxPacket()

for scs_id in [1, 2, 3]:
    available, error = groupSyncRead.isAvailable(scs_id, LY_TTLSD_PRESENT_POSITION_L, 4)
    if available:
        position = groupSyncRead.getData(scs_id, LY_TTLSD_PRESENT_POSITION_L, 2)
        speed = groupSyncRead.getData(scs_id, LY_TTLSD_PRESENT_POSITION_L + 2, 2)
        print(scs_id, position, speed)

groupSyncRead.clearParam()
```

!!! warning "只添加真实存在的 ID"
    如果代码中添加了未连接的 ID，可能导致同步读取失败或等待超时。

## 设置当前位置基准

将 ID 1 编码器当前位置设置为 1024：

```python
result, error = packetHandler.reOfsCal(1, 1024)
```

在 12bit 模式下：

```text
1024 = 90°
2048 = 180°
3072 = 270°
```

换算公式：

```
position = angle_deg * 4096 / 360
```

校准结果会掉电保存。
