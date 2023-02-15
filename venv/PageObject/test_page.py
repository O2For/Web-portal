from poium import Element,Page,Elements
import time
from selenium import webdriver

class StCv(Page):
    '''一些测试脚本'''


    news = Element(xpath="//a[contains(text(),'新闻')]", describe="1---")
    ins=Element(id_="ww")

class Ht(Page):
    un=Element(id_="username")
    pd=Element(id_="password")
    go=Element(xpath="//button")
    tt=Element(xpath="//a[contains(text(),'Task Tracking')]")
    dr=Element(xpath="//li/a[contains(text(),'Daily Report')]",index=0)
    des=Element(id_="ctl00_ContentPlaceHolder1_tbDescription")
    commit=Element(id_="ctl00_ContentPlaceHolder1_btnCommit")



