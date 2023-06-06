from poium import Page, Element,Elements
import time
from poium.common import logging

class Documents_Corp(Page):

    _docEmpty = '//p[contains(text(),"Your vault is empty")]'
    latestV = Element(id_='document-view-modal-select')
    PreviousV =Element(id_='document-view-modal-select-item1')


    _requestAccess = 'document-view-modal-request-access-button'

    _note = 'document-request-modal-textarea'
    _confirmNote = 'document-request-modal-confirm-button'
    requestAccessButton = Element(id_=_requestAccess)
    note = Element(id_=_note)
    confirmNote = Element(id_=_confirmNote)

    #样式转换器
    _gridActive = "document-page-change-type-btn-grid-two"
    _listActive = 'document-page-change-type-btn-list-one'

    '关闭文档展示页面'
    def close_doc_window(self):
        Element(class_name='el-dialog__headerbtn').click();
        self.sleep(3)

    '跳转到document 页面'
    def open_Documents(self):
        Element(xpath= '//li[contains(text(),"Documents")]').click();self.sleep(3)

    '打开rep的下拉框'
    def open_Representatives(self):
        _Representatives = '//div[contains(text(),"Representatives")]'

        Element(xpath= _Representatives).click();self.sleep(1)

    '打开指定的 online ep文档列表'
    def open_OnlineRepPage(self,repName):

        _onlineClass='el-radio-button__inner'
        _onlineRepName='//p[contains(text(),"{}")]'.format(repName)

        Element(class_name=_onlineClass,index=0).click()
        Element(xpath=_onlineRepName).click();self.sleep(3)
        return True

    '打开指定的 Inactive ep文档列表'

    def open_InactiveRepPage(self,repName):

        _onlineClass='el-radio-button__inner'
        _InactiveRepName='//p[contains(text(),"{}")]'.format(repName)

        Element(class_name=_onlineClass,index=2).click()
        Element(xpath=_InactiveRepName).click();self.sleep(3)

    '打开指定文件的详情页面'
    def check_repDocDetails(self,doc_type):
        _docType ='//div[contains(text(),"{}")]'.format(doc_type)
        if Element(xpath = _docType).is_exist():
            Element(xpath = _docType).click();self.sleep(3)
            _version = 'document-view-modal-select'
            currentV = Element(id_=_version,index=0).get_attribute('value')

            return currentV
        else:
            logging.info(f'{doc_type} No Exist')
            return False

    '判断列表是否有文档存在'
    def NOdoc_isExist(self):
        if Element(xpath =self._docEmpty).is_exist()==True:
            return True
        else:
            return False

    '判断这个版本的文档是否有权限查看'
    def docIs_NoAccess(self):

        if Element(xpath = "//div[contains(text(),'No Access')]").is_exist()==True:
            logging.info('Doc Is_NoAccess')
            return True

        if Element(xpath ='//*[@class="imageDoc"]',index=1).is_exist()==True:
            logging.info('docHas_Access')
            return False

    '判断当前的文件是否带有New的标签 以此来表示其是否具有新上传的版本'
    def check_NewLabel(self,docType):


        _Docl_withNewLabel = '//*[@class="docNew svg-icon"]/../.././div[2]//p[contains(text(),"{}")]'.format(docType)
        Element(id_ = self._gridActive).click();self.sleep(3)
        if Element(xpath = _Docl_withNewLabel).is_exist():
            Element(id_ = self._listActive).click();self.sleep(2)
            return True
        else:
            return False

    '判断当前的文件是否带有No access 的标签 以此来表示其是否具有未授权的版本'
    def check_NoAccess_Label(self,docType,click=True):
        """

        :param docType:
        :param click: 默认去 请求这个no access 的文档
        :return: 是否有此标签
        """


        _Docl_with_NoAccess_Label = '//div[@class="noAccessBox"]/../../../div[2]//p[contains(text(),"{}")]'.format(docType)

        _no_access = '//p[contains(text(),"{}")]/../../../div'.format(docType)
        Element(id_= self._gridActive,describe='点击切换成网格状').click();self.sleep(3)
        if Element(xpath = _Docl_with_NoAccess_Label,describe='判断此文档是否有No access 的样式').is_exist():
            if click:

                Element(xpath = _no_access,describe='点击No access 的标签').click();self.sleep(2)
            else: pass

            return True
        else:
            return False

    '''Invidual '''
    def Delete_Doc(self,Doc):


        DocDelete = '//div[contains(text(),"{}")]/../../td[4]//a[2]'.format(Doc)
        Element(xpath = DocDelete).click()
        Element(xpath = '//span[contains(text(),"Y")]').click()
        _errorM = '//div[contains(@class,"el-message el-message--error")]'
        if Element(xpath = _errorM).is_exist():

            Return_text= Element(xpath = _errorM).text
            #Return_text = self.alert_is_display();self.sleep(3)
            if 'The document has been shared with onboarding' in Return_text:
                logging.info(f'{Doc} has been shared with onboarding')
                return False,Return_text
        else:
            if self.check_repDocDetails(Doc)==False:
                logging.info(f'{Doc} has been delete')
                return True
















