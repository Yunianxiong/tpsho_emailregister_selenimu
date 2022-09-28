#coding=utf-8

from PIL import Image
import pytesseract
from selenium import webdriver
import ddddocr
from base.find_el import Find_element
from selenium.webdriver.chrome.service import Service

class Get_check_code():
    def __init__(self,driver,check_element):
        self.check_element=check_element
        self.driver=driver

    def get_screen(self):
        self.driver.save_screenshot("D:\pypj\selenimu\images\check_code\\t1.png")

    def get_crop_screen(self):
        var = self.check_element
        left = var.location['x']
        top = var.location['y']
        right = var.size['width'] + left
        height = var.size['height'] + top

        im = Image.open("D:\pypj\selenimu\images\check_code\\t1.png")
        img = im.crop((left, top, right, height))
        img.save("D:\pypj\selenimu\images\checek_code_crop\\t2.png")

    ''' 这个不用
    def get_code(self):
        image = Image.open("/images/checek_code_crop/t2.png")
        text = pytesseract.image_to_string(image)
        return text
        
    def get_code_run(self):
        self.get_screen()
        self.get_crop_screen()
        text=self.get_code()
        return text
    '''

    def get_dddcor_code(self):
        ocr = ddddocr.DdddOcr(show_ad=False)
        with open("D:\pypj\selenimu\images\checek_code_crop\\t2.png", 'rb') as f:
            image = f.read()

        res = ocr.classification(image)
        return res

    def get_code_run2(self):
        self.get_screen()
        self.get_crop_screen()
        text=self.get_dddcor_code()
        return text

if __name__=='__main__':
    service = Service(executable_path=r"C:\Users\yuxiaonian\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("http://192.168.50.131/Home/User/reg/t/email.html")
    fd=Find_element(driver)
    td=fd.find_el('imagecode')
    tg=Get_check_code(driver,td)
    text=tg.get_code_run2()
    print(text)
    driver.close()
'''


        print(f'left-->{left}')
        print(f'top-->{top}')
        print(f"size width->{var.size['width']}")
        print(f"sizeheight-->{var.size['height']}")
        print(f'right-->{right}')
        print(f'height-->{height}')
'''