import os
import sys
from time import sleep
import pytest
import allure
from pytest_assume.plugin import assume

#POB

sys.path.append(os.getcwd())
from PageView.Customer_portal.customer_login import *
from PageView.Customer_portal.customer_system_page import *
from PageView.Business_portal.business_login import LoginPage
from PageView.Business_portal.MyWorkPage import *
from PageView.Business_portal.VaultHubPage import *

from PageView.Customer_portal.customer_connections_companies_page import *
from PageView.Customer_portal.customer_connections_corpRep_page import *
from PageView.Customer_portal.Documents.customer_corporateDoc_page import *
from PageView.Customer_portal.customer_connections_AuthorisedRep import *
from PageView.Customer_portal.customer_document_page import *
from PageView.Customer_portal.customer_action_page import *
from PageView.Business_portal.Configuration.Product_services import *
from Common.config import *
#

# 数据准备导入路径
from Data.test_data import GetData

''' 当前路径(使用 abspath 方法可通过dos窗口执行)'''
current_path = os.path.dirname(os.path.abspath(__file__))
print("当前路径"+current_path)


'''得到本次测试配置数据：'''
sys.path.append(os.getcwd())
data=GetData.TestData()


'''得到本次导入到测试中的excel数据：'''
FileExecl=FileOperation()
Test_data=FileExecl.getExecl()


@allure.epic('Somke Testing Valid8Me v2.11.0')
class TestCaes:
    def test_St110(self, drivers, CorpEmail, CorpName,
                   Rep1Email, Rep1Name,
                   Rep2Email, Rep2Name,DocumentType1, Rep2Doc2,
                   Rep3Email, Rep3Name, DocumentType2,
                   Password,
                   business_name, NewProductName,business_email, business_password):
        RootPath = PathOperation()
        with allure.step('Precondition 0: Doc Type Path Ready....'):
            DocPath = RootPath.getOtherPath('\Data')
            dataTest = dict(data.Photo_C)  # 加载 文档内容
        bus = LoginPage(drivers)
        CusHomePage=CustomerHomePage(drivers)

        bus.open(Test_data['business_url']);

        vaulhub=VaultHub(drivers)
        drawer=Drawer(drivers)
        nav=NavigationBar(drivers)

        with allure.step('The obc user can see the reps document'):
            with allure.step('Login business portal...'):

                bus.BusLogin(business_email, business_password)
            with allure.step('Check the Notifications can find {} link case'.format(CorpEmail)):

                vaulhub.();
                vaulhub.searchCustomer(Email=CorpEmail)
                vaulhub.ClickSearchList(CorpEmail)
                drawer.checkConnectionCases()
                drawer.ClickCase(NewProductName)
                username = nav.showConnection(CorpEmail)
            with allure.step('OBC  can check shared doc img'):
                nav.LinkedConnections(username['linkname'],DocumentType1)
                nav.closeConnectioncase()
                nav.switch_to_window(0)





