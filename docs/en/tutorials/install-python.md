# Install Python

The Lygion Python SDK requires Python 3.8 or later.

## Check the Installed Version

=== "Linux / macOS"

    ```bash
    python3 --version
    ```

=== "Windows"

    ```powershell
    py -3 --version
    python --version
    ```

An output such as `Python 3.10.x` or `Python 3.11.x` confirms that Python is installed.

## Install Python

=== "Ubuntu / Debian"

    ```bash
    sudo apt update
    sudo apt install python3 python3-pip python3-venv git
    ```

=== "macOS"

    Install Python from the official Python website or with Homebrew:

    ```bash
    brew install python git
    ```

=== "Windows"

    Install Python 3 from the official Python website. During installation, enable:

    ```text
    Add python.exe to PATH
    ```

    Reopen PowerShell after installation, then verify it:

    ```powershell
    py -3 --version
    ```

## Create a Virtual Environment

Using a separate virtual environment for each project keeps its dependencies isolated.

=== "Linux / macOS"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

=== "Windows"

    ```powershell
    py -3 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

### PowerShell blocks `Activate.ps1`

Allow locally created scripts for your user account:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then run the activation command again.

### Multiple Python installations

Use the following commands to see which interpreter is selected:

=== "Linux / macOS"

    ```bash
    which python3
    ```

=== "Windows"

    ```powershell
    where python
    where py
    ```
