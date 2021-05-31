import tkinter as tk
import tkinter.font as font
import numpy as np

class ProductDetails:
    def __init__(self, master, listProductDetail):
        self.master = master
        self.listProductDetail = listProductDetail
        self.windowFrame = tk.Toplevel()
        self.colSize = 5
        self.font = font.Font(size=30)
        self.maxButtonSize = 0

        self.openProductPage()
        self.addProductDetailToWindow()

    def openProductPage(self):
        self.windowFrame.grab_set()
        self.windowFrame.title("Choose the correct product")
        # Setting the geometry i.e Dimensions
        self.windowFrame.geometry("1020x600")
        self.windowFrame.lift(aboveThis=self.master)

    def addProductDetailToWindow(self):
        y = 0
        x = 0
        getUniqueProducts = np.unique(self.listProductDetail['Fruit'])

        for idxProducts, product in enumerate(getUniqueProducts):
            print("{0} {1}".format(idxProducts, product))
            productButton = tk.Button(self.windowFrame, text=product, bg='gray', command=lambda val=product:self.productChosen(val))
            productButton.grid(row=y, column=x, ipadx=50, ipady=50, sticky="NSEW")
            productButton['font'] = self.font
            [y,x] = self.getGridLocation(y, x)


    def getGridLocation(self, prevRow, prevCol):

        if prevCol < self.colSize-1:
            return [prevRow, prevCol + 1]
        if prevCol == self.colSize-1:
            return [prevRow + 1, 0]


    def productChosen(self, value):
        #TODO:
        idxListProductDetail = np.where(self.listProductDetail['Fruit'] == value)
        tempListProductDetail = self.listProductDetail[idxListProductDetail[0]]
        NotImplementedError


