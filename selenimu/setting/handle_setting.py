#coding=utf-8
import configparser
import os
class HandleSetting():
    def __init__(self,block='emailregister'):
        self.block=block
        #这个要加绝对路径。不然其他py文件引用会报错。
        self.setting_path='D:\pypj\selenimu\setting\setting.ini'
        self.find_handle=''


    def find_setting_el(self,element):
        finstr=configparser.ConfigParser()
        finstr.read(self.setting_path)
        self.find_handle=finstr.get(self.block,element)
        return self.find_handle

    def find_wantstr(self,element):
        self.find_setting_el(element)
        data=self.find_handle.split(">")
        guid=data[0]
        content=data[1]
        return guid,content

    def get_settinges_dict(self):
        finstr = configparser.ConfigParser()
        finstr.read(self.setting_path)
        return finstr

if __name__=='__main__':
    #传错参了。
    cf=HandleSetting()
    sf=cf.get_settinges_dict()['emailregister']
    for s,f in sf:
        print(s)


    '''    
    cf=HandleSetting()
    var=cf.find_wantstr('useemail')
    print(var[1])
    path=os.path.join(os.getcwd()+'\setting.ini')
    print(path)'''