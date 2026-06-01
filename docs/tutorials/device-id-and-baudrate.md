# 设备 ID 与波特率

TTL 总线是多设备总线。多个设备可以接在同一根总线上，但必须满足两个条件：

1. 所有设备 ID 不重复。
2. 通信波特率一致。

## 默认设置

常见默认设置：

| 项目 | 默认值 |
| --- | --- |
| 设备 ID | `1` |
| 波特率 | `1000000` |

不同批次或不同产品可能存在差异，实际以产品页面和出厂设置为准。

## 为什么不能重复 ID

如果两个设备使用相同 ID，它们会同时响应同一条指令，导致：

- 读取失败
- 返回数据异常
- 多个设备同时运动
- 通信不稳定

## 新设备改 ID 的安全流程

```text
1. 总线上只连接一个新设备
2. 使用 FD 软件或 SDK 修改 ID
3. 修改后重新 ping 新 ID
4. 断开设备，连接下一个新设备
5. 所有设备都设置为不同 ID 后，再一起接入总线
```

## 使用 FD 软件修改

Windows 用户通常可以使用 FD 调试软件扫描设备、修改 ID 和波特率。

请参考：[FD 调试软件](fd-tool.md)。

## 使用 SDK 修改

部分产品支持通过 SDK 修改 ID，例如：

### Python SDK

[lygion_devs_py/lyttlsd/ttlsd_eprom.py](https://github.com/LygionOrganization/lygion_devs_py/blob/main/lyttlsd/ttlsd_eprom.py)

```python
# 打开 EPROM 保存功能，参数 254 是广播 ID
packetHandler.unLockEprom(1)

# 参数 2 是你要更改的新 ID
packetHandler.SetID(254, 1)

# 关闭 EPROM 保存功能，因为刚刚设备的 ID 已经被改为了 1
# 所以这里关闭 EPROM 保存功能要输入新的 ID 1
packetHandler.unLockEprom(1)
```

### C++ SDK

[lygion_devs_cpp/lyttlsd/ProgramEprom](https://github.com/LygionOrganization/lygion_devs_cpp/blob/main/example/lyttlsd/ProgramEprom/ProgramEprom.ino)

```cpp
// 打开 EPROM 保存功能，参数 254 是广播 ID
hlscl.unLockEprom(254);

// 参数 2 是你要更改的新 ID
hlscl.writeByte(254, HLSCL_ID, 1);

// 关闭 EPROM 保存功能，因为刚刚设备的 ID 已经被改为了 1
// 所以这里关闭 EPROM 保存功能要输入新的 ID 1
hlscl.LockEprom(1);
```

!!! warning "修改 ID 前只连接一个目标设备"
    使用广播 ID 或默认 ID 修改设备参数时，请确认总线上只有一个目标设备，否则可能误改多个设备。

## 波特率不一致怎么办

如果代码使用 `1000000`，但设备已经被改成其它波特率，就会通信失败。解决方法：

1. 使用 FD 软件尝试扫描常见波特率。
2. 在代码中改成设备当前波特率。
3. 必要时恢复出厂设置。
