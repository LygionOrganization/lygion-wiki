# Open a Terminal, PowerShell, or Command Prompt

Many Wiki instructions ask you to enter a command such as:

```bash
python3 --version
```

Enter these commands in your operating system's command-line application.

| Operating system | Recommended command-line application |
| --- | --- |
| Linux | Terminal |
| macOS | Terminal |
| Windows | Windows Terminal or PowerShell |

## Linux

Press `Ctrl + Alt + T` on most desktop Linux systems, or search the application menu for `Terminal`.

A typical prompt looks like:

```text
user@computer:~$
```

Type the command after the `$` prompt.

## macOS

Press `Command + Space`, search for `Terminal`, and press Enter. You can also open `Applications -> Utilities -> Terminal`.

A typical prompt looks like:

```text
user@MacBook ~ %
```

Type the command after the `%` prompt.

## Windows

PowerShell is recommended for the commands in this Wiki.

- Right-click the Start menu and choose **Terminal** or **Windows PowerShell**.
- To open Command Prompt, press `Win + R`, enter `cmd`, and press Enter.
- To open a terminal in a specific folder, right-click an empty area in that folder and choose **Open in Terminal**.

## Entering Commands Correctly

=== "Linux / macOS"

    ```bash
    python3 --version
    ```

=== "Windows PowerShell"

    ```powershell
    py -3 --version
    ```

Do not enter commands in a browser address bar, a source-code file, or the Python interactive prompt.

## Common Questions

### Do I type the `$`, `%`, or `>` shown in an example?

No. Those characters represent the terminal prompt. Enter only the command that follows them.

### Which directory should I use?

Change to the directory containing the SDK or project before running an example. For an SDK extracted to your desktop:

=== "Linux / macOS"

    ```bash
    cd ~/Desktop/lygion_devs_py
    ```

=== "Windows"

    ```powershell
    cd $env:USERPROFILE\Desktop\lygion_devs_py
    ```
