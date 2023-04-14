from poium import Page, Element
import time
class LoginPage(Page):
    '''business portal 的login page基础定位'''
    login_username = Element(id_='login-username-input')
    login_password = Element(id_='login-password-input')
    login_button = Element(id_='login-handleLogin-btn')
    def BusLogin(self,Email,Password):

        self.login_username.send_keys(Email)
        self.login_password.send_keys(Password)
        self.login_button.click();
        self.sleep(5)




