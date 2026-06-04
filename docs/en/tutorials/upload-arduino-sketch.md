# Upload an Arduino Example

This guide covers building and uploading a Lygion C++ SDK example with Arduino IDE.

## 1. Open a Safe First Example

Open an `.ino` example such as:

```text
example/lyttlsd/FeedBack.ino
```

Start with a feedback or read-only example. Do not begin with a sketch that commands high-speed motor motion.

## 2. Select the Board and Upload Port

Choose your board under **Tools -> Board**, then choose the MCU development board's USB serial port under **Tools -> Port**.

!!! note "This is the MCU upload port"
    It connects the computer to the MCU for uploading and debug output. It is not the TTL bus connection.

## 3. Configure the Hardware UART

ESP32S3 example:

```cpp
Serial.begin(115200);
Serial1.begin(1000000, SERIAL_8N1, 18, 17);
ttlsd.pSerial = &Serial1;
```

Change pins `18` and `17` if your wiring uses different RX and TX pins.

Mega2560 example:

```cpp
Serial.begin(115200);
Serial1.begin(1000000);
ttlsd.pSerial = &Serial1;
```

## 4. Upload and View Output

Click the Upload button. A successful upload reports:

```text
Done uploading.
```

Open **Tools -> Serial Monitor** and set it to `115200`, matching:

```cpp
Serial.begin(115200);
```

Successful communication may print:

```text
Position:1200
Speed:0
```

If you see `FeedBack error`, verify the device ID, 1 Mbps TTL bus rate, RX/TX/GND wiring, external power, and duplicate IDs.
