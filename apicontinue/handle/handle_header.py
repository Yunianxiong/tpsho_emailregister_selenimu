# coding=utf-8

import json
import os
import sys
base_path=os.getcwd()
f_path=os.path.dirname(os.getcwd())
sys.path.append(base_path)
print(base_path)
from handle.handle_json import HandeJson

class HandeHeader:
    def __init__(self):
        self.hj=HandeJson()

    def get_header_value(self):
        '''

        :return: 返回header.json的数据
        '''
        header_value=self.hj.read_json('header')
        return header_value

    def header_md5(self):
        data=self.get_header_value()
        #用md5加密
        '''
        前置条件这个--》视频中有两个方案 ：
        第一个是以上前置条件中case编号的输出为本次输入的参数之一
        第二个是将case进行先后循序的排序，然后将输出都放在excel表格进行获取
        第二个--》将case拆分，比如一个查询订单的接口，我可以拆分成，创建订单，获取订单，更新订单，删除订单
        '''

