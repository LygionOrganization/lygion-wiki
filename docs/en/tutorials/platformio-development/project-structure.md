# Understand the Project Structure

## Standard Directories

| Path | Purpose |
| --- | --- |
| `platformio.ini` | Build environments, boards, dependencies, and upload settings |
| `src/` | Application source files |
| `include/` | Shared headers |
| `lib/` | Project-local libraries |
| `data/` | Files uploaded to LittleFS or another device filesystem |
| `test/` | Unit and integration tests |
| `.pio/` | Generated build output; do not edit |

## Program Entry

Arduino-framework projects normally implement `setup()` and `loop()` in `src/main.cpp`. Keep the entry file small and move distinct responsibilities into modules with `.h` and `.cpp` files.

Useful module boundaries include:

- hardware and pin initialization
- actuator and bus communication
- network services
- JSON command parsing
- mission or task execution
- persistent configuration
- safety and fault handling

## Initialization Order

Initialize safety-critical state first, then communications and user features. A typical order is:

1. Put outputs in a safe state.
2. Initialize logging and configuration.
3. Initialize buses and actuators without issuing movement.
4. Start the filesystem and network.
5. Enable commands and automation only after validation.

Avoid long blocking delays in `loop()`. Use state machines, timers, queues, or RTOS tasks when operations must run concurrently.

