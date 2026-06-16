# Python SDK 开发

完成[快速开始](quickstart.md)并验证 CLI 后，即可在自己的 Python 项目中使用 `RobotController`。

## 最小示例

在 SDK 仓库目录中新建 `demo.py`：

```python
from linkarm import RobotController


robot = RobotController()

success, joints, xyz = robot.get_current_position()
if not success:
    raise RuntimeError("无法读取机械臂状态，请检查串口和供电")

print("关节角：", joints)
print("末端坐标（mm）：", xyz)

# 首次运行只做小幅、单关节动作
robot.set_joint_angle(3, -0.5, reliable=True)
robot.set_gripper_angle(-1)
```

=== "Windows"

    ```powershell
    .\venv\Scripts\activate
    python demo.py
    ```

=== "macOS / Linux"

    ```bash
    source venv/bin/activate
    python3 demo.py
    ```

!!! warning "以安装版本的接口为准"
    SDK 仍在迭代。官方 README 展示的是 `RobotController` 高层接口，仓库后续版本可能增加同步运动等新方法。升级后应先阅读该版本 README 和源码中的函数签名。

## 关节与夹爪控制

```python
# 夹爪角度
robot.set_gripper_angle(-1)

# 单关节，索引与角度均按当前 SDK 约定
robot.set_joint_angle(3, -0.5)

# 等待到位
robot.set_joint_angle(3, -0.5, reliable=True)

# 四个关节同时运动
robot.set_joints_angle([0.0, -0.3, 0.5, 0.0], reliable=True)
```

角度使用弧度。不要在未核对 `joint_limit` 的情况下传入大角度。

## 读取当前姿态

```python
success, joints, xyz = robot.get_current_position()

if success:
    print(f"joints={joints}")
    print(f"xyz={xyz}")
else:
    print("读取失败")
```

调用失败时不要继续执行依赖当前位置的动作序列。

## 坐标系定义

LinkArm-M 使用下图所示的基座坐标系，原点和 X/Y/Z 正方向以图中箭头为准：

![LinkArm-M 坐标系定义](assets/B.png){ .img-rounded }

- 笛卡尔坐标单位为毫米（mm）。
- 输入 IK 目标前，应先根据机械臂安装方向确认坐标轴。
- 安装在移动底盘、桌面或其他支架上时，机械臂自身坐标系不会随上层应用的地图坐标系自动转换。

如果上层程序使用相机坐标系、底盘坐标系或世界坐标系，需要在调用 SDK 前完成坐标变换。

## 逆运动学

LinkArm-M 的 Python 控制接口使用毫米（mm）表示笛卡尔坐标和距离。

```python
target = robot.inverse_kinematics(250, 0, 60)

if target is None:
    print("目标不可达")
else:
    print("关节解：", target)
    robot.set_joints_angle(target, reliable=True)
```

其中目标坐标为 `[250 mm, 0 mm, 60 mm]`。需要所有可用解时：

```python
solutions = robot.inverse_kinematics(
    250,
    0,
    60,
    return_all=True,
)
```

选择逆解时还应考虑关节限位、当前姿态、线缆方向和障碍物；数学上可达不代表机械环境中一定安全。

## 正运动学

```python
xyz = robot.forward_kinematics([0.0, -0.3, 0.5, 0.0])
print("末端坐标（mm）：", xyz)
```

FK 返回的末端坐标单位为毫米（mm）。计算依赖 `servo_middle`、`joint_direction` 和连杆参数；若结果与实际姿态偏差明显，应先检查配置，不要用软件偏移量掩盖错误中位。

## 可靠动作序列

```python
poses = [
    [0.0, -0.2, 0.4, 0.0],
    [0.2, -0.3, 0.5, -0.1],
    [0.0, 0.0, 0.0, 0.0],
]

for pose in poses:
    robot.set_joints_angle(pose, reliable=True)
```

复杂项目还应增加：

- 每一步的超时和异常处理
- 用户停止或急停入口
- 目标范围检查
- 串口断开后的安全退出
- 日志与动作编号

## 项目组织建议

```text
my_linkarm_project/
├─ arm_config.json
├─ main.py
├─ motions/
│  └─ demo.py
└─ requirements.txt
```

将设备配置与业务代码分开。多台机械臂应使用不同配置文件，参见[多机械臂与 AI 集成](multi-arm-and-ai.md)。
