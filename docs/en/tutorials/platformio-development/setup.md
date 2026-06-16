# Set Up the Development Environment

Install VS Code and the PlatformIO IDE extension. Git is not required to compile firmware, but it is strongly recommended.

## Install VS Code

Install VS Code for your operating system, then verify the command-line launcher:

```bash
code --version
```

On macOS, run `Shell Command: Install 'code' command in PATH` from the VS Code command palette if needed.

## Install PlatformIO IDE

1. Open the Extensions view in VS Code.
2. Search for `PlatformIO IDE` and verify the publisher.
3. Install the extension and restart VS Code.
4. Wait for PlatformIO Core initialization to finish.
5. Confirm that the PlatformIO icon and build/upload status-bar buttons appear.

The first installation and first build may download a Python environment, toolchains, development platforms, and libraries.

## Install Git

Install Git for your operating system and verify it:

```bash
git --version
```

Before your first commit, configure your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Verify PlatformIO Core

Open a terminal from PlatformIO and run:

```bash
pio --version
```

If `pio` is unavailable in a normal system terminal, use the PlatformIO terminal or the VS Code status-bar commands.

