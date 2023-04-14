from poium import Page, Element,Elements
import time
from poium.common import logging

class AuthRep(Page):


    def open_AuthorisedRepresent(self):
        _connectionPage = '//div[contains(text(),"Connections")]'
        _Coprep = 'sidebar-menu-item1'
        Element(xpath = _connectionPage).click()
        Element(id_=_Coprep).click();time.sleep(3)

    '''Connections_Authorised Representatives'''
    def CheckAuthInformation(self):
        """

        :return: 返回列表中 d[repemail],doc
        """
        self.open_AuthorisedRepresent()
        _repNameCLASS = 'avatar-text' # repEmail的一列
        _repEmailX = '//tr/td[2]/div/span'  # repEmail的一列
        _docWithAccessid = 'component-toolTip-visibilityChange'
        repsEmailEle = Elements(xpath = _repEmailX).find(self)
        len(repsEmailEle)
        DocWithAccessEle = Elements(id_=_docWithAccessid).find(self)
        d=dict()

        for index in range(0,len(repsEmailEle)):
            getRepEmail=repsEmailEle[index].text
            getRepAccessEle=DocWithAccessEle[index].text


            d[getRepEmail]=getRepAccessEle

        return d


    '''Delete online rep'''
    def Remove_onlineRep(self,RepEmail):
        DeleteButton = '//span[contains(text(),"{}")]/../../../td[4]/div/span'.format(RepEmail)

        repExist ='//span[contains(text(),"{}")]'.format(RepEmail)
        Element(xpath = DeleteButton).click()
        if Element(xpath = '//span[contains(text(),"Are You Sure?")]').is_exist():

            Element(xpath = '//span[contains(text(),"Confirm")]').click();self.sleep(3)
            if Element(xpath =repExist).is_exist()==False:
                return True
            else:
                logging.error(f'{RepEmail} delete failed')
                return False
        else:
            logging.error('No Are You Sure? Prompt')

    '''Invite online rep'''
    def InviteRep(self,repemail):
        invite = '//*[@id="connections"]/div[2]/div[1]/img'
        Element(xpath = invite).click()
        Element(id_ ='invite-dialog-email-field').send_keys(repemail)
        Element(id_ = 'invite-dialog-confirm-button').click()








