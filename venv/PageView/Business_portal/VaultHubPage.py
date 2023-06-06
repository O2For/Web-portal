from poium import Page, Element,Elements
import time
from poium.common import logging

class VaultHub(Page):
    Vault_HubTitle = Element(xpath = '//span[contains(text(),"Vault Hub")]')

    def openVaultHub(self):
        self.Vault_HubTitle.click();
        self.sleep(3)

    '搜索功能 '
    def searchCustomer(self,**kwargs):
        _nameinput = 'customer-searchForm-customerName-input'
        _emailinput = 'customer-searchForm-email-input'
        customerTypeselect = 'customer-searchForm-userType-select'

        ResultEmail='//*[contains(text(),"{}")]'.format(kwargs['Email'])

        Element(id_ = _emailinput).send_keys(kwargs['Email'],clear=True)
        Element(id_=_emailinput).enter();self.sleep(5)

        searchResultEmail = Element(xpath =ResultEmail).text
        searchResultCustomerType = Element(xpath ='//*[contains(@class,"el-table_3_column_13    el-table__cell")]/div//div').text
        searchResultVaultType =Element(xpath ="//*[contains(@class,'el-table_3_column_15    el-table__cell')]/div//div").text

        d=dict()
        d['searchResultEmail'] = searchResultEmail
        d['searchResultCustomerType'] = searchResultCustomerType
        d['searchResultVaultType'] = searchResultVaultType

        return d


    def ClickSearchList(self,CustomerEmail):
        ResultEmail = '//div[contains(text(),"{}")]'.format(CustomerEmail)
        Element(xpath =ResultEmail,index=0).click();self.sleep(3)

class Drawer(VaultHub):

    _porfile = '//button[contains(@class,"v8-button is-medium is-secondary is-icon-only")][1]'
    _onlineVault ='//button[contains(@class,"v8-button is-medium is-secondary is-icon-only")][2]'
    _localVault ='//button[contains(@class,"v8-button is-medium is-secondary is-icon-only")][3]'
    _riskCase = '//button[contains(@class,"v8-button is-medium is-secondary is-icon-only")][4]'
    _connectionCase = '//button[contains(@class,"v8-button is-medium is-secondary is-icon-only")][5]'
    _xButton = '//button[contains(@class,"v8-button is-medium is-secondary is-icon-only")][7]'
    queryid = 'newProfile-doQuery'

    def closeDrawer(self):
        Element(xpath=self._xButton).click();self.sleep(3)


    # 'OnlineVault Query'
    'OnlineVault'
    def checkOnlineVault(self):
        Element(xpath = self._onlineVault).click();self.sleep(3)

        'send query'
    def Query(self,Purpose,Product,ConnectionCase=None,Note=None,**kwargs):

        connect_case_inputbox = '//*[@id="newProfile.queryModal.queryForm.caseRefId.select"]'
        Element(id_=self.queryid).click()
        Element(id_='newProfile.queryModal.queryForm.purpose.select', index=0, describe='purpose').click()
        if Purpose=='New Product/Service':

            Element(xpath = '//span[contains(text(),"New Product/Service")]', describe='New Product/Service').click()
            Element(id_='newProfile.queryModal.queryForm.productId.select',index=0,describe='Product/Service').send_keys(Product)
            Element(xpath='//li[@id="newProfile.queryModal.queryForm.productId.select.option1"]').click()

        else :
            if Purpose=='Document(s) is/are not listed':
                Element(xpath = '//span[contains(text(),"Document(s) is/are not listed")]', describe='Document(s) is/are not listed').click()
            if Purpose=='Access required to another document':
                Element(xpath = '//span[contains(text(),"Access required to another document")]', describe='Access required to another document').click()
            if Purpose=='Document Out of Date':
                Element(xpath = '//span[contains(text(),"Document Out of Date")]', describe='Document Out of Date').click()
            if Purpose=='Document Unclear or Obscured':
                Element(xpath = '//span[contains(text(),"Document Unclear or Obscured")]', describe='Document Unclear or Obscured').click()

            Element(id_='newProfile.queryModal.queryForm.productId.select', index=0,describe='Product/Service').click()
            product_name = '//span[contains(text(),"{}")]'.format(Product)
            Element(xpath=product_name,describe='inputbox').click()
            Element(xpath=connect_case_inputbox).click()
            Element(id_="newProfile.queryModal.queryForm.caseRefId.select.option0").click()

        if  Note==None:
            Element(id_='newProfile.queryModal.queryForm.note', index=0, describe='Note').clear()

    def QueryInfo_individual(self,*queryDoc):
        document_input_box = '//input[contains(@id,"newProfile.queryModal.queryForm.adhocDocTypes.select3")]'
        ExpendQueryinfor = '//span[contains(text(),"Query Info")]'
        Element(xpath=ExpendQueryinfor,describe='ExpendQueryinfor').click()
        Element(xpath=document_input_box,describe='Document input box').click()

        for doc in queryDoc:
            docname='//span[contains(text(),"{}")]'.format(doc)
            Element(xpath=docname).click()
        Element(xpath=document_input_box, describe='Document input box').click()

    def QueryInfo_WithRep(self,**queryDoc):
        """

        :param queryDoc: 二维数组包括：用户类型，用户名称，用户选择的文档
        fun(corp=[['corpEmail'],['BOD','NID']])
        :return:
        """
        '基础定位'
        document_input_box = '//input[contains(@id,"newProfile.queryModal.queryForm.adhocDocTypes.select2")]'
        rep_input_box = '//input[contains(@id,"newProfile.queryModal.queryForm.representativeId.select")]'
        rep_document_input = '//input[contains(@id,"newProfile.queryModal.queryForm.adhocRepDocs.select")]'
        rep_doc_foldcalss ='//*[contains(@class,"el-select__caret el-input__icon el-icon-arrow-up is-reverse")]'

        ExpendCompanyDocument = '//span[contains(text(),"Company")]'

        ExpendAuthorisedRep = '//*[contains(@class,"el-collapse-item__header")]/span[contains(text(),"Authorised Rep")]'

        '展开infro里面的框'
        Element(xpath=ExpendCompanyDocument,describe='ExpendCompanyDocument').click()
        Element(xpath=ExpendAuthorisedRep, describe='ExpendAuthorisedRep').click()

        '输入框定位'
        #

        for QueryUserType in queryDoc.keys():
            if QueryUserType =='Corporate':
                Element(xpath=document_input_box, describe='Document input box').click()
                for doc in queryDoc['Corporate'][1]:
                    docname = '//span[contains(text(),"{}")]'.format(doc)
                    Element(xpath=docname).click()
                Element(xpath=document_input_box, describe='Document input box').click()

            if QueryUserType =='Fund':
                pass

            if QueryUserType =='Individual':
                Element(xpath=rep_input_box).click()
                queryRep=",".join(map(str,queryDoc['Individual'][0]))
                repname = "//span[contains(text(),'{}')]".format(queryRep)
                Element(xpath=repname).click()

                Element(xpath=rep_document_input).scrollDownIntoView()
                Element(xpath=rep_document_input).click();self.sleep(3)

                for doc in queryDoc['Individual'][1]:
                    docname = '//span[contains(text(),"{}")]'.format(doc)
                    Element(xpath=docname).click()
                Element(xpath = rep_doc_foldcalss).click()

    def QuerySend(self):
        Element(id_='newProfile.queryModal.btn.send',index=0,describe='Send query button').click();self.sleep(3)

    #OnlineVault See document
    def CorpDocumentCategory(self,docName):
        Company_Information=['Board Resolution Document','Memorandum of Association',
                             'Certificate of Incorporation','Company Constitution',
                             'Filed Corporate Accounts','Company Ownership Structure',
                             'Other (Company Information)','Fund Prospectus','Financial Statements',
                             'Tax Structuring Memo','Register Of Members','Offering Memo']
        Authorised_Representatives=['Authorised Signatory List (Headed Paper)','Official List of Company Directors',
                                    'Other (Authorised Representatives)']
        Ownership_Information=['Beneficial Ownership/Control','Details of shareholding/ownership structure',
                               'Other (Ownership Information)']

        if docName in Company_Information:
            return 'Company Information'
        if docName in Authorised_Representatives:
            return 'Authorised Representatives'
        if docName in Ownership_Information:
            return 'Ownership Information'

    def IndividualDocumentCategory(self,docName):
        Photo_ID=['Passport', 'Driving Licence', 'National ID Card',
                  'Other Proof of Identity Documentation', 'Certified Photo ID']
        Proof_of_Address=['Other(Proof of Address)', 'Utility Bill',
                          'Bank / Financial Statement', 'Test for Ind1', 'Certified Address']
        Financial_Information=['Salary Certificate', 'Pay Slips', 'Other Source of Funds Documentation',
                               'Test for Ind3']
        Other=['Other', 'Test for Ind2']
        Medical_Documents=['Covid Vaccine Certificate']
        Taxes=['Recent Income Tax/Self-Assessment Statement', 'Revenue Commissioner statement']
        Statements=['Current Bank Account Statement', 'Current Credit Union Statement', 'Current Mortgage Statements',
                    'Current Loan Statements', 'Supplier Statements']
        EarningsFinancial_Information=['Current Social Welfare Payslips', 'Employment earnings summary',
                                       'Share Certificates or Annual Statements']
        Correspondence=['Correspondence from mortgage lender', 'Correspondence from pension provider showing value']
        Assets=['Valuations of Significant Items of Value', 'Any contingent assets', 'Any contingent liabilities']

        if docName in Photo_ID:
            return 'Photo ID'
        if docName in Proof_of_Address:
            return 'Proof of Address'
        if docName in Financial_Information:
            return 'Financial Information'
        if docName in Other:
            return 'Other'
        if docName in Medical_Documents:
            return 'Medical Documents'
        if docName in Taxes:
            return 'Taxes'
        if docName in Statements:
            return 'Statements'
        if docName in EarningsFinancial_Information:
            return 'Earnings / Financial Information'
        if docName in Correspondence:
            return 'Correspondence'
        if docName in Assets:
            return 'Assets'

    def selectUserType(self,userType):

        if userType=='Corporate'or userType=='Fund':
            Element(xpath='//div[contains(@id,"tab-1")]').click();self.sleep(3)
            return
        if userType=='Authorised Representatives':
            Element(xpath='//div[contains(@id,"tab-2")]').click();self.sleep(3)
            return
        if userType=='Inactive Representatives':
            Element(xpath='//div[contains(@id,"tab-2")]').click();self.sleep(3)
            return

    def switchRepDocPage(self,RepName):
        repNameInputbox='//input[@id="newProfile-handleChangeRep2"]'
        reName='//span[contains(text(),"{}")]'.format(RepName)

        Element(xpath=repNameInputbox).click()
        Element(xpath=reName).click()


    def is_ExistDoc(self,Category,docName):
        CategoryIsHideXpath ='//*[contains(text(),"{}")]/following-sibling::div'.format(Category)
        ArrowRightID ='newProfile-doOnlineRight'

        if Element(xpath=CategoryIsHideXpath).text =='Show':
            Element(xpath=CategoryIsHideXpath).click() #如果你搜索的文档类型是隐藏的 ，那么就展开他
            self.sleep(3)
        elif Element(xpath=CategoryIsHideXpath).text =='Hide':
            pass
        docXpath = '//*[contains(text(),"{}") and contains(@class,"el-tooltip type")]'.format(docName)
        if Element(xpath=docXpath).is_exist():
            return True
        else:
            if Element(id_=ArrowRightID, index=0).is_exist():
                while Element(id_=ArrowRightID, index=0).is_enabled():
                    Element(id_=ArrowRightID, index=0).click();
                    self.sleep(3)
                    if Element(xpath=docXpath).is_exist():
                        return True
                    else:
                        continue
            return False
    def clickDoc(self,docName):
        docXpath = '//*[contains(text(),"{}") and contains(@class,"el-tooltip type")]'.format(docName)
        imgDoc='//img[contains(@id,"newProfile.view.scaleImage.contextmenu")]'
        Element(xpath=docXpath).click();self.sleep(3)
        if Element(xpath=imgDoc).is_exist():
            logging.info(f'{docName} is exist and has access')
            return True
        else:
            logging.error(f'{docName} has no access to click')
            return False

    def closeViewDocument(self):
        xButton='//span[contains(text(),"View Document")]/following-sibling::button'
        Element(xpath=xButton).click();self.sleep(3)















    #ConnectionCases Operation

    def checkConnectionCases(self):
        Element(xpath = self._connectionCase).click()
        self.sleep(3)

    def ClickCase(self,Product,**kwargs):
        _prodcutname = '//span[contains(text(),"{}")]'.format(Product)
        Element(xpath = _prodcutname).click();self.sleep(3)

    def showConnection(self):
        '展开link connections, 返回picName'
        LinkedConnectionTitle = '//*[contains(text(),"Linked Connections")]'
        Element(xpath = LinkedConnectionTitle,describe='展开link').click()
        d=dict()
        linkname=Element(class_name = 'picName').text
        d['linkname'] = linkname

        return d

    '查看被分享的文件内容'
    def LinkedConnections(self, *args):


        ViewDocid = 'newProfile.caseModal-val.docList.fileName'
        imgDOCid = '//img[contains(@id,"dashboard.view.img2.contextmenu")]'
        closeDocdisplay = '/html/body/div[4]/div/div[1]/button'

        for i in range(0, len(args)):
            docname = '//div[contains(text(),"{}")]'.format(args[i])
            if Element(xpath=docname).is_exist():
                Element(id_=ViewDocid, index=i, describe='查看分享的文件内容').click();
                self.sleep(5)
                if Element(xpath=imgDOCid).is_exist():
                    logging.info(f'Doc {args[i]} display right')
                    Element(xpath=closeDocdisplay).click()
                    self.sleep(3)
                    pass
                else:
                    logging.warning(f'Doc {args[i]} display error')
            else:
                logging.warning(f'No Find doc {args[i]} in link connections details')


        '关闭connection 的弹窗'

    def closeConnectioncase(self):
        xbutton = '/html/body/div[2]/div/div[1]/button/i'
        Element(xpath=xbutton).click();
        self.sleep(3)














