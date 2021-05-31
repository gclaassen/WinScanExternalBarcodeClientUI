import sys
import tkinter as tk
import EmployeeKeypadUI
import ExportXlsToCsv


def main():
    root = tk.Tk()

    employeeCodes = ExportXlsToCsv.exportEmployeeData()

    # Setting the title of the window
    root.title("WinScan External Barcode Printer")

    # Setting the geometry i.e Dimensions
    root.geometry("1020x600")

    app = EmployeeKeypadUI.EmployeeCodes(root)
    root.mainloop()

if __name__ == '__main__':
    main()