from poium import Page, Element,Elements
import time
from poium.common import logging

class Companies(Page):
    _sharebuttonX='//div[@class="header"]/img'

    _shareCompanyID='companies-dialog-companyId-select'
    _sharecompanylistX='//ul/li/div'
    _shareProductButtonID='companies-dialog-service-select'
    _shareConfirmID='companies-dialog-confirm-button'
    _shareCancelID='companies-dialog-cancel-button'



    def SearchConnect(self,company,product):

        _pendingDocsX='//span[contains(text(),"Pending")]'
        _shareProductX = '//li/span[contains(text(),"{}")]'.format(product);
        Element(xpath=self._sharebuttonX).click()
        Element(id_=self._shareCompanyID).send_keys(company)
        Element(xpath=self._sharecompanylistX).click()
        Element(id_=self._shareProductButtonID).click()
        Element(xpath=_shareProductX).click()

        Element(id_=self._shareConfirmID).click();self.sleep(3);
        '展开list'
        pendingNumbers=Elements(xpath=_pendingDocsX).find(self)
        if len(pendingNumbers)>0: #存在pending的文件
            Doc=[]
            DocListEle=Elements(xpath="//span[contains(text(),'Pending')]/../..//preceding-sibling::span").find(self)
            for ele in DocListEle:
                DocName = ele.text;
                Doc.append(DocName)
            logging.info(f'τ Pending docs :{Doc}...')
            Element(id_=self._shareConfirmID).click();
            return Doc

        else:
            Element(id_=self._shareConfirmID).click();
            self.sleep(5);

    def ReturnSharedDocuments(self):
        shareDocument = Element(xpath='//*[@id="component-toolTip-visibilityChange"]').text

        Recent_Product = Element(xpath='//td/div/span',index=0).text
        #get_attribute('value')

        d=dict()
        d['shareDocument']=shareDocument
        d['Recent_Product']=Recent_Product

        logging.info(f"OP ✅ ReturnSharedDocuments :{shareDocument}，Recent_Product：【{Recent_Product}】")

        return d