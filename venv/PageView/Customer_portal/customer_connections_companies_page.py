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

    _pendingDocsX = '//span[contains(text(),"Pending")]'
    _NoAccessDocsX = '//span[contains(text(),"NoAccess")]'

    _alertMessage = '//*[contains(@class,"el-message__content")]'


    XButton= Element(class_name = 'el-dialog__headerbtn')
    confirmButton  = Element(id_ =_shareConfirmID)



    def JumpCompanies(self):
        _connection = 'el-submenu__title'
        _companyid = 'sidebar-menu-item0'
        Element(class_name = _connection).click()
        Element(id_ = _companyid).click();self.sleep(3)

    '分享控件'
    def SearchConnect(self,company,product):
        '点击share 按钮并选择分享的公司和产品'

        _shareProductX = '//li/span[contains(text(),"{}")]'.format(product);
        '选择产品'
        Element(xpath=self._sharebuttonX).click()
        Element(id_=self._shareCompanyID).send_keys(company)
        Element(xpath=self._sharecompanylistX).click()
        Element(id_=self._shareProductButtonID).click()
        Element(xpath=_shareProductX).click()

        NeedRep = '//*[contains(text(),"Authorised reps")]'
        if Element(xpath = NeedRep).is_exist():
            repnumText = Element(xpath = NeedRep).text
            repnum = "".join(list(filter(str.isdigit, repnumText)))
            logging.info(f'This product need reps number is {int(repnum)}')
            return int(repnum)
        else:

            Element(id_=self._shareConfirmID).click();self.sleep(3);
            return self.shareProductDetail()

    def ProductSelectRep(self,*args,UserType='Online'):
        '为产品选择rep 默认选择online'
        _repTypeLabel = 'el-radio__label'
        confirmid = 'companies-dialog-confirm-button'

        if UserType=='Online':
            Element(class_name = _repTypeLabel,index=1).click();self.sleep(1)
            for repname in args:
                _repcheck = '//*[contains(text(),"{}")]/../span[2]//span'.format(repname)
                Element(xpath = _repcheck,index=1).click()
        Element(id_=confirmid).click();self.sleep(2)
        return self.shareProductDetail()


    '具体产品需要上传的文档，若满足所有条件，则直接上传成功'
    def shareProductDetail(self):
        '分享产品中的详情操作，判断列表中各个文档的状态'

        '展开list'

        if Element(xpath = self._pendingDocsX).is_exist():
            pendingNumbers=Elements(xpath=self._pendingDocsX).find(self)

            '#存在pending的文件'
            pendingDoc = []
            DocListEle = Elements(xpath="//span[contains(text(),'Pending')]/../..//preceding-sibling::span").find(
                self)
            for ele in DocListEle:
                DocName = ele.text;
                pendingDoc.append(DocName)
            logging.info(f'τ Pending docs :{pendingDoc}...')
            Element(id_=self._shareConfirmID).click();
            return pendingDoc

        if Element(xpath=self._NoAccessDocsX).is_exist():
            noaccessNumber = Elements(xpath = self._NoAccessDocsX).find(self)
            '#存在no access 的文件'
            noaccess = []
            DocListEle = Elements(xpath="//span[contains(text(),'NoAccess')]/../..//preceding-sibling::span").find(self)
            for ele in DocListEle:
                DocName = ele.text;
                noaccess.append(DocName)
            logging.info(f'τ Pending docs :{noaccess}...')
            Element(id_=self._shareConfirmID).click();
            return noaccess



        else:
            '证明文件中全部都是 完成 出状态 的文件可以直接提交'

            return 0

    def confirmShare(self):
        """

        :return: 1.You don't have permission for this document, please request permission first
                 2.Please upload relevant documents first!
                 3.Share Success!
        """
        '确认分享之后的一些情况'
        Element(id_= self._shareConfirmID).click()
        Message = Element(xpath=self._alertMessage).text
        self.sleep(3)

        ''
        return Message




    def ReturnSharedDocuments(self):
        '返回页面中展示的数据'
        shareDocument = Element(xpath='//*[@id="component-toolTip-visibilityChange"]').text

        Recent_Product = Element(xpath='//td/div/span',index=0).text
        #get_attribute('value')

        d=dict()
        d['shareDocument']=shareDocument
        d['Recent_Product']=Recent_Product

        logging.info(f"OP ✅ ReturnSharedDocuments :{shareDocument}，Recent_Product：【{Recent_Product}】")

        return d