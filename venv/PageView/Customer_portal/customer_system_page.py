from poium import Page, Element
from selenium import webdriver
import allure
from poium.common import logging
import time








class Profile_Page(Page):
    '''这里是customer portal中system 的基础定位以及相关方法'''


    def upload_logo(self,logo):
        '''update photo'''
        Element(xpath='//div/input',index=0).send_keys(logo);time.sleep(1)



class MessagesPage(Page):
    '跳转 system'
    def JumpSytemMessage(self):
        _systemX = '//li[contains(text(),"System")]'
        _massage = 'system-menu-item-message'
        Element(xpath = _systemX).click();self.sleep(3)
        Element(id_=_massage).click()

    def GetLatestMassage(self):
        _massageTextID = 'component-toolTip-visibilityChange'
        latest_massage = Element(id_ = _massageTextID).text
        logging.info(f'Important info: {latest_massage}')
        return latest_massage

