# coding=utf-8


import os
import sys

base_path = os.getcwd()
sys.path.append(base_path)
from deepdiff import DeepDiff
from handle.handle_json import HandeJson


class Hand_result:
    def __init__(self):
        self.hj = HandeJson()

    # 这两个方法，本质是一样的。get_code_msg是从返回的所有json数据一步一步拆开，从最开始遍历url的键存不存在，存在就获取相对应键的值
    # 这个值是一个列表嵌套字典，通过遍历列表，在遍历字典获取在判断，在获取相应的键值，
    # handl_code_msg这个是利用字典的get方法。在Hget_json_value那边用get获取相应键的值。然后遍历这个data，在用get获取相应值。
    def get_code_msg(self, url, code):
        '''

        :param url: 链接-具体到code_message，就是对应的键
        :param code: 要寻找的键
        :return: 对应键的值
        '''
        code_data = self.hj.read_json('code_message')
        for code_key in code_data:
            if url == code_key:
                code_list = code_data[url]
                for code_dict in code_list:
                    for code_text in code_dict:
                        if code_text == code:
                            msg = code_dict[code]
                            break
        return msg

    def handl_code_msg(self, url, code):
        '''

        :param url: 参考上面那一个
        :param code:
        :return:
        '''
        code_data = self.hj.get_json_value('code_message', url)
        if code_data != None:
            for i in code_data:
                msg = i.get(str(code))
                if msg:
                    return msg
        return None

    def get_result_msg(self, url, status):
        '''

        :param url: 跟上面一样
        :param status:
        :return:
        i.get(str(status))这个要注意，因为不因str()会报错。
        '''
        code_data = self.hj.get_json_value('result', url)
        if code_data != None:
            for i in code_data:
                msg = i.get(str(status))
                if msg:
                    return msg
        return None

    def judge_json(self, dict1, dict2):
        '''

        :param dict1: 要比对的第一个值
        :param dict2:
        :return:
        '''
        # dict1={"aa":"AAA","bbb":"BBBB","CC":[{"11":"22"},{"11":"44"}]}
        # dict2={"aaa":"123","bbb":"456","CC":[{"11":"111"},{"11":"44"}]}
        # DeepDiff(dict1, dict2, ignore_order=True)输出下面的结果
        # {'dictionary_item_added': [root['aaa']],
        # 'dictionary_item_removed': [root['aa']],
        # 'values_changed': {"root['bbb']": {'new_value': '456', 'old_value': 'BBBB'}, "root['CC'][0]['11']": {'new_value': '111', 'old_value': '22'}}}
        if isinstance(dict1, dict) and isinstance(dict2, dict):
            cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
            print(cmp_dict)
            if cmp_dict.get("dictionary_item_added"):
                return False
            else:
                return True


if __name__ == '__main__':
    hr = Hand_result()
    msg = hr.get_result_msg('api3/newcourseskill', 'error')
    print(msg)

'''    
    dict1={"aaa":"AA","bbb":"BBB","CC":[{"11":"22"},{"11":"44"}]}
    dict2={"aaa":"123","CC":[{"11":"111"},{"11":"44"}]}
    hs=Hand_result()
    tf=hs.judge_json(dict1,dict2)
    print(tf)
'''
