# WIP

# WinScanExternalBarcodeClientUI

This script is build for linux compatible OS'es. The UI was executed and tested on PC running POP-OS 20.04, and a Raspberry Pi and RPi Zero.

Python version 3.X is required.

### Python modules:
- pandas
- numpy
- python-barcode
- barcode
- xlrd
- treepoem
### Packages required for linux
> sudo apt install python3-tk python3-pil python3-pil.imagetk python3-dev libcups2-dev gcc ghostscript barcode

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
>pip3 install numpy pandas python-barcode xlrd treepoem

## TODO:
- Printer: ARGOX X-1000 VL
- Page and Label Setup:
  - Orientation: Portrait
  - Page size: 94.1 x 126.6mm
  - Label size: 45.3 x 23mm (w x h)
  - Left margin: 1mm
  - Top margin: 2mm
  - Horizontal gap: 2.5mm
  - Vertical gap: 2.4mm
- File types: PCX, BMP, GDI, (IMG, HEX)

