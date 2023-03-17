from poium import Page, Element,Elements
import time
from poium.common import logging


class ActionPage(Page):
    '关于action的相关操作'

    def open_Action_Page(self):
        self.wait_page_load_timeout(10)


        Element(xpath="//a/li[text()='Actions']").click();
        time.sleep(3)
        logging.info(f"OP ✅ OPEN MY ACTIONS PAGE")

    def open_Home_Page(self):

        Element(xpath="//a/li[text()='Home']").click();self.wait_page_load_timeout(3)
        logging.info(f"OP ✅ OPEN MY Home PAGE")

    def open_new_prod_action(self,prod):
        '''传入 product name 以此来打开对应的product '''
        self.wait(5)
        product_name_xpath='//div[contains(text(),"{}")]'.format(prod)
        if Element(xpath=product_name_xpath).is_exist():
            Element(xpath=product_name_xpath).click()
            self.wait_page_load_timeout(5)
            logging.info(f"OP ✅ OPEN new product sever :{prod}")

        else: return "No find this product"

    def consent_action(self):
        '''consent button of action'''

        Element(xpath="//span[contains(text(),'Consent')]").click()
        Element(xpath="//span[contains(text(),'Yes')]").click()
        time.sleep(3)

    def not_list(self):
        return

    def upload_action_doc(self,doc_photo):
        time.sleep(3)
        '''搜索并且上传action中文件状态是pending的文件'''
        elems=Elements(xpath="//span[contains(text(),'Pending')]",timeout=5).find(self);time.sleep(3)

        for ele in elems:
            ele.click()
            Element(id_='ActionUpload-upload-select').get_attribute('value')
            Element(xpath="//div[@id='ActionUpload-upload-file-button']//input").send_keys(doc_photo);
            #要具体 定位

            time.sleep(2)
            Element(id_='ActionUpload-submit-button',describe='submit',timeout=3).click();
            logging.info(f"upload_doc : {doc_photo}")
            time.sleep(5)
        logging.info(f"OP ✅ upload_action_doc success")

    def reject_action(self):
        Element(xpath="//span[contains(text(),'Reject')]").click()
        Element(xpath="//span[contains(text(),'Yes')]").click()
        self.sleep(3)
        logging.info(f'reject_action success')


















