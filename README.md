# MFRC522 RFID Reader on Raspberry Pi (Raspbian)

This guide explains how to use the **MFRC522 RFID reader** with a **clean Raspbian installation** on Raspberry Pi using SPI.

---

## 1. Hardware Wiring

Connect the MFRC522 module to the Raspberry Pi as follows:

| RFID-RC522 Pin | Raspberry Pi Pin | GPIO Name | SPI1 Pin | SPI1 GPIO |
| -------------- | ---------------- | --------- | -------- | --------- |
| SDA / NSS      | 24               | GPIO8     | 12       | GPIO18    |
| SCK            | 23               | GPIO11    | 40       | GPIO21    |
| MOSI           | 19               | GPIO10    | 38       | GPIO20    |
| MISO           | 21               | GPIO9     | 35       | GPIO19    |
| IRQ            | Not connected    | –         | –        | –         |
| GND            | 20               | GND       | 34       | GND       |
| RST            | 22               | GPIO25    | 22       | GPIO25    |
| 3.3V / VCC     | 17               | 3V3       | 17       | 3V3       |

⚠️ **Note:**
There are multiple versions of the MFRC522 module with different pin layouts.
Always rely on **pin names (SDA, SCK, MOSI, MISO, etc.)**, not just pin positions.

---

## 2. Enable SPI Interface

Run the Raspberry Pi configuration tool:

```bash
sudo raspi-config
```

Navigate to:

```
Advanced Options → SPI → Yes
```

Reboot is optional.
You can verify SPI is enabled with:

```bash
dtoverlay -l
```

---

## 3. Install Required Packages

Update the system and install required dependencies:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-dev git
```

---

## 4. Install SPI-Py Library

Clone and install the SPI-Py library:

```bash
git clone https://github.com/lthiery/SPI-Py.git
cd SPI-Py
sudo python setup.py install
cd ..
```

---

## 5. Install MFRC522 Python Library

Clone the MFRC522 Python repository:

```bash
cd ~
git clone https://github.com/pelwell/MFRC522-python.git
cd MFRC522-python
```

---

## 6. Run the RFID Reader Example

Run the example script:

```bash
sudo python Read.py
```

If everything is wired and configured correctly, the UID of the RFID card will be printed when a card is placed near the reader.

---

## 7. Troubleshooting

* Ensure the module is powered with **3.3V only** (never 5V).
* Double-check SPI wiring (MOSI/MISO/SCK are easy to mix up).
* Make sure SPI is enabled in `raspi-config`.
* Try running the script with `sudo`.

---

## 8. References

* [https://github.com/pelwell/MFRC522-python](https://github.com/pelwell/MFRC522-python)
* [https://github.com/lthiery/SPI-Py](https://github.com/lthiery/SPI-Py)

---

Happy hacking 🚀
