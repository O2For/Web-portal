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
            self.sleep(3)

        else: return "No find this product"

    def consent_action(self):
        '''consent button of action'''

        Element(xpath="//span/button/span[contains(text(),'C')]",index=1).click()
        Element(xpath="//span[contains(text(),'Yes')]").click()
        time.sleep(3)

    def not_list(self):
        return

    #def upload_action_doc(self,doc_photo,**kwargs):
    def upload_action_doc(self,DocPath,dataTest):
        DOCPATH=DocPath#跟目录
        AllDoc=dataTest#路径

        DocList_AddDateOfIssue=['Certified Document', 'Utility Bill', 'Bank / Financial Statement',
                                'Test for Ind1', 'Current Bank Account Statement', 'Current Mortgage Statements', 'Current Credit Union Statement', 'Current Loan Statements', 'Supplier Statements', 'Current Social Welfare Payslips', 'Employment earnings summary', 'Share Certificates or Annual Statements']

        time.sleep(3)
        '''搜索并且上传action中文件状态是pending的文件'''
        elems=Elements(xpath="//span[contains(text(),'Pending')]",timeout=5).find(self);time.sleep(3)

        for ele in elems:
            ele.click()
            Doc_type=Element(id_='ActionUpload-upload-select').get_attribute('value')
            cur_date = time.strftime("%d/%m/%Y")

            if Doc_type=='Passport':
                #kwargs['Passport'] 为路径文件地址！

                Element(xpath="//div[@id='ActionUpload-upload-file-button']//input").send_keys(DOCPATH+AllDoc[Doc_type]);
                Element(id_='ActionUpload-submit-button', describe='submit', timeout=3).click();
                self.sleep(5)#等待regular
                #修改到期时间

                Element(id_='document-upload-regular-inputList-item-not-513').send_keys(cur_date,clear=True)
                #修改 出生时间
                Element(id_='document-upload-regular-inputList-item-not-514').send_keys('01/01/1999',clear=True)
                Element(xpath="//BUTTON/span[contains(text(),'Confirm')]",describe='# 确认regular 证件识别结果').click()# 确认regular 证件识别结果
                self.sleep(5)
                complete_icon =  Element(xpath="//div[contains(text(),'Passport')]/../following-sibling::div[1]//span[contains(text(),'Completed')]")
                assert complete_icon
                logging.info(f"Doc path :{DOCPATH+AllDoc[Doc_type]}, Type is :{Doc_type} --> Upload successfully")
            #要具体 定位
            elif Doc_type=='National ID Card':
                Element(xpath="//label[contains(text(),'Date of Expiry')]/..//input",describe='Date of Expiry').send_keys(cur_date)

                Element(xpath="//div[@id='ActionUpload-upload-file-button']//input").send_keys(DOCPATH+AllDoc[Doc_type]);
                time.sleep(2)
                Element(id_='ActionUpload-submit-button',describe='submit',timeout=3).click();
                logging.info(f"Doc xpath : {DOCPATH+AllDoc[Doc_type]},Type is :{Doc_type}-> upload successfully")
                time.sleep(5)
            elif Doc_type in DocList_AddDateOfIssue:
                Element(xpath="//label[contains(text(),'Date of Issue')]/..//input",describe='Date of Issue').send_keys('01/01/1999')
                Element(xpath="//div[@id='ActionUpload-upload-file-button']//input").send_keys(DOCPATH+AllDoc[Doc_type]);
                time.sleep(2)
                Element(id_='ActionUpload-submit-button', describe='submit', timeout=3).click();
                logging.info(f"Doc xpath : {DOCPATH+AllDoc[Doc_type]}, Type is :{Doc_type}-> upload successfully")
                time.sleep(5)
            else:
                Element(xpath="//div[@id='ActionUpload-upload-file-button']//input").send_keys(DOCPATH+AllDoc[Doc_type]);
                time.sleep(2)
                Element(id_='ActionUpload-submit-button', describe='submit', timeout=3).click();
                logging.info(f"Doc xpath : {DOCPATH+AllDoc[Doc_type]},Type is :{Doc_type}-> upload successfully")
                time.sleep(5)


        logging.info(f"OP ✅ upload_action_doc success")

    def reject_action(self):
        Element(xpath="//button/span[contains(text(),'R')]",index=1).click()
        Element(xpath="//span[contains(text(),'Yes')]").click()
        self.sleep(3)
        logging.info(f'reject_action success')


















