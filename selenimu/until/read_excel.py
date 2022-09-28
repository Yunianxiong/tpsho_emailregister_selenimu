#coding=utf-8

import sys
sys.path.append('..')
print(sys.path)

import xlrd2
import xlutils
from xlutils.copy import copy

class handle_excel_data:
    def __init__(self,excel_path=None,index=None):

        if excel_path==None:
            excel_path=r'D:\pypj\selenimu\until\excel_data\register_case.xlsx'
        if index==None:
            index=0

        self.data=xlrd2.open_workbook(excel_path)
        self.table=self.data.sheets()[index]

        #获取行数


#xlrd.biffh.XLRDError: Excel xlsx file; not supported报错----版本问题
#从xlrd换成xlrd2
#-----------6-3记录----------------------------
#首先在get_row获取行数加了一个容错(只查找行数大于等于1的）
#然后再get_data获取数据这边也加以个容错。（如果get_row返回NONE,这个就没法运行了）
#最后是获取单元格数据那边也加了一个容错，当所要写的行数小于Excel总行数的时候才可以写入。
#------------------分割线----------------------------------------------
    def get_data(self):
        result=[]
        rows=self.get_rows()
        if rows !=None:
            for i in range(self.get_rows()):
                gexc=self.table.row_values(i)
                result.append(gexc)
            return result
        return None

    #获取行数
    def get_rows(self):
        rows = self.table.nrows
        if rows>=1:
            return rows
        return None
    #获取单元格的数据。
    def get_col_value(self,row,col):
        if self.get_rows()>row:
            data=self.table.cell (row,col).value
            return data
        return None
    #写入数据
    def write_value(self,row,col,value):

        rear_value=self.data
        write_data=copy(rear_value)
        write_data.get_sheet(0).write(row,col,value)
        write_data.save()


if __name__=='__main__':
    hea=handle_excel_data()
    data=hea.table
    print(data)
    '''  
    ed=handle_excel_data()
    data=ed.get_col_value()
    print(data)
    '''
