# Developing Complex Projects with VS Code and PlatformIO

This tutorial series is for users who need to modify and maintain a complete robot-controller firmware project. It covers opening an existing PlatformIO project, understanding its code and configuration, building and uploading safely, and using Git to manage long-term development.

PlatformIO is a good fit for projects with multiple source files, dependencies, boards, or build environments. Small single-file examples can still be developed with the Arduino IDE.

## What You Will Learn

- Install and verify VS Code, PlatformIO, and Git.
- Open an existing project at the correct directory level.
- Understand `src`, `include`, `lib`, `data`, and `platformio.ini`.
- Manage libraries, build flags, upload ports, partitions, and filesystems.
- Build, upload, and monitor firmware from the GUI or CLI.
- Separate application firmware from filesystem content.
- Split complex firmware into maintainable modules.
- Use branches and commits to preserve reversible changes.
- Diagnose failures from the first meaningful error message.

## Recommended Order

1. [Set Up the Development Environment](setup.md)
2. [Get and Open a Project](open-project.md)
3. [Understand the Project Structure](project-structure.md)
4. [Configure platformio.ini](configuration.md)
5. [Build, Upload, and Debug](build-upload-debug.md)
6. [Manage Dependencies and Data Files](dependencies-and-data.md)
7. [Use a Git Development Workflow](git-workflow.md)
8. [Troubleshooting](troubleshooting.md)

!!! tip "Reproduce before modifying"
    Build the unmodified project first. A known-good baseline makes later failures much easier to attribute.

!!! danger "Robot firmware can move hardware"
    Disconnect or disable external actuators before the first upload and whenever you change initialization or motion-control code.

