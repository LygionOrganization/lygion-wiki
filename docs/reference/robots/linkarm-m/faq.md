# 故障排查

## 找不到串口

1. 确认连接的是 TTL Node (A) 的 Type-C 数据接口。
2. 更换支持数据传输的 USB 线。
3. 重新插拔后列出串口。

=== "Windows"

    ```powershell
    python -m serial.tools.list_ports
    ```

=== "macOS / Linux"

    ```bash
    python3 -m serial.tools.list_ports
    ```

仍无法识别时，检查系统驱动和[串口查找教程](../../../tutorials/find-serial-port.md)。

## Linux 提示 Permission denied

```bash
sudo usermod -aG dialout "$USER"
```

注销并重新登录后再试。部分发行版使用的串口用户组不同，可通过 `ls -l /dev/ttyUSB0` 查看设备所属组。

## 串口存在但机械臂无响应

依次检查：

- 动力电源是否为约 12V 且供电能力不低于 3A
- `default_device_serial_ports` 是否为当前端口
- `serial_baudrate` 是否为 `500000`
- 舵机 ID 是否为 `31`、`32`、`33`、`34`
- TTL Node (A) ID 是否为 `40`
- 是否有其他程序占用串口

关闭串口监视器、其他 Python 程序或上位机软件后重试。

## 机械臂姿态明显不正确

立即停止动作并断开动力电源，核对：

- `servo_middle` 是否与当前设备贴纸完全一致
- 四个数值的顺序是否改变
- `joint_direction` 是否被误改
- 舵机或连杆是否重新安装过

不要用修改目标角度的方法补偿错误中位。

## 返回 IK_FAILED

常见原因：

- 目标点超出机械臂工作空间
- 笛卡尔坐标没有使用毫米（mm）
- `servo_middle` 或连杆参数错误
- 目标姿态违反关节限位

LinkArm-M 的 CLI 与 Python API 均使用毫米（mm）。先读取当前 FK，再从当前位置附近的小幅目标开始测试。

## 动作没有到位

- 使用 `--reliable` 或 Python API 的 `reliable=True`
- 检查负载是否过大
- 检查扭矩限制是否过低
- 检查电源是否压降
- 确认关节没有碰到机械限位

可靠模式只能等待和判断到位，不能消除过载、碰撞或错误配置。

## 配置文件没有生效

SDK 通常按以下顺序寻找配置：

1. 命令行 `--config` 指定的文件
2. 当前工作目录中的 `arm_config.json`
3. SDK 目录中的 `arm_config.json`

多份同名配置容易造成误判。部署时建议始终显式指定配置路径。

## JSON 配置报错

检查：

- 是否使用英文双引号
- 最后一项后是否多了逗号
- 是否写入注释
- 数组括号和对象括号是否成对

可使用 Python 快速验证：

```bash
python -m json.tool arm_config.json
```

## 安装依赖失败

=== "Windows"

    ```powershell
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    ```

=== "macOS / Linux"

    ```bash
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    ```

建议在虚拟环境中安装，并使用 Python 3.8 或更高版本。

## 升级 SDK 后命令不同

先查看当前版本帮助：

```bash
python linkarm.py --help
python linkarm.py <command> --help
```

项目 README 与源码属于最终依据。生产项目升级前，应锁定依赖版本并重新完成状态读取、小幅动作、IK/FK 和异常停机测试。
