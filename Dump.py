#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import MFRC522
import signal
import sys
import time

continue_reading = True

def end_read(sig, frame):
    global continue_reading
    print("\nStop")
    continue_reading = False
    sys.exit(0)

signal.signal(signal.SIGINT, end_read)

reader = MFRC522.MFRC522()

print("Waiting for RFID card...")

while continue_reading:
    status, _ = reader.MFRC522_Request(reader.PICC_REQIDL)
    if status == reader.MI_OK:
        status, uid = reader.MFRC522_Anticoll()
        if status == reader.MI_OK:
            print(f"Card UID: {uid}")
            time.sleep(1)
