#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import MFRC522
import time

reader = MFRC522.MFRC522()

print("Waiting for card...")

while True:
    status, _ = reader.MFRC522_Request(reader.PICC_REQIDL)
    if status == reader.MI_OK:
        status, uid = reader.MFRC522_Anticoll()
        if status == reader.MI_OK:
            print("UID:", uid)
            print("Write demo done (implement Auth/Write nếu cần)")
            break
