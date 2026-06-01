# 常见通信问题排查

本页用于排查 TTL 总线设备无法通信、读取失败或脚本无法打开端口的问题。

## 先判断是哪一类问题

| 现象 | 优先检查 |
| --- | --- |
| 系统看不到串口 | USB 线、驱动、USB 口、Hub |
| Python 无法打开串口 | 串口名称、权限、端口占用 |
| 能打开串口但 ping 失败 | ID、波特率、供电、线序 |
| 能 ping 但设备不动作 | 外部电源、运行模式、电流、限位、Torque |
| 同步读取失败 | 添加了不存在的 ID、重复 ID、总线过长、供电不足 |

## 1. 系统是否识别串口

先看：[查找串口设备](find-serial-port.md)。

如果完全看不到串口：

- 更换 USB 数据线。
- 更换 USB 口。
- 避免使用质量较差的 USB Hub。
- 安装 CH343 / CH34X 驱动。

## 2. 串口名称是否写对

脚本中的端口必须和系统实际识别到的端口一致。

```python
portHandler = PortHandler('COM3')
```

Windows 下不要写成 `/dev/ttyUSB0`；Linux 下不要写成 `COM3`。

## 3. 波特率是否一致

代码中的波特率：

```python
portHandler.setBaudRate(1000000)
```

必须与设备实际波特率一致。

## 4. ID 是否正确

如果设备 ID 是 2，但代码读取 ID 1，就会失败：

```python
packetHandler.ReadPosSpeed(1)
```

请修改为实际 ID，或使用 FD 软件扫描。

## 5. 供电是否正常

仅 USB 供电可能不足以驱动执行器。步进驱动器、总线舵机、轮式模块等请接入外部电源。

## 6. 是否有重复 ID

多个默认 ID 为 1 的设备同时接入总线，会导致通信冲突。新设备改 ID 时，应一次只连接一个。

## 7. 同步读取是否添加了不存在的 ID

如果总线上只有 ID 1、2、3，不要读取 1~10。

```python
for scs_id in range(1, 4):
    groupSyncRead.addParam(scs_id)
```

## 8. 仍然失败时的最小化测试

建议回到最小系统：

```text
电脑 + USB 线 + TTL Adapter (A) + 单个 TTL 设备 + 合适电源
```

先运行 `ping` 或 `read`。最小系统成功后，再逐步增加 Hub、延长线和其它设备。
