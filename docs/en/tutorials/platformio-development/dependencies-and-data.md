# Manage Dependencies and Data Files

## Libraries

Declare external libraries in `lib_deps` and put project-owned libraries in `lib/`. Do not edit generated copies under `.pio/libdeps`; those changes are discarded.

When dependencies conflict:

1. Identify which header and library version PlatformIO selected.
2. Pin compatible versions in `platformio.ini`.
3. Remove obsolete duplicate libraries.
4. Clean and rebuild the project.

## The data Directory

Web pages, JSON defaults, certificates, and other runtime assets commonly live in `data/`.

!!! warning "Uploading firmware does not upload the filesystem"
    Program flash and filesystem images are separate. After changing `data/`, run the filesystem upload target required by the project, such as `uploadfs`.

```bash
pio run -t uploadfs
```

Back up device configuration before replacing a filesystem image. Keep passwords and production secrets out of the repository.

