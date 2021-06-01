# WinScanExternalBarcodeUI

This script is build for linux compatible OS'es. The UI was executed and tested on PC running POP-OS 20.04, and a Raspberry Pi and RPi Zero.

### python modules:
- pandas
- numpy
- python-barcode
- barcode
- xlrd
- python-barcode
- pillow
- python-barcode images

### packages required for linux
> sudo apt install python3-tk python3-pil python3-pil.imagetk python3-dev libcups2-dev gcc


### cups for accessing and using the printer
> git clone https://github.com/OpenPrinting/pycups.git

> cd pycups

> make && sudo make install

### python pip install commandline
>pip3 install numpy pandas python-barcode xlrd python-barcode "python-barcode[images]"