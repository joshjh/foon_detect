
#!/home/josh/code/python/foon_detect/.venv/bin/python3

from sql_engine import GresEngine
from bt_engine import BTEngine
import asyncio
import socket

DEVICE_STRING_T = ("F2:FF:95:EA:BB:F6", "40:92:D3:4E:08:A1", "C1:3A:6D:25:C4:CA")
HOSTNAME = socket.gethostname()
print(f"Running on host: {HOSTNAME}")

def main():
    engine = GresEngine()
    bt_engine = BTEngine()

    try:
        while True:
            # record heartbeat
            engine.write_heartbeat(detector=HOSTNAME)
            devices = asyncio.run(bt_engine.scan_devices())
            print("Bluetooth devices found:")
            for device in devices:
                print(f" - {device.name} ({device.address})")
            
            for device in devices:
                if device.address in DEVICE_STRING_T:
                    print(f"Found target device: {device.name} ({device.address})")
                    engine.write_instance()
                    print("Instance written to database.")
        
    except KeyboardInterrupt:
        print("Exiting...")
        engine.close()

if __name__ == "__main__":
    main()

