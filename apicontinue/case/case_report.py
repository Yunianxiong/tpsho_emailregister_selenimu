#coding=utf-8
import os
import sys
base_path=os.getcwd()
sys.path.append(base_path)
import unittest
import HTMLTestRunner


def test_report():
    path=os.path.abspath(os.path.dirname(__file__))
    discover=unittest.defaultTestLoader.discover(start_dir=path,pattern='test_case_dd*.py')
    suite=unittest.TestSuite()
    suite.addTest(discover)
    return suite


if __name__=="__main__":
    report_up_path=os.path.abspath(os.path.dirname(os.getcwd()))
    report_path=report_up_path+"\\report\\report.html"
    with open(report_path,'wb') as f :
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='第一次报告',description='ddt报告')
        runner.run(test_report())