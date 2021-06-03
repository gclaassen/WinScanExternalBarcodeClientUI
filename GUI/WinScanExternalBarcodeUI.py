from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter.messagebox import askyesno, askquestion
from PIL import Image, ImageTk
import numpy as np
import barcode
from barcode.writer import ImageWriter
import os
import cups
import common

from subprocess import check_output
from subprocess import call
from time import sleep
import ghostscript

class WinScanExternalBarcodeUI:
    def __init__(self, master, listEmployeeCodes, listProductDetail):
        self.listEmployeeCodes = listEmployeeCodes
        self.listProductDetail = listProductDetail
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.font = font.Font(size=30)
        self.listChosenClass = None

        self.valChosenEmployeeName = None
        self.valChosenEmployeeCode = None
        self.valChosenProduct = None
        self.valChosenClass = None
        self.valChosenProductCode = None
        self.EmployeeIdCode = ''

        self.productColSize = 3

        self.backspaceIcon = '<'
        self.cancelIcon = 'C'

        self.EmployeeIdKeys = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            [self.backspaceIcon, '0', self.cancelIcon],
        ]

        self.createEmployeesUI()

    def clearFrame(self):
        # destroy all widgets from frame
        for widget in self.frame.winfo_children():
            widget.destroy()


    def cancelOperation(self):
        self.clearFrame()
        self.createEmployeesUI()

    def clearUserSelectedParameters(self):
        self.valChosenEmployeeName = None
        self.valChosenEmployeeCode = None
        self.valChosenProduct = None
        self.valChosenClass = None
        self.valChosenProductCode = None


    def createEmployeesUI(self):
        btnColor = common.colorDefault

        self.clearUserSelectedParameters()

        textEntry = tk.Entry(self.frame, font = self.font)
        textEntry.grid(row=0, column=0, columnspan=3, ipady=50)

        # create buttons using `keys`
        for y, row in enumerate(self.EmployeeIdKeys, 1):
            for x, key in enumerate(row):
                # `lambda` inside `for` has to use `val=key:code(val)`
                # instead of direct `code(key)`
                if key == self.backspaceIcon:
                    btnColor = common.colorBackspace
                elif key == self.cancelIcon:
                    btnColor = common.colorCancel
                else:
                    btnColor = common.colorDefault

                keyPadButton = tk.Button(self.frame, text=key, bg=btnColor, command=lambda val=key:self.keyPadPressed(val, textEntry))
                keyPadButton.grid(row=y, column=x, ipadx=45, ipady=45, sticky = "NSEW")
                keyPadButton['font'] = self.font

        acceptButton = tk.Button(self.frame, text='YES', bg=common.colorAccept, command=lambda: self.acceptButtonPressed(textEntry))
        acceptButton.grid(row=y+1, column=0, columnspan=3, ipady=50, sticky = tk.W+tk.E)
        acceptButton['font'] = self.font

        self.frame.grid_columnconfigure(5, minsize=0)

    def acceptButtonPressed(self, textEntry):
        self.valChosenEmployeeCode = int(self.EmployeeIdCode)
        # clear `entry`
        textEntry.delete('0', 'end')
        # clear global
        self.EmployeeIdCode = ''

        if np.min(np.isin(self.valChosenEmployeeCode, self.listEmployeeCodes['Code'])) :
            idxRow = np.min(np.where(self.listEmployeeCodes['Code'] == self.valChosenEmployeeCode ))
            self.valChosenEmployeeName = self.listEmployeeCodes['Name'][idxRow]
            print("Code: {0} Employee Name: {1}".format(self.valChosenEmployeeCode, self.valChosenEmployeeName))

            self.clearFrame()
            self.confirmEmployee()

        else:
            print("Code: {0} not in database".format(self.valChosenEmployeeCode))
            self.valChosenEmployeeCode = None
            ValueError

    def keyPadPressed(self, value, textEntry):
        if value == self.backspaceIcon:
            self.EmployeeIdCode = self.EmployeeIdCode[:-1]
            textEntry.delete('0', 'end')
            textEntry.insert('end', self.EmployeeIdCode)

        elif value == self.cancelIcon:
            # clear `pin`
            self.EmployeeIdCode = ''
            # clear `entry`
            textEntry.delete('0', 'end')

        else:
            self.EmployeeIdCode += value
            textEntry.insert('end', value)

    def confirmEmployee(self):

        label = tk.Label(self.frame, text="IS THIS CORRECT?\nCode: {0}\nName: {1}".format(self.valChosenEmployeeCode, self.valChosenEmployeeName), font = self.font)
        label.grid(row=0, column=0, columnspan=3, ipady=50, sticky = tk.W+tk.E)

        yesButton = tk.Button(self.frame, text='YES', bg=common.colorAccept, command=lambda: self.selectedCorrectEmployee())
        yesButton.grid(row=1, column=0, columnspan=1, ipady=50, sticky = tk.W+tk.E)
        yesButton['font'] = self.font

        noButton = tk.Button(self.frame, text='NO', bg=common.colorCancel, command=lambda: self.cancelOperation())
        noButton.grid(row=1, column=2, columnspan=1, ipady=50, sticky = tk.W+tk.E)
        noButton['font'] = self.font

        # answer = askyesno(title='Confirmation',
        #                     message=')

    def selectedCorrectEmployee(self):
        self.clearFrame()
        self.createProductUI()

    def createProductUI(self):
        y = 0
        x = 0
        getUniqueProducts = np.unique(self.listProductDetail['Fruit'])

        label = tk.Label(self.frame, text="CHOOSE PRODUCT", font = self.font)
        label.grid(row=y, column=0, columnspan=3, ipady=50, sticky = tk.W+tk.E)

        y = y + 1

        for idxProducts, product in enumerate(getUniqueProducts):
            print("{0} {1}".format(idxProducts, product))
            productButton = tk.Button(self.frame, text=product, bg=common.colorDefault, command=lambda val=product:self.productChosen(val))
            productButton.grid(row=y, column=x, ipadx=15, ipady=15, sticky="NSEW")
            productButton['font'] = self.font
            [y,x] = self.getGridLocation(y, x)

        y = y + 1

        cancelButton = tk.Button(self.frame, text='CANCEL', bg=common.colorCancel, command=lambda: self.cancelOperation())
        cancelButton.grid(row=y, column=0, columnspan=self.productColSize, ipady=50, sticky = tk.W+tk.E)
        cancelButton['font'] = self.font


    def getGridLocation(self, prevRow, prevCol):
        if prevCol < self.productColSize-1:
            return [prevRow, prevCol + 1]
        if prevCol == self.productColSize-1:
            return [prevRow + 1, 0]


    def productChosen(self, value):
        self.valChosenProduct = value
        idxListProductDetail = np.where(self.listProductDetail['Fruit'] == value)
        self.listProductClassDetail = np.take(self.listProductDetail, idxListProductDetail[0], 0)
        self.clearFrame()
        self.createClassUI()

    def createClassUI(self):
        y = 0
        x = 0

        label = tk.Label(self.frame, text="SIZE CHOSEN: {0}".format(self.valChosenProduct), font = self.font)
        label.grid(row=y, column=0, columnspan=3, ipady=50, sticky = tk.W+tk.E)

        y = y + 1

        label = tk.Label(self.frame, text="CHOOSE CLASS", font = self.font)
        label.grid(row=y, column=0, columnspan=3, ipady=50, sticky = tk.W+tk.E)

        y = y + 1

        for idxClass, prodClass in enumerate(self.listProductClassDetail['Class']):
            print("{0} {1}".format(idxClass, prodClass))
            productButton = tk.Button(self.frame, text=prodClass, bg=common.colorDefault, command=lambda val=prodClass:self.classChosen(val))
            productButton.grid(row=y, column=x, ipadx=15, ipady=15, sticky="NSEW")
            productButton['font'] = self.font
            [y,x] = self.getGridLocation(y, x)

        y = y + 1

        cancelButton = tk.Button(self.frame, text='CANCEL', bg=common.colorCancel, command=lambda: self.cancelOperation())
        cancelButton.grid(row=y, column=0, columnspan=self.productColSize, ipady=50, sticky = tk.W+tk.E)
        cancelButton['font'] = self.font

    def classChosen(self, value):
        self.valChosenClass = value
        idxProductCode = np.where(self.listProductClassDetail['Class'] == value)
        tempProductCodeArr = np.take(self.listProductClassDetail, idxProductCode[0], 0)
        self.valChosenProductCode = np.unique(tempProductCodeArr['Code'])[0]
        self.clearFrame()
        self.barcodeGenerator()
        self.printSetupUI()

    def barcodeGenerator(self):
        # TODO: how does the first set relate to product code
        # TODO: how to make the last 5 digits unique
        oCode128 = barcode.get_barcode_class('code128')
        code128 = oCode128("{0:03d}{1:04d}{2:05d}".format(2, self.valChosenEmployeeCode, 4260), writer=ImageWriter())
        code128.save('DataStore/Output/barcode')

    def printSetupUI(self):
        label = tk.Label(self.frame, text="{0} {1} {2}".format(self.valChosenEmployeeCode, self.valChosenEmployeeName, self.valChosenProductCode), font = self.font)
        label.grid(row=0, column=0, columnspan=3, ipady=50, sticky = tk.W+tk.E)

        # Create a photoimage object of the image in the path
        barcodeImage = Image.open("DataStore/Output/barcode.png")
        barcodePhotoImage = ImageTk.PhotoImage(barcodeImage)

        barcodeWidget = tk.Label(self.frame, image=barcodePhotoImage)
        barcodeWidget.image = barcodePhotoImage
        barcodeWidget.grid(row=1, column=0, columnspan=3, ipady=50, sticky = tk.W+tk.E)

        #TODO: check printer status

        #TODO: print buttons
        yesButton = tk.Button(self.frame, text='  PRINT  ', bg=common.colorAccept, command=lambda: self.printBarcode())
        yesButton.grid(row=2, column=0, columnspan=1, ipady=50, sticky = tk.W+tk.E)
        yesButton['font'] = self.font

        noButton = tk.Button(self.frame, text='CANCEL', bg=common.colorCancel, command=lambda: self.cancelOperation())
        noButton.grid(row=2, column=2, columnspan=1, ipady=50, sticky = tk.W+tk.E)
        noButton['font'] = self.font

        self.frame.grid_columnconfigure(4, minsize=0)

    def printBarcode(self):
        # TODO:
        conn = cups.Connection()
        printers = conn.getPrinters()
        conn.printFile(common.printer_name,'DataStore/Output/test.pcx',"{0} {1} {2}".format(self.valChosenEmployeeCode, self.valChosenEmployeeName, self.valChosenProductCode), {})
        # conn.printFile(common.printer_name,'DataStore/Output/test.eps',"{0} {1} {2}".format(self.valChosenEmployeeCode, self.valChosenEmployeeName, self.valChosenProductCode), {})
