import sys
import pandas as pd

def exportEmployeeData():
    read_file = pd.read_excel(r'DataStore/Employees/emp.XLS')
    read_file.to_csv(r'DataStore/Employees/emp.csv', encoding = 'utf-8', index = False, header = True)
    listEmployeeData = pd.read_csv('DataStore/Employees/emp.csv', usecols = ['Code','Name'])
    return listEmployeeData

def exportProductData():
    read_file = pd.read_excel(r'DataStore/Products/prodcodes.XLS')
    read_file.to_csv(r'DataStore/Products/prodcodes.csv', encoding = 'utf-8', index = False, header = True)
    listPoductData = pd.read_csv('DataStore/Products/prodcodes.csv', usecols = ['Code', 'Descr', 'Fruit', 'Class'])
    return listPoductData
