import sys
import pandas as pd

def exportEmployeeData():
    read_file = pd.read_excel(r'DataStore/Input/Employees/emp.XLS')
    read_file.to_csv(r'DataStore/Input/Employees/emp.csv', encoding = 'utf-8', index = False, header = True)
    listEmployeeData = pd.read_csv('DataStore/Input/Employees/emp.csv', usecols = ['Code','Name'])
    return listEmployeeData

def exportProductData():
    read_file = pd.read_excel(r'DataStore/Input/Products/prodcodes.XLS')
    read_file.to_csv(r'DataStore/Input/Products/prodcodes.csv', encoding = 'utf-8', index = False, header = True)
    listProductData = pd.read_csv('DataStore/Input/Products/prodcodes.csv', usecols = ['Code', 'Descr', 'Fruit', 'Class'])
    return listProductData
