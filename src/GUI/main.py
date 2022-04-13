import sys
import tkinter as tk
import WinScanExternalBarcodeUI
import ExportXlsToCsv


def main():

    listEmployeeCodes = ExportXlsToCsv.exportEmployeeData()
    listProductDetail= ExportXlsToCsv.exportProductData()

    root = tk.Tk()

    # Setting the title of the window
    root.title("WinScan External Barcode Printer")

    # Setting the geometry i.e Dimensions
    root.geometry("600x1020")

    app = WinScanExternalBarcodeUI.WinScanExternalBarcodeUI(root, listEmployeeCodes, listProductDetail)
    root.mainloop()

if __name__ == '__main__':
    main()