#coding=utf-8
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from find_el import Find_element


class Mainrun():
    def __init__(self,url):
        self.driver=self.get_driver(url)

    def get_driver(self,url):
        driver = webdriver.Chrome()
        driver.get(url=url)
        driver.maximize_window()
        time.sleep(5)
        return driver

    def get_element(self,element):
        fd = Find_element(self.driver)
        user_element=fd.find_el(element=element)
        return user_element

    def sent_info(self,element,value):
       self.get_element(element).send_keys(value)

    def drive_colose(self):
        self.driver.close()

def main():
  td=Mainrun('http://192.168.50.131/Home/User/reg/t/email.html')
  td.sent_info('useemail','123@dd.com')
  td.sent_info('usepass','123456789')
  td.sent_info('usepaasagin','123456789')
  td.sent_info('userestel','123456')
  time.sleep(5)
  td.drive_colose()

main()

