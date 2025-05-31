from bleak import BleakClient, BleakScanner
import asyncio


class BTEngine:
    def __init__(self):
        self.scanner = BleakScanner()
        print("Bluetooth engine initialized.")

    async def scan_devices(self) -> list:
        devices = await self.scanner.discover()
        await asyncio.sleep(10)  # Allow some time for scanning
        return devices