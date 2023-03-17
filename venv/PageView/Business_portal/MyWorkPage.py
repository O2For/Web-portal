from selenium.webdriver.common.keys import Keys
from PageView.Mail.snapmail_page import *
from poium.common import logging


class NavigationBar(Page):
    '''这里是business portal 中My work page的基础定位以及方法'''
    #left_table
    # notifications_table=Element(xpath="//div[contains(text(),'Notifications')]",timeout=1,describe="left_table")
    # Forms_table = Element(xpath="//div[contains(text(), 'Forms')]", timeout=1, describe="left_table")
    # Reminders_table = Element(xpath="//div[contains(text(), 'Reminders')]", timeout=1, describe="left_table")
    # Events_table = Element(xpath="//div[contains(text(), 'Events')]", timeout=1, describe="left_table")
    # invit_email = Element(xpath='//textarea[@placeholder="Ensure there is only one email address per line if inviting multiple at one time"]')
    # system_role = Element(xpath="//span[contains(text(),'Freemium')]")
    def OpenMyWork(self):
        self.wait(5)
        Element(xpath="//span[contains(text(),'My Work')]").click()

    def SourceDocuments(self,invite_email,product,**kwargs):
        '''send request 发送一个新的邀请'''
        self.wait_page_load_timeout(10)

        Element(id_='layout-navbar-source-documents-button',describe='点击Soure document').click()

        Element(id_='component-tag-input').send_keys(invite_email)
        #Element(id_='source-documents-product-service-select',timeout=5).send_keys(Keys.ENTER)
        #2023 最新版更新路径
        Element(id_='source-documents-product-service-select').click();time.sleep(3)
        ProductXpath="//div/div//p[contains(text(),'{}')]".format(product)
        Element(xpath=ProductXpath).click()
        if kwargs:
            Element(id_='layout-connect-note-input',describe='note').send_keys(kwargs['Note'])
        Element(id_='customer.Confirm.btn.save',describe='Send Request').click();time.sleep(3)
        Element(id_='customer.close.grey.btn',describe="close SourceDocuments").click()
        logging.info(f'SourceDocuments success invite: {invite_email}the product is: {product}')
        self.sleep(2)


        return print('send request success')





