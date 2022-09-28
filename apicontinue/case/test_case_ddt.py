# coding=utf-8
import json
import os
import sys
base_path=os.getcwd()
sys.path.append(base_path)
import ddt
import unittest
from handle.read_excel import Read_Excel
from run.new_run_main import RunMain
re=Read_Excel()
@ddt.ddt
class TestCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rm=RunMain()

    def setUp(self) -> None:
        print("这是前置")
    def tearDown(self) -> None:
        print('这是后置')

    @ddt.data(*re.get_excel_dict_list())
    @ddt.unpack
    def test_01(self,excel_dict_list):
        #print(f"{type(excel_dict_list)}--->{excel_dict_list}")
        #for exce_dict in excel_dict_list:
        fin_result=self.rm.run_case(excel_dict_list)
        self.assertEqual('用例通过',fin_result,msg=f"{type(fin_result)}-->{fin_result}")

if __name__=='__main__':
    unittest.main()