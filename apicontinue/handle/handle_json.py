# coding=utf-8

import json
import os


class HandeJson:
    def __init__(self):
        self.base_path = os.path.abspath(os.path.dirname(os.getcwd()))

    # 这边文件路径可以加一个默认值，做一个防错。
    def read_json(self, file_name):
        '''

        :param file_name: 文件名
        :return: 返回对应文件名的数据
        '''
        with open(self.base_path + '\\config\\' + file_name + '.json', encoding='utf-8') as file_json:
            json_data = json.load(file_json)
        return json_data

    def get_json_value(self, file_name, key):
        '''

        :param file_name: 文件名
        :param key: 字典的键
        :return: 返回对应字典键的值
        '''
        data = self.read_json(file_name=file_name)
        return data.get(key)

    def write_json_vale(self, file_name, data):
        '''

        :param file_name: 文件名
        :param data: 要写入的数据
        :return: 范湖一个TURE或者FALSE
        '''
        data = json.dumps(data)
        with open(self.base_path + '\\config\\' + file_name + '.json', 'w') as file_json:
            file_json.write(data)
        #这里有问题。。待改。。
        return True


if __name__ == '__main__':
    hj = HandeJson()
    data = hj.get_json_value('result', 'api3/newcourseskill')
    res = hj.get_json_value('result', 'sucess')
    data_text = {
        'dddd': 'dddsdsdzx'
    }
    hj.write_json_vale('cookie', data_text)
    print(res)
