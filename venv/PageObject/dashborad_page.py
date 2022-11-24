from poium import Page, Element
from selenium.webdriver.common.keys import Keys
import time
from PageObject.snapmail_page import *



class NavigationBar(Page):
    '''这里是business portal 中dashboard的基础定位以及方法'''
    #left_table
    # notifications_table=Element(xpath="//div[contains(text(),'Notifications')]",timeout=1,describe="left_table")
    # Forms_table = Element(xpath="//div[contains(text(), 'Forms')]", timeout=1, describe="left_table")
    # Reminders_table = Element(xpath="//div[contains(text(), 'Reminders')]", timeout=1, describe="left_table")
    # Events_table = Element(xpath="//div[contains(text(), 'Events')]", timeout=1, describe="left_table")
    # invit_email = Element(xpath='//textarea[@placeholder="Ensure there is only one email address per line if inviting multiple at one time"]')
    # system_role = Element(xpath="//span[contains(text(),'Freemium')]")

    def global_search_invite(self,invite_email,product,note):
        Element(id_='layout-navbar-doSearch-input-field').send_keys(invite_email)
        Element(id_='layout-navbar-doSearch-input-field').send_keys(Keys.ENTER);time.sleep(3)

        Element(id_='layout-navbar-dataForm-product-select').send_keys(product);time.sleep(3)
        product_xpath='//li/span[contains(text(),"{}")]'.format(product)
        Element(xpath=product_xpath).click();time.sleep(1)

        Element(id_='layout-navbar-dataForm-note-textarea',describe='note').send_keys(note)
        Element(id_='layout-navbar-dataForm-doInvite-button',describe='link/invite to Valid8Me').click();time.sleep(3)
        return 0




