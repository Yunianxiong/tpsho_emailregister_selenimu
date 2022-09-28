#coding=utf-8
import os
import unittest
import HTMLTestRunner


def test_register():

    path='D:\pypj\selenimu\case'
    discover=unittest.defaultTestLoader.discover(start_dir=path,pattern='unittest_*.py')
    suite=unittest.TestSuite()
    suite.addTest(discover)
    return suite

if __name__=='__main__':
    path = 'D:\pypj\selenimu\\reporets\\data_excel.html'
    with open(path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='第一次报告', description='测试报告', verbosity=2)
        runner.run(test_register())