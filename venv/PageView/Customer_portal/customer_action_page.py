from poium import Page, Element,Elements
import time
from poium.common import logging
import allure


class ActionPage(Page):
    '关于action的相关操作'

    '基础定位'
    _rep_nums = 'rep-nums'
    _Next = "//span[contains(text(),'Next')]"
    rep_name = Element(class_name=_rep_nums)
    Next = Element(xpath=_Next,index=1);
    _alert_error='//*[contains(@class,"el-message el-message--error")]'
    reject_button=Element(xpath='//button/span[contains(text(),"REJECT") or contains(text(),"Reject")]')

    '一些按钮控件'

    def open_Action_Page(self):

        self.wait_page_load_timeout(10)
        Element(xpath="//a/li[text()='Actions']").click();
        time.sleep(3)
        logging.info(f"OP ✅ OPEN MY ACTIONS PAGE")

    def open_Home_Page(self):

        Element(xpath="//a/li[text()='Home']").click();
        self.wait_page_load_timeout(3)
        logging.info(f"OP ✅ OPEN MY Home PAGE")

    '选择rep'
    def Select_rep(self,*args,Type='online'):
        if Type == 'online':
            for i in range(0,len(args)):
                repName = '//div[contains(text(),"{}")]'.format(args[i])
                Element(xpath = repName).click()

        if Type=='local':
            Element(id_ = 'el-collapse-head-3667').click()
            for i in range(0, len(args)):
                repName = '//div[contains(text(),"{}")]'.format(args[i])
                Element(xpath = repName).click()
        Element(xpath = self._Next).click();self.sleep(3)

    '打开特定请求的action 传入action名称'
    def open_Purpose(self,Purpose):
        '''传入 Purpose name 以此来打开对应的Purpose '''

        self.open_Action_Page()
        self.sleep(3)
        Purpose_name_xpath='//div[contains(text(),"{}")]'.format(Purpose)
        if Element(xpath=Purpose_name_xpath).is_exist():
            Element(xpath=Purpose_name_xpath).click()
            self.wait_page_load_timeout(5)
            logging.info(f"OP ✅ OPEN new Purpose sever name :{Purpose}")
            self.sleep(3)

        else:
            logging.error(f'No find this Purpose named :{Purpose}')
            return False
    '同意action'
    def consent_action(self):
        '''consent button of action'''
        consent_but="//button/span[contains(text(),'Consent') or contains(text(),' CONSENT')]/.."

        if Element(xpath = consent_but).is_enabled()==False:
            logging.info(f'Consent button can not be click')
            return False

        else:
            #可点击 分为两种情况：点击成功，点击失败
            Element(xpath=consent_but).click()
            if Element(xpath = self._alert_error).is_exist():
                return Element(xpath = self._alert_error).text

            if Element(xpath="//span[contains(text(),'Yes')]").is_exist():
                Element(xpath="//span[contains(text(),'Yes')]").click()
                time.sleep(3)

    '关闭action弹窗'
    def action_close(self):
        Element(xpath='//span[contains(text(),"Action")]/../button').click()
        self.sleep(3)

    '上传文档通用函数--自动上传所有pending的文档'
    def upload_action_doc(self,DocPath,dataTest,username,*args):
        """
        :param DocPath: 数据文件根本目录
        :param dataTest: Execl 文件目录
        :args 传入特定的文件名称
        :return: 无特殊返回
        """
        DOCPATH=DocPath#跟目录
        AllDoc=dataTest#路径

        DocList_AddDateOfIssue=['Certified Document', 'Utility Bill', 'Bank / Financial Statement','Certified Photo ID',
                                'Test for Ind1', 'Current Bank Account Statement', 'Current Mortgage Statements', 'Current Credit Union Statement', 'Current Loan Statements', 'Supplier Statements', 'Current Social Welfare Payslips', 'Employment earnings summary', 'Share Certificates or Annual Statements']

        time.sleep(3)
        '''搜索并且上传action中文件状态是pending的文件'''
        elems=Elements(xpath="//span[contains(text(),'Pending')]",timeout=5).find(self);time.sleep(3)
        if elems!=[]:

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
                    Element(id_='document-upload-regular-inputList-item-not-518').send_keys(username,clear=True)
                    Element(id_='document-upload-regular-inputList-item-not-517').send_keys(username,clear=True)
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


    'Update document'
    def UpdateDocInAction(self):
        update_button=Element(xpath='//button/span[contains(text(),"UPDATE") or contains(text(),"Update")]')
        if update_button.is_exist():
            update_button.click()
            #下面是更新文件通用函数
            Doc_type = Element(id_='document-upload-docVault-select').get_attribute('value')
            cur_date = time.strftime("%d/%m/%Y")



    '判断Action文档状态'
    def returnDocStatus(self,*args):
        document=dict()

        for i in range(0, len(args)):
            DocTypesStatue ='//span[contains(text(),"{}")]/../../../../div[2]//span'.format(args[i])
            status = Element(xpath=DocTypesStatue).text
            document[args[i]] = status
            logging.info(f'Document {document[args[i]]} status is {status}')

        return document

    '拒绝Action'
    def reject_action(self):

        Element(xpath='//button/span[contains(text(),"REJECT") or contains(text(),"Reject")]').click()
        Element(xpath="//span[contains(text(),'Yes')]").click()
        self.sleep(3)
        logging.info(f'reject_action success')

    '''	Add Authorised Representatives'''
    def AddOnlineRep(self,*args):
        """
        添加在线用户
        :param args: 传入的REP email 元祖，未知数量。
        :return:
        """
        self.open_Action_Page()
        self.open_Purpose("Add Authorised Representatives")
        _OnlineVaultX = '//h2[contains(text(),"Online vault")]'
        _Continue = '//span[contains(text(),"Continue")]'
        _InviteButton = '//span[contains(text(),"Invite")]'

        Element(xpath=_OnlineVaultX).click()
        Element(xpath= _Continue).click();self.sleep(3)

        for idNum,Email in enumerate(args):
            _RepInput = '//input[@id="authRepEmailInput{}"]'.format(idNum+1)
            print(_RepInput)

            Element(xpath=_RepInput,describe='填写Rep邮箱').send_keys(Email)
        logging.info(f'Input REP Emails {args} success')
        Element(xpath= _Continue).click()
        Element(xpath = _InviteButton).click();self.sleep(2)
        assert Element(xpath = '//div[contains(text(),"Add Authorised Representatives")]').is_exist()==False
        logging.info(f'Invite Reps send success')

    '''Confirmation needed as an Authorised representative'''
    '''Action type ,'''
    confirmBeRepFirstConsent = Element(id_='ActionType35-consent-button')
    docPermissionConfirm =Element(id_ ='ActionDocumentPermissionDialog-confirm-button')

    def ConfirmAuteRep_With_No_Doc(self):
        self.open_Action_Page()
        self.open_Purpose('Confirmation needed as an Authorised representative')

        _NoData = '//span[contains(text(),"No Data")]'

        self.confirmBeRepFirstConsent.click();self.sleep(3)
        try:
            if Element(xpath= _NoData).is_exist()==True:
                allure.step('The action named {}from the corresponding corporate company will be disappeared.'.format('as an Authorised representative'))
                self.docPermissionConfirm.click();self.sleep(3)
                if self.open_Purpose('Confirmation needed as an Authorised representative')==False:
                    logging.success(f'Authorised representative Processed successfully')

                else:
                    logging.error(f'The user Exist Doc')
        except:
            logging.error(f'Action processing failed')


    def ConfirmAuteRep_WithDocs(self,*args):
        """
        支持多个文档进行文件选权限的操作
        share给对应的公司
        :param args: 文档元祖
        :return: 0
        """

        self.open_Action_Page()
        self.open_Purpose('Confirmation needed as an Authorised representative')
        _ActionConsent = 'ActionType35-consent-button'



        self.confirmBeRepFirstConsent.click();self.sleep(3)
        try:
            if args!=[]:#存在需求分享给corp的文件

                for docWantShare in args:
                    _DocName = '//span[contains(text(),"{}")]'.format(docWantShare)

                    if Element(xpath=_DocName).is_exist():

                        _DocCheckInput = '//span[contains(text(),"{}")]/following-sibling::span/span/label/span/input/..'.format(docWantShare)
                        Element(xpath =_DocCheckInput).click()
                    else:
                        logging.error(f'The user no Exist {docWantShare} Doc in this page')
                self.docPermissionConfirm.click()
                Element(xpath = "//span[contains(text(),'Yes')]").click();self.sleep(3)

            else:
                self.docPermissionConfirm.click();self.sleep(3)

            if self.open_Purpose('Confirmation needed as an Authorised representative') == False:
                logging.success(f'Authorised representative Processed successfully')
            else:
                logging.error(f'Action processing failed')
        except:
            logging.error('Action processing failed')


    '判断文档是否授权给公司用户'
    def assertDocHasBeenShared(self,Doc):

        Doc_is_check_and_disable = '//span[contains(@class,"is-disabled is-checked")]/../../../..//..//../../../div/preceding-sibling::div[1]/span/span[contains(text(),"{}")]'.format(
            Doc)
        if Element(xpath=Doc_is_check_and_disable).is_exist():
            _versioninformation = '(//span[contains(text(),"{}")]/../..)[2]/span[2]/span'.format(Doc)
            versioninformation = Element(xpath=_versioninformation, describe='已经授权的版本信息').text

            logging.info(f'{Doc} This doc has been share with OBC')
            return True,versioninformation
        else:
            return False

    'Type 13 Document Permission Request'
    def Confirm_DocPermission(self,DocType,reason):
        _SendNote = '//div[contains(text(),"{}")]'.format(reason)
        _PermissonDoc = '//div[contains(text(),"{}") and @class="list-item-left-text"]'.format(DocType)

        if Element(xpath= _SendNote).is_exist():
            Element(xpath =_PermissonDoc).is_exist()
            self.consent_action()


        else:
            logging.error(f'Not find note: {reason}')





































