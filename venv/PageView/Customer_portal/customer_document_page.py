from poium import Page, Element,Elements
import time
from poium.common import logging

class Document(Page):

    DocList_AddDateOfIssueCorp = ['Filed Corporate Accounts', 'Company Ownership Structure',
                                  'Test for Corp1', 'Test for Corp2']
    OrtherInforCorp = ['Test for Corp1']

    DocList_AddDateOfIssueInd = ['Certified Document', 'Utility Bill', 'Bank / Financial Statement',
                                 'Test for Ind1', 'Current Bank Account Statement', 'Current Mortgage Statements',
                                 'Current Credit Union Statement', 'Current Loan Statements', 'Supplier Statements',
                                 'Current Social Welfare Payslips', 'Employment earnings summary',
                                 'Share Certificates or Annual Statements']
    cur_date = time.strftime("%d/%m/%Y");


    'Document page opreate'
    def JumpDocumentPage(self):
        Element(xpath="//li[contains(text(),'Documents')]").click();self.sleep(3)
    '在ind 文档页面上传文档'
    def UploadDocDocumentPage_ind(self,DocPath,dataTest,DocType):
        'UPLOAD doc opreate'
        DOCPATH = DocPath  # 跟目录
        AllDoc = dataTest  # 路径



        _UploadIconId = 'document-page-upload-button'
        _docTypeId = 'document-upload-docVault-select'
        _inputdocName = '//li/span[contains(text(),"{}")]'.format(DocType)
        _confimeDoc = "//p[contains(text(),'{}')]".format(DocType)
        _confirmDocUploadSuccess = '//div[contains(text(),"{}")]'.format(DocType)
        '跳转到document page'
        self.JumpDocumentPage()


        Element(id_=_UploadIconId,describe='点击uplolad 按钮').click();
        Element(id_=_docTypeId,describe='点击下拉框').click();
        Element(xpath=_inputdocName,describe=_inputdocName).click();

        Element(xpath="//em/following-sibling::input").send_keys(DOCPATH + AllDoc[DocType]);
        self.sleep(3)
        if DocType == 'Passport':
            Element(id_='document-upload-local-doc-submit-button', describe='submit', timeout=3).click();
            self.sleep(5)  # 等待regular

            Element(id_='document-upload-regular-inputList-item-not-513',describe='修改到期时间').send_keys(self.cur_date, clear=True)
            Element(id_='document-upload-regular-inputList-item-not-514',describe='修改 出生时间').send_keys('01/01/1999', clear=True)
            Element(xpath="//BUTTON/span[contains(text(),'Confirm')]",
                    describe='# 确认regular 证件识别结果').click();self.sleep(5)
            if Element(xpath="//span[contains(text(),'Update Profile Details?')]",index=1).is_exist():
                Element(xpath="//span[contains(text(),'Yes, I would')]",index=1).click();
            else:
                pass
            self.sleep(2)

        else:
            if DocType == 'National ID Card':
                Element(xpath="//label[contains(text(),'Date of Expiry')]/..//input", describe='Date of Expiry').send_keys(
                    self.cur_date)


            elif DocType in self.DocList_AddDateOfIssueInd:
                Element(xpath="//label[contains(text(),'Date of Issue')]/..//input", describe='Date of Issue').send_keys(
                    '01/01/1999')

            Element(id_='document-upload-local-doc-submit-button', describe='submit', timeout=3).click();self.sleep(5)

        assert Element(xpath=_confirmDocUploadSuccess), logging.info(f'{DocType} UPLOAD successfully in document page')
        return True

    '在Ind文档页面更新 文档'
    def UpdateDocDocumentPage_Ind(self, DocPath, dataTest, NeedUpadteDocType):
        _UpdateID = 'document-page-updateOne-button381'
        _UpdatedrownID = 'document-upload-docVault-select'
        _confirmDocUploadSuccess = '//div[contains(text(),"{}")]'.format(NeedUpadteDocType)
        DOCPATH = DocPath  # 跟目录
        AllDoc = dataTest  # 路径
        self.JumpDocumentPage()
        Element(xpath=_confirmDocUploadSuccess)

        try:
            if Element(xpath=_confirmDocUploadSuccess).is_exist() == True:
                Element(id_=_UpdateID, index=0, describe='点击更新按钮').click()
            try:
                catchDocName = Element(id_=_UpdatedrownID, describe='获取当前更新的文件名称').get_attribute('value')
                if NeedUpadteDocType == catchDocName:

                    Element(xpath="//em/following-sibling::input", describe='输入需要上传的文件路径').send_keys(
                        DOCPATH + AllDoc[NeedUpadteDocType]);
                    self.sleep(3)

                    if NeedUpadteDocType =='Passport':
                        Element(id_='document-upload-local-doc-submit-button', describe='submit', timeout=3).click();
                        self.sleep(5)  # 等待regular

                        Element(id_='document-upload-regular-inputList-item-not-513', describe='修改到期时间').send_keys(
                            self.cur_date, clear=True)
                        Element(id_='document-upload-regular-inputList-item-not-514', describe='修改 出生时间').send_keys(
                            '01/01/1999', clear=True)
                        Element(xpath="//BUTTON/span[contains(text(),'Confirm')]",
                                describe='# 确认regular 证件识别结果').click();self.sleep(3)
                        if Element(xpath="//span[contains(text(),'Update Profile Details?')]", index=1).is_exist():
                            Element(xpath="//span[contains(text(),'Yes, I would')]",index=1).click();
                        else:
                            pass
                        self.sleep(5)

                    else:
                        if NeedUpadteDocType == 'National ID Card':
                            Element(xpath="//label[contains(text(),'Date of Expiry')]/..//input",
                                describe='Date of Expiry').send_keys(self.cur_date)

                        elif NeedUpadteDocType in self.DocList_AddDateOfIssueInd:
                            Element(xpath="//label[contains(text(),'Date of Issue')]/..//input",describe='Date of Issue').send_keys('01/01/1999')

                        else:
                            pass

                        Element(id_='document-upload-local-doc-submit-button', timeout=3, describe='确认提交文件').click();
                        self.sleep(3)
                    return True

            except:
                logging.error(f'updated file{NeedUpadteDocType} is inconsistent with the uploaded file{catchDocName}')
        except:
            logging.error(f'This document {NeedUpadteDocType} does not exist')

    '在Ind文档页面删除 文档'
    def DeleteDocDocumentPage_IND(self,DocPath,dataTest,NeedDeletDocDocType):

        _confirmDocUploadSuccess = '//div[contains(text(),"{}")]'.format(NeedDeletDocDocType)
        _DeleteButton = 'document-page-updateOne-button381'
        try:
            Element(xpath = _confirmDocUploadSuccess,describe='查看是否存在此文件').is_exist()
            Element(id_=_DeleteButton,describe='点击删除按钮',index=1).click()
            Element(xpath = '//span[contains(text(),"Yes")]',describe='确认删除按钮').click();self.sleep(3)
            if Element(xpath = _confirmDocUploadSuccess,describe='查看是否存在此文件').is_exist()==False:

                logging.info(f'Delete {NeedDeletDocDocType} successfully')
                return True
            else:
                logging.error(f'Document{NeedDeletDocDocType} deletion failed ')
        except:
            logging.error(f'The doc {NeedDeletDocDocType},not exist')







    '在CORP 文档页面上传文档'
    def UploadDocDocumentPage_Corp(self,DocPath,dataTest,DocType):
        'UPLOAD doc opreate'
        DOCPATH = DocPath  # 跟目录
        AllDoc = dataTest  # 路径


        _UploadIconId = 'document-page-upload-button'
        _docTypeId = 'document-upload-modal-docVault-select'
        _inputdocName = '//li/span[contains(text(),"{}")]'.format(DocType)
        _confimeDoc = "//p[contains(text(),'{}')]".format(DocType)
        _confirmDocUploadSuccess = '//div[contains(text(),"{}")]'.format(DocType)

        '跳转到document page'
        Element(xpath="//li[contains(text(),'Documents')]",describe='首先呢跳转到document page').click();self.sleep(3)

        Element(id_=_UploadIconId,describe='点击uplolad 按钮').click();
        Element(id_=_docTypeId,describe='点击选择文件的下拉框',index=0).click();
        Element(xpath=_inputdocName,describe=_inputdocName).click();

        Element(xpath="//em/following-sibling::input",describe='上传文档').send_keys(DOCPATH + AllDoc[DocType]);
        self.sleep(3)

        if DocType in self.DocList_AddDateOfIssueCorp:

            Element(xpath="//label[contains(text(),'Date of Issue')]/..//input", describe='Date of Issue').send_keys(
                '01/01/1999')
            if DocType not in self.OrtherInforCorp:
                pass
            else:
                Element(id_='document-upload-modal-input-doc', describe='input copr name doc need').send_keys('Other')
        else:
            pass

        Element(id_='document-upload-local-doc-submit-button', describe='submit', timeout=3).click();
        time.sleep(3)
        assert Element(xpath=_confirmDocUploadSuccess), logging.info(f'{DocType} UPLOAD successfully in document page')
        return True

    '在Corp文档页面更新 文档'
    def UpdateDocDocumentPage_Corp(self,DocPath,dataTest,NeedUpadteDocType):
        _UpdateID = 'document-page-updateOne-button380'
        _UpdatedrownID = 'document-upload-modal-docVault-select'
        _confirmDocUploadSuccess = '//div[contains(text(),"{}")]'.format(NeedUpadteDocType)
        DOCPATH = DocPath  # 跟目录
        AllDoc = dataTest  # 路径
        self.JumpDocumentPage()
        Element(xpath=_confirmDocUploadSuccess)

        try:
            if Element(xpath = _confirmDocUploadSuccess).is_exist()==True:
                Element(id_=_UpdateID,index=0,describe='点击更新按钮').click()
            try:
                catchDocName =  Element(id_=_UpdatedrownID,describe='获取当前更新的文件名称').get_attribute('value')
                if  NeedUpadteDocType == catchDocName:

                    Element(xpath="//em/following-sibling::input",describe='输入需要上传的文件路径').send_keys(DOCPATH + AllDoc[NeedUpadteDocType]);self.sleep(3)

                    if NeedUpadteDocType in self.DocList_AddDateOfIssueCorp:
                        Element(xpath="//label[contains(text(),'Date of Issue')]/..//input",escribe='Date of Issue').send_keys('01/01/1999')
                        if NeedUpadteDocType not in self.OrtherInforCorp:
                            pass
                        else:
                            Element(id_='document-upload-modal-input-doc',describe='input copr name doc need').send_keys('Other')

                    Element(id_='document-upload-local-doc-submit-button', timeout=3,describe='确认提交文件').click();self.sleep(3)
                return True

            except:
                logging.error(f'updated file{NeedUpadteDocType} is inconsistent with the uploaded file{catchDocName}')
        except:
            logging.error(f'This document {NeedUpadteDocType} does not exist')

    '在Corp文档页面删除 文档'
    def DeleteDocDocumentPage_Corp(self,DocPath,dataTest,NeedDeletDocDocType):

        _confirmDocUploadSuccess = '//div[contains(text(),"{}")]'.format(NeedDeletDocDocType)
        _DeleteButton = 'document-page-updateOne-button380'
        try:
            Element(xpath = _confirmDocUploadSuccess,describe='查看是否存在此文件').is_exist()
            Element(id_=_DeleteButton,describe='点击删除按钮',index=1).click()
            Element(xpath = '//span[contains(text(),"Yes")]',describe='确认删除按钮').click();self.sleep(3)
            if Element(xpath = _confirmDocUploadSuccess,describe='查看是否存在此文件').is_exist()==False:

                logging.info(f'Delete {NeedDeletDocDocType} successfully')
                return True
            else:
                logging.error(f'Document{NeedDeletDocDocType} deletion failed ')
        except:
            logging.error(f'The doc {NeedDeletDocDocType},not exist')















