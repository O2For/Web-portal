from poium import Page, Element
from selenium import webdriver
import allure
import time
class Profile_Page(Page):
    '''这里是customer portal中system 的基础定位以及相关方法'''
    def upload_logo(self,logo):
        '''update photo'''
        Element(xpath='//div/input',index=0).send_keys(logo);time.sleep(1)
    def company_information(self):
        return 0

