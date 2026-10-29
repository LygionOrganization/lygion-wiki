"""Lyo-D42 USB CDC client. pip install pyserial. No movement is issued by the CLI.

python python_example/lyo_d42_client.py COM7
Motion is explicit: with client.armed(): client.twist(.03, 0)
The context sends heartbeat and always requests stop on exit.
"""
import argparse
import contextlib
import json
import threading
import time

class LyoD42Client:
    def __init__(self, port):
        import serial
        self.serial = serial.Serial(port, 115200, timeout=0.1, write_timeout=0.3)
        self._write_lock = threading.Lock()
        self._request_lock = threading.Lock()
        self._rid = 0

    def send(self, command):
        payload = json.dumps(command, separators=(',', ':'), allow_nan=False).encode('utf-8')
        if len(payload) > 255:
            raise ValueError('Command exceeds 255 bytes')
        with self._write_lock:
            self.serial.write(payload + b'\n')

    def request(self, command, timeout=2):
        # Serial responses can include telemetry and log lines. Never retry writes.
        with self._request_lock:
            self._rid = (self._rid + 1) & 0x7fffffff
            rid = self._rid
            self.send({**command, 'rid': rid, 'reliable': True})
            deadline = time.monotonic() + timeout
            while time.monotonic() < deadline:
                line = self.serial.readline(8192)
                try:
                    result = json.loads(line)
                except (ValueError, UnicodeDecodeError):
                    continue
                if not isinstance(result, dict) or result.get('rid') != rid:
                    continue
                if not result.get('ok'):
                    raise RuntimeError(result.get('error', 'command rejected'))
                return result
            raise TimeoutError('No matching result; check current state before retrying')

    def twist(self, v, w):
        self.send({'T': 804, 'v': v, 'w': w})

    def status(self):
        return self.request({'T': 808})

    def stop(self):
        self.send({'T': 800})  # Reception is not a mechanical-stop acknowledgement.

    @contextlib.contextmanager
    def armed(self):
        done = threading.Event()
        self.request({'T': 801, 'enable': True})
        def heartbeat():
            while not done.wait(.1):
                try:
                    self.send({'T': 810})
                except Exception:
                    done.set()  # Firmware deadman stops after its configured timeout.
        thread = threading.Thread(target=heartbeat, daemon=True)
        thread.start()
        try:
            yield self
        finally:
            done.set()
            thread.join(timeout=.5)
            self.stop()

    def close(self):
        self.serial.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('port')
    args = parser.parse_args()
    client = LyoD42Client(args.port)
    try:
        print(json.dumps(client.status(), indent=2, ensure_ascii=False))
    finally:
        client.close()
