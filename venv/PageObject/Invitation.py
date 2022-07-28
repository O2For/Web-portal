from poium import Page,Element
from selenium import webdriver

class invitation_page(Page):
    system_mune= Element(xpath="//div[contains(text(),'System')]", index=0, timeout=2, describe="invtaion_menu")

    invitation_mune=Element(xpath="//li[contains(text(), 'Invitation')]",index=0,timeout=2,describe="invtaion_menu")
    create_button=Element(xpath="//span[contains(text(),'Create')]", index=0, timeout=2, describe="点击新增用户按钮")

    free_email =  Element(xpath="//textarea[@class='el-textarea__inner']",index=2,timeout=1,describe="input invite email")
    select_role = Element(xpath="//span[contains(text(),'Freemium')]/preceding-sibling::span[1]",timeout=1,describe="进行角色选择")
    create_bus= Element(xpath="//span[contains(text(),'Create')]", index=2, timeout=2, describe="确认新增此用户create_bus")
    # snapmail,cc
    add_email_button = Element(xpath="//span[@class='subline clearfix']", index=0, timeout=2, describe="add——test——email")
    input_email = Element(id_="inputEmail",timeout=2, describe="输入被邀请的d公司邮箱")
    confirm_emil_btn = Element(xpath="//button[@ng-click='addEmailBox()']",timeout=2, describe="save")

    join_v8_link = Element(xpath="(//tbody//img[@title='valid8Me'])[2]",index=0,timeout=3,describe="点击邀请链接")
    #email_iframe=Element(xpath='//iframe[@name="preview-iframe"]')
    #email_iframe=find_element_by_xpath('//iframe[@name="preview-iframe"]')
    # registion_bus_page Create your account
    you_email = Element(xpath="//input[@placeholder='Your email']",timeout=2)
    your_password = Element(xpath="//input[@placeholder='Your password']", timeout=2, describe="")
    confirm_password = Element(xpath="//input[@placeholder='Confirm password']", timeout=2, describe="")
    next_button= Element(xpath="//span[contains(text(),'next')]", timeout=2, describe="",index=0)
    code_inp = Element(xpath="//input[@placeholder='Your code']",index=1, timeout=2, describe="输入邮箱验证码")
    # snapmail,cc
    invite_title = Element(xpath="//span[contains(text(),'invite you to register valid8Me account')]", index=0,timeout=2, describe="读取邀请邮箱")
    back_button= Element(xpath="//a[@class='ng-binding']",index=13,timeout=1,describe="back_button")
    r_fst_email= Element(xpath="//li[@ng-if='emailCount']/following-sibling::li[1]",index=0,timeout=1,describe="定位最新的邮件信息")
    text_email = Element(xpath="//table/tbody/tr/td[1]/p",timeout=2,index=1, describe="")
    #step 2


    next_ = Element(xpath="//span[contains(text(),'next')]", timeout=2,index=1, describe="生成账号的最后一步邮箱验证")
    #step 3
    accept_but=Element(xpath="//button[@type='button']",index=3,describe="接受条约许可")



