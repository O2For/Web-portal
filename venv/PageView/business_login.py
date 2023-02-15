from poium import Page, Element

class LoginPage(Page):
    '''business portal 的login page基础定位'''
    login_username = Element(id_='login-username-input')
    login_password = Element(id_='login-password-input')
    login_button = Element(id_='login-handleLogin-btn')

