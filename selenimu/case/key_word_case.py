#coding=utf-8
from until.read_excel import handle_excel_data
from key_word.action_method import Action_method

#-------------6.7---------------
#------------6.11有一个写入错误----运行了，只写一次
#原因是excel那边处理写入数据那边只调用一次xlrd2.open_workbook(excel_path)这个，
#简单理解就是只打开了一次，

class Keywordcase:
    def __init__(self):
        self.am = Action_method()

    def run_main(self):
        hed=handle_excel_data('D:\pypj\selenimu\\until\excel_data\key_word.xlsx')
        case_lins=hed.get_rows()
        if case_lins:
            for lin in range(1,case_lins):
                isrun=hed.get_col_value(lin,4)
                #这个后期应该可以设置为type类型
                if isrun=='yes':
                    h_element=hed.get_col_value(lin,3)
                    h_method=hed.get_col_value(lin,5)
                    h_values=hed.get_col_value(lin,6)
                    h_ex_method=hed.get_col_value(lin,7)
                    h_ex_text=hed.get_col_value(lin,8)
                    self.run_method(h_method,h_values,h_element)


    def get_except_text(self,data):
        return data



    def run_method(self,method,send_value,handle_value):

        #getattr可以执行方法。要执行加一个()，比如：method()
        method_run=getattr(self.am,method)
        #判断是否为空,这边针对三种情况。
        if send_value:
            method_run(handle_value,send_value)
        elif handle_value:
            method_run(handle_value)
        else:
            method_run()

if __name__=='__main__':
    kwc=Keywordcase()
    kwc.run_main()