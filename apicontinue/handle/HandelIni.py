# coding=utf-8
import configparser
import os
import sys

# 返回上一级路径
ini_path = os.path.dirname(os.getcwd())
base_path = os.getcwd()
sys.path.append(base_path)
print(base_path)


class HandleInit:

    def load_ini(self):
        file_path = ini_path + "\config\sserver.ini"
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8-sig")
        return cf

    def get_value(self, key, node=None):
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


if __name__ == "__main__":
    handle_ini = HandleInit()
    hi = HandleInit()
    print(hi.get_value("host"))
