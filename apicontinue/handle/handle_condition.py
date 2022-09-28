#coding=utf-8
import json
import os
import sys
base_path=os.getcwd()
f_path=os.path.dirname(os.getcwd())
sys.path.append(base_path)
from handle.read_excel import Read_Excel
from jsonpath_rw import parse
from handle.HandelIni import HandleInit
'''
pass_data={
    'case':'case_001',
    'tf_opt':'yes',
    'data_text':''
}
pass_data={
    'case':'case_001',
    'tf_opt':'no',
    'data_text':data_dict
}
#         case     是否需要执行前置的编号，对应的键。
condition=imooc_001>need>data>banner>id
                                匹配规则
jsonpat_rw=imooc_001>data.banner.id
'''
class Hadnle_codition:
    def __init__(self):
        self.re=Read_Excel()
        self.hi=HandleInit()

    def split_data(self,condition):
        '''

        :param condition: 格式参考：imooc_001>data.banner.id
        :return:
        '''
        condition_list=condition.split(">")
        return condition_list

    def depend_data(self,condition_list):
        out_put_response_num=int(self.hi.get_value('output_response'))
        col = self.re.get_col('B', condition_list[0])
        row_data = self.re.get_data(col, out_put_response_num)
        return row_data

    def find_condition_data(self,condition,pass_data):
        '''
        :param condition: 前置条件
        :param pass_data: 参考pass_data
        :return:
        pass_data={
                'case':'case_001',
                'tf_opt':'no',
                'data_text':data_dict
                }
        这个前置条件的设置根据实际情况来。当前知识为
        condition_list[1]='data.banner.[0].id'
        '''
        res = ''
        pass_data = pass_data
        condition_list = self.split_data(condition)
        if pass_data['tf_opt'] == 'yes':
            data_text=self.depend_data(condition_list)
            pass_data['data_text'] = json.dumps(data_text)

        json_exe=parse(condition_list[1])
        modles=json_exe.find(pass_data['data_text'])
        for modle in modles:
            res=modle.value
            #推导式--不是很会用。。
            #res = [model.value for model in modles][0]
        return res




        #find_data=data['data_text'][condition[1]][condition[2]][condition[3]]

if __name__=='__main__':
    condition='imooc_001>data.banner.[0].id'
    data_dict={

            "status": 0,
            "data": {
                "banner": [
                    {
                        "id": 2262,
                        "type": 6,
                        "type_id": 330,
                        "name": "\u524d\u7aef\u4e0b\u4e00\u4ee3\u5f00\u53d1\u8bed\u8a00TypeScript\u4ece\u57fa\u7840\u5230axios\u5b9e\u6218",
                        "pic": "http:\/\/szimg.mukewang.com\/5cf721df09fc2be500000000.jpg",
                        "links": ""
                    },
                    {
                        "id": 1648,
                        "type": 6,
                        "type_id": 169,
                        "name": "Python3\u5165\u95e8\u673a\u5668\u5b66\u4e60 \u7ecf\u5178\u7b97\u6cd5\u4e0e\u5e94\u7528",
                        "pic": "http:\/\/szimg.mukewang.com\/5d0ed2d9085bd6ed09000300.jpg",
                        "links": ""
                    }
                ]

            }
    }
    pass_data = {
        'case': 'case_001',
        'tf_opt': 'no',
        'data_text': data_dict
    }
    hc=Hadnle_codition()
    res=hc.find_condition_data(condition,pass_data)
    print(res)