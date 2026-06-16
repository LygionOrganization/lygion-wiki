# Get and Open a Project

## Get the Project

Clone the repository when Git is available:

```bash
git clone <repository-url>
cd <project-directory>
```

Alternatively, download and extract the project ZIP.

## Open the Correct Directory

Open the directory that contains `platformio.ini`:

```bash
code .
```

!!! warning "Do not open only src"
    PlatformIO needs `platformio.ini` and the complete project structure. Opening only `src` prevents normal build and dependency discovery.

## Build the Original Project

Before editing:

```bash
pio run
```

Record the selected environment, framework and platform versions, dependency versions, partition scheme, and any required build flags.

## Create a Development Copy

Create a branch before making changes:

```bash
git switch -c feature/my-change
git status
```

