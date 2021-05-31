import sys
import pandas as pd

def exportEmployeeData():
    read_file = pd.read_excel(r'DataStore/Employees/emp.XLS')
    read_file.to_csv(r'DataStore/Employees/emp.csv', encoding = 'utf-8', index = False, header = True)
    employeeList = pd.read_csv('DataStore/Employees/emp.csv', usecols = ['Code','Name'])
    return employeeList