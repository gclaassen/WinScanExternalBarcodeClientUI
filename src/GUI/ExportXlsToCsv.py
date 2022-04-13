import sys
import pandas as pd
import common

def exportEmployeeData():
    read_file = pd.read_excel(common.employeeXlsFilePath)
    read_file.to_csv(common.employeeCsvFilePath, encoding = 'utf-8', index = False, header = True)
    listEmployeeData = pd.read_csv(common.employeeCsvFilePath, usecols = common.employeeColumnList)
    return listEmployeeData

def exportProductData():
    read_file = pd.read_excel(common.productXlsFilePath)
    read_file.to_csv(common.productCsvFilePath, encoding = 'utf-8', index = False, header = True)
    listProductData = pd.read_csv(common.productCsvFilePath, usecols = common.productColumnList)
    return listProductData
