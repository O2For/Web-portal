from poium import Page, Element

class customer_login_page(Page):

    '这里是 Customer protal 的 login 页面 基础定位'

    email = Element(xpath="//input[@placeholder='Enter your email']",describe="输入邮箱")
    password = Element(xpath="//input[@placeholder='Enter password']",describe="password")
    login =Element(xpath="//span[contains(text(),'Login')]",describe="login button")
    sign_up = Element(xpath="//span[contains(text(),'Sign Up')]",describe="sign up button")
    forgot_password =Element(xpath="//a[contains(text(),'Forgot')]")

    inp_password = Element(xpath="//input[@placeholder='Please enter your password']", describe="password")

    confirm_paw = Element(xpath="//input[@placeholder='Please enter your password again']",describe="重新输入密码")
    accept_read = Element(xpath="//a[contains(text(),'END USER-TERMS & CONDITIONS')]/preceding-sibling::label/*[1]")


    code_input =  Element(xpath="//input[@placeholder='Please enter the code you received']",describe="验证码")
    confirm_btu = Element(xpath="//BUTTON/span[contains(text(),'Confirm')]", timeout=3,describe="code confirm button")
    role_ind = Element(xpath="//span[contains( text(),'Individual')]",describe="ind")
    role_corp = Element(xpath="//span[contains( text(),'Corporate')]",describe="corp")

    fst_n = Element(xpath="//input[@placeholder='Enter first name']",describe='first name')
    lst_n =  Element(xpath="//input[@placeholder='Enter last name']",describe='lst st name')








