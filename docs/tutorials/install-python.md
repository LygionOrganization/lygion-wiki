# 安装 Python

Lygion Python SDK 建议使用 Python 3.8 或更高版本。

## 确认是否已经安装

=== "Linux"

    ```bash
    python3 --version
    ```

=== "MacOS"

    ```bash
    python3 --version
    ```

=== "Windows"

    ```powershell
    py -3 --version
    python --version
    ```

如果能看到类似 `Python 3.10.x`、`Python 3.11.x` 的输出，说明 Python 已安装。

## 安装方式

=== "Linux"

    Ubuntu / Debian 通常已经内置 Python。若没有，可使用：

    ```bash
    sudo apt update
    sudo apt install python3 python3-pip python3-venv git
    ```

=== "MacOS"

    推荐使用官方安装包或 Homebrew：

    ```bash
    brew install python git
    ```

    如果没有安装 Homebrew，也可以从 Python 官网下载安装包。

=== "Windows"

    推荐从 Python 官网安装 Python 3。

    安装时请勾选：

    ```text
    Add python.exe to PATH
    ```

    安装完成后重新打开 PowerShell，再运行：

    ```powershell
    py -3 --version
    ```

## 建议使用虚拟环境

=== "Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

=== "MacOS"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

=== "Windows"

    ```powershell
    py -3 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

## 常见问题

### Windows 提示无法运行 Activate.ps1

PowerShell 可能限制了脚本执行。可以先使用：

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

然后重新执行激活命令。

### 系统里有多个 Python

可以使用以下命令确认当前解释器路径：

=== "Linux"

    ```bash
    which python3
    ```

=== "MacOS"

    ```bash
    which python3
    ```

=== "Windows"

    ```powershell
    where python
    where py
    ```
