from poium import Page, Element,Elements
import time



class ActionPage(Page):

    def open_Action_Page(self):

        Element(xpath="//a/li[text()='Actions']").click();time.sleep(3)
        return
    def open_new_prod_action(self,prod):
        '''传入 product name 以此来打开对应的product '''
        xpath='//div[contains(text(),"{}")]'.format(prod)
        Element(xpath=xpath).click();time.sleep(5)

    def consent_action(self):
        '''consent button of action'''
        Element(id_='ActionType4-consent-button').click()
        Element(xpath="//span[contains(text(),'Yes')]").click()
        time.sleep(3)

    def not_list(self):
        return
    def upload_action_doc(self,doc_photo):
        '''搜索并且上传action中文件状态是pending的文件'''
        elems=Elements(xpath="//span[contains(text(),'Pending')]").find();time.sleep(3)

        for ele in elems:
            ele.click()
            Element(id_='ActionUpload-upload-select').get_attribute('value')
            Element(xpath="//div[@id='ActionUpload-upload-file-button']//input").send_keys(doc_photo);
            #要具体 定位
            time.sleep(2)
            Element(id_='ActionUpload-submit-button',describe='submit').click();time.sleep(10)
















    def reject_action(self):
        return

