#coding=utf-8
import time

from selenium import webdriver
from base.find_el import Find_element

#----------------6.4------------------
#可以看到的是，这网页操作的集合，即设置驱动driver->打开网页->获取网页元素->输入框传值或者元素点击->等待以及浏览器关闭
#===============6.4====================
#---------------6.5思考-----------------
#仔细思考一下open_browser和get_url是要输入的，但是传一个值的话会这个-element_click冲突
#一个handle_value,一个send_value.而element_click用得比较多。
#同理sleep_time这个也可以在Excel那边把输入参数放到操作元素那边。

class Action_method:
    def __init__(self):
        pass

    def open_browser(self,borwser):
        if borwser=='chrome':
            self.driver=webdriver.Chrome()

        elif borwser=='firefox':
            self.driver=webdriver.Firefox()
        else:
            self.driver=webdriver.Edge()

    def get_url(self,url):
        self.driver.get(url)

    def get_element(self,element):
        find_element=Find_element(self.driver)
        element=find_element.find_el(element)
        return element


    def element_send_key(self,key,value):
        element=self.get_element(key)
        element.send_keys(value)

    def element_click(self,key):
        element=self.get_element(key)
        element.click()

    def sleep_time(self,sleep_time):
        time.sleep(int(sleep_time))

    def drive_close(self):
        self.driver.close()

if __name__ =='__main__':
    pass