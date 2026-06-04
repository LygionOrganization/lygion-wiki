# Product Reference

Use this section after completing a [first communication test](../quickstart/index.md). Each product guide collects the hardware specifications, wiring, software examples, operating notes, and troubleshooting information needed to integrate that product.

## TTL Bus Products

| Product | Purpose | Documentation |
| --- | --- | --- |
| TTL Adapter (A) | Converts USB or an MCU UART into a single-wire TTL bus interface | [Open guide](bus-devices/ttl-adapter-a/index.md) |
| TTL Encoder E02 | 12-bit absolute magnetic angle encoder with TTL bus feedback | [Open guide](bus-devices/ttl-encoder-e02/index.md) |
| TTL Stepper Driver (A) | TTL bus driver for bipolar stepper motors | [Open guide](bus-devices/ttl-stepper-driver-a/index.md) |
| Robot Driver with ESP32S3 Lite | ESP32S3-based robot controller with multiple robot interfaces | [Open guide](bus-devices/robot-driver-with-esp32s3-lite/index.md) |

## Bus Hubs

- [TTL-5264 8P Hub (A)](bus-devices/hub-boards/ttl-5264-8p-hub-a.md)
- [HC-1.25 8P Hub (A)](bus-devices/hub-boards/hc-1.25-8p-hub-a.md)

## Before Integrating a Product

- Start with one device and a read-only example.
- Confirm that the power supply matches every device in the powered group.
- Assign a unique ID to every device on the shared bus.
- Use the [tutorial library](../tutorials/index.md) for common setup and troubleshooting tasks.
