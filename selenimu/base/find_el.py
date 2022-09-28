#coding=utf-8
import time
from selenium import webdriver
from setting.handle_setting import HandleSetting
from selenium.webdriver.common.by import By


class Find_element(object):
    def __init__(self,driver):
        self.driver=driver
    def find_el(self,element):
        hs=HandleSetting()
        data=hs.find_wantstr(element)
        try:
            if data[0]=='id':
                el=self.driver.find_element(by=By.ID,value=data[1])
            elif data[0]=='class':
                el = self.driver.find_element(by=By.CLASS_NAME, value=data[1])
            elif data[0]=='name':
                el = self.driver.find_element(by=By.NAME, value=data[1])
        except:
            el=None

        return el


#仅用于测试是否有问题
if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get("http://192.168.50.131/Home/User/reg/t/email.html")
    fdt=Find_element(driver)
    fdt.find_el("useemail")
    driver.close()
