# 获取并打开项目

复杂项目通常已经包含正确的开发板、依赖、分区和构建配置。优先打开厂商或团队提供的完整工程，不要先创建空工程再复制几个源文件。

## 获取项目

=== "Windows"

    使用 Git：

    ```powershell
    git clone <项目仓库地址>
    cd <项目目录>
    code .
    ```

    无法使用 Git 时，也可下载 ZIP。解压到普通目录后再打开，不要直接在压缩包内编辑。

=== "macOS"

    ```bash
    git clone <项目仓库地址>
    cd <项目目录>
    code .
    ```

=== "Linux"

    ```bash
    git clone <项目仓库地址>
    cd <项目目录>
    code .
    ```

GitHub 账号不是克隆公开仓库的必要条件。

## 打开正确目录

选择 VS Code 的 `File → Open Folder`，打开包含以下文件的目录：

```text
platformio.ini
src/
include/
lib/
```

!!! warning "不要只打开 src"
    如果 VS Code 顶层看不到 `platformio.ini`，PlatformIO 无法读取开发板、依赖和构建参数。

## 信任项目

VS Code 可能询问是否信任文件作者。只有当项目来源可靠、你已确认仓库地址时才选择信任。未知项目中的构建脚本可能在电脑上执行命令。

## 第一次构建

打开项目后先不要修改代码：

1. 等待 PlatformIO 下载开发平台和依赖。
2. 点击状态栏的编译按钮。
3. 等待终端出现 `SUCCESS`。
4. 保存完整错误输出，若失败先解决环境问题。

终端方式：

```bash
pio run
```

多环境项目应指定目标：

```bash
pio run -e <环境名>
```

环境名来自 `platformio.ini` 中的 `[env:名称]`。

## 建立自己的开发副本

推荐在修改前新建分支：

```bash
git switch -c feature/my-customization
```

如果项目不是 Git 仓库，也可以先复制一份完整目录，但不要只复制 `src`，否则会遗漏依赖和配置。

## 记录原始状态

首次构建成功后记录：

- 使用的环境名
- PlatformIO 输出的开发板和平台版本
- Flash 与 RAM 占用
- 上传端口
- 串口监视器波特率
- 固件正常启动时的日志

这些信息是后续排查回归问题的基准。
