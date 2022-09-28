# coding=utf-8
import configparser
import os
import sys

base_path = os.getcwd()
sys.path.append(base_path)
ini_path = os.path.dirname(os.getcwd())


class HandleInit:

    def load_ini(self):
        file_path = ini_path + "\\config\\server.ini"
        # print(file_path)
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8-sig")
        return cf

    def get_value(self, key, node=None):
        '''

        :param key:
        :param node:
        :return:
        '''
        '''
        获取ini里面的value
        '''
        if node == None:
            node = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(node, key)
        except Exception:
            print("没有获取到值")
            data = None
        return data


handle_ini = HandleInit()
if __name__ == "__main__":
    hi = HandleInit()
    res=hi.get_value('fin_result')
    print(res)
