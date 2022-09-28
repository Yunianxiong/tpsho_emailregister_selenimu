#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get('http://192.168.50.131/Home/User/reg/t/email.html')
time.sleep(5)
use_emial=driver.find_element(by=By.ID,value='username')
use_emial.send_keys('12345678901@qq.com')
use_emial.click()
'''
use_code=driver.find_element(by=By.ID,value='verify_Code2')

use_password=driver.find_element(by=By.ID,value='password')
use_password2=driver.find_element(by=By.ID,value='password2')

use_tel=driver.find_element(by=By.NAME,value='invite')

use_check=driver.find_element(by=By.ID,value='checktxt')

use_pass=driver.find_element(by=By.CLASS_NAME,value='layui-layer-title')
use_pass_toexit=ec.visibility_of_element_located(use_pass)
if use_pass_toexit:
    use_pass_to=driver.find_element(by=By.CLASS_NAME,value='layui-layer-ico layui-layer-close layui-layer-close1')
    use_pass_to.click()
'''
time.sleep(5)
driver.close()