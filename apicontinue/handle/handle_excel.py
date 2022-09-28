# coding=utf-8

import os
import sys

import openpyxl

# 添加工程路径。防止找不到模块
case_path = os.getcwd()
sys.path.append(case_path)

open_excel = openpyxl.load_workbook(case_path + ' \\excel_data\\excel_data.xlsx')
# 拿到所有
sheet = open_excel.sheetnames
excel_data = open_excel[sheet[0]]

print(excel_data)
