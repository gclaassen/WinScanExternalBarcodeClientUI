# WinScanExternalBarcodeUI

This script is build for linux compatible OS'es. The UI was executed and tested on PC running POP-OS 20.04, and a Raspberry Pi and RPi Zero.

Python version 3.X is required.

### Python modules:
- pandas
- numpy
- python-barcode
- barcode
- xlrd
- python-barcode
- pillow
- python-barcode images

### Packages required for linux
> sudo apt install python3-tk python3-pil python3-pil.imagetk python3-dev libcups2-dev gcc

### Get the correct linux drivers for the printer
ARGOX X-1000vl Printer:

Linux 64-bit:
> wget https://www.argox.com/wp-content/uploads/2018/08/ARGOX_Linux_Printer_Driver-V1.4.064-bit.zip

Linux 32-bit:
> wget https://www.argox.com/wp-content/uploads/2018/08/ARGOX_Linux_Printer_Driver-V1.4.032-bit.zip

Raspberry Pi:
> wget https://www.argox.com/wp-content/uploads/2018/08/ARGOX_RPi_Printer_Driver-V1.4.0armhf.zip

To install drivers:
> unzip *argox-driver* -d *folder/to/driver*

> cd *folder/to/driver*

> sudo bash ./install

### Cups for accessing and using the printer
> git clone https://github.com/OpenPrinting/pycups.git

> cd pycups

> make && sudo make install

> in python: import cups

### Python pip install commandline
>pip3 install numpy pandas python-barcode xlrd python-barcode "python-barcode[images]"
