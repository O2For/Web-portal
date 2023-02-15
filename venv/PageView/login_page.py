from poium import Page, Element

class Login_page(Page):
    email_input=Element(xpath='//input[@placeholder="Your email"]',index=0,timeout=1,describe="登录页面邮箱输入框")
    password_input=Element(xpath='//input[@placeholder="Your password"]',index=0,timeout=2,describe="登录页面密码输入框")
    login_button=Element(xpath='//span[contains(text(),"Login")]',timeout=2,describe="登录按钮")
