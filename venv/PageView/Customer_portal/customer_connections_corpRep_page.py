from poium import Page, Element,Elements
import time
from poium.common import logging

class CorpRep(Page):


    _PermissionSetting = 'corporatesIRepresent-settingOne-shareundefined'
    PermissionSetting=Element(id_ = _PermissionSetting)


    warning  = Element(xpath = "//div[@class='el-message-box__message']/p")

    okay = Element(xpath = '//span[contains(text(),"Okay")]')

    '''Connections/Corporates I represent page'''
    def open_CorporatesRepresent(self):
        _connectionPage = '//div[contains(text(),"Connections")]'
        _Coprep = 'sidebar-menu-item1'
        Element(xpath = _connectionPage).click()
        Element(id_=_Coprep).click();time.sleep(3)
    '''检查 页面列表数据'''
    def CheckCorpInformation(self):
        self.open_CorporatesRepresent()
        _cororateNameCLASS = 'avatar-text'
        _docWithAccessid = 'component-toolTip-visibilityChange'
        getcorpName = Element(class_name = _cororateNameCLASS).text
        getDocWithAccess = Element(id_=_docWithAccessid).text
        d = dict()
        d['getcorpName'] = getcorpName
        d['getDocWithAccess'] = getDocWithAccess
        return d

    def reovkeDoc(self,doc):
        _confirm = 'el-button el-button--default el-button--small el-button--primary'
        _CLOSE = 'el-dialog__headerbtn'


        docRevokeButton = '//p[contains(text(),"{}")]/../../../span[2]/span'.format(doc)
        Element(xpath = docRevokeButton).click();self.sleep(3)
        if Element(xpath = '//span[contains(text(),"Document has been shared ")]').is_exist() ==True:
            Element(id_ = _confirm,describe='Confirm').click()

            logging.info(f'This document has been shared by corporate company and therefore you cannot revoke access. If you wish to remove access, please initiate a revoke request.')
            Element(class_name = _CLOSE).click();self.sleep(3)
            return False
        elif Element(xpath = "//p[contains(text(),'Are you sure')]").is_exist():
            Element(id_=_confirm, describe='Confirm').click();self.sleep(3)
            if Element(xpath = docRevokeButton).is_exist()==False:
                Element(class_name=_CLOSE).click();
                self.sleep(3)
                logging.info(f'{doc} revoke successfull ')
                return True
            else:
                logging.error(f'{doc} revoke failed ')













