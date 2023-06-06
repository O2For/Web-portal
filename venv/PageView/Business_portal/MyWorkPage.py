from selenium.webdriver.common.keys import Keys
from PageView.Mail.snapmail_page import *
from poium.common import logging
from poium import Elements,Page,Element


class NavigationBar(Page):
    '''这里是business portal 中My work page的基础定位以及方法'''
    #left_table
    # notifications_table=Element(xpath="//div[contains(text(),'Notifications')]",timeout=1,describe="left_table")
    # Forms_table = Element(xpath="//div[contains(text(), 'Forms')]", timeout=1, describe="left_table")
    # Reminders_table = Element(xpath="//div[contains(text(), 'Reminders')]", timeout=1, describe="left_table")
    # Events_table = Element(xpath="//div[contains(text(), 'Events')]", timeout=1, describe="left_table")
    # invit_email = Element(xpath='//textarea[@placeholder="Ensure there is only one email address per line if inviting multiple at one time"]')
    # system_role = Element(xpath="//span[contains(text(),'Freemium')]")
    def OpenMyWork(self):
        self.wait(5)
        Element(xpath="//span[contains(text(),'My Work')]").click()
        self.sleep(3)


        '邀请未在此客户中的人'
    def SourceDocuments(self,invite_email,product,**kwargs):
        '''send request 发送一个新的邀请'''
        self.wait_page_load_timeout(10)

        Element(id_='layout-navbar-source-documents-button',describe='点击Soure document').click()

        Element(id_='component-tag-input').send_keys(invite_email)
        #Element(id_='source-documents-product-service-select',timeout=5).send_keys(Keys.ENTER)
        #2023 最新版更新路径
        Element(id_='source-documents-product-service-select').click();time.sleep(3)
        ProductXpath="//div/div//p[contains(text(),'{}')]".format(product)
        Element(xpath=ProductXpath).click()
        if kwargs:
            Element(id_='layout-connect-note-input',describe='note').send_keys(kwargs['Note'])
        Element(id_='customer.Confirm.btn.save',describe='Send Request').click();time.sleep(3)
        Element(id_='customer.close.grey.btn',describe="close SourceDocuments").click()
        logging.info(f'SourceDocuments success invite: {invite_email}the product is: {product}')
        self.sleep(2)


        return print('send request success')
        '查看列表中的 通知 并且返回'
    def CheckNotifications(self):
        Status = Element(xpath='//td/div',index=1).text
        ConnectionName = Element(xpath='//td/div', index=2).text
        CaseRef = Element(xpath='//td/div', index=3).text
        EmailAddress = Element(xpath='//td/div', index=4).text
        Type = Element(xpath='//td/div', index=5).text
        d=dict()
        d['Status']=Status
        d['ConnectionName']=ConnectionName
        d['CaseRef']=CaseRef
        d['EmailAddress']=EmailAddress
        d['Type']=Type
        logging.info(f'Get the first Notifications{d}')

        return d
    def ClickNotificationsDetail(self,Email):
        operationIcon = '//div[contains(text(),"{}")]/../../td[8]//span/..'.format(Email)
        Element(xpath  = operationIcon,index=0,describe='默认只打开第一个').double_click()

    '点击viewcase 并且返回其中的linkname'
    def showConnection(self,Email):
        self.ClickNotificationsDetail(Email)

        viewcaseid = 'dashboard.myForms.table.showConnection'
        LinkedConnectionTitle = '//*[contains(text(),"Linked Connections")]'
        elelist=Elements(id_ = viewcaseid).find(self)
        '根据页面只有检索的最后一个为view case的按钮'
        elelist[-1].click();self.sleep(3)
        Element(xpath = LinkedConnectionTitle,describe='展开link').click()
        d=dict()
        linkname=Element(id_ = 'dashboard.caseModal.picName.goProfile').text
        d['linkname'] = linkname
        return d

        '查看被分享的文件内容'
    def LinkedConnections(self,linkUsername,*args):
        linknameid='dashboard.caseModal.picName.goProfile'

        ViewDocid = 'dashboard.caseModal.docList.goViewDoc'
        imgDOCid = 'dashboard.view.img2.contextmenu'
        closeDocdisplay = '/html/body/div[5]/div/div[1]/button'
        if Element(id_ =ViewDocid).text ==linkUsername:
            for i in range(0,len(args)):
                docname = '//div[contains(text(),"{}")]'.format(args[i])
                if Element(xpath = docname).is_exist():
                    Element(id_ = ViewDocid,index=i,describe='查看分享的文件内容').click();self.sleep(3)
                    if Element(id_ = imgDOCid).is_exist():
                        logging.info(f'Doc {args[i]} display right')
                        Element(xpath = closeDocdisplay).click()
                        self.sleep(3)
                        pass
                    else:
                        logging.warning(f'Doc {args[i]} display error')
                else:
                    logging.warning(f'No Find doc {args[i]} in link connections details')
        else:
            logging.error(f'Link user error')

        '关闭connection 的 弹窗'
    def closeConnectioncase(self):
        xbutton ='/html/body/div[3]/div/div[1]/button/i'
        Element(xpath = xbutton).click();self.sleep(3)














