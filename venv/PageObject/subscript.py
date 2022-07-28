from poium import Page,Element
import time

class subscript(Page):
    def logout_bus_portal(self):
        click_icon=Element(xpath="//div[@class='el-dropdown']",timeout=1,describe="点击头像").click()
        logout_button=Element(xpath="//ul/li[contains(text(),' Logout')]",timeout=3,describe="logout web").click()
    def login_bus_portal(self,email,pwd):
        email_input = Element(xpath='//input[@placeholder="Your email"]', index=0, timeout=1, describe="登录页面邮箱输入框").send_keys(email)
        password_input = Element(xpath='//input[@placeholder="Your password"]', index=0, timeout=2,
                                 describe="登录页面密码输入框").send_keys(pwd)
        login_button = Element(xpath='//span[contains(text(),"Login")]', timeout=2, describe="登录按钮").click()
    def User_Profile(self,edit,fnmae=None,mname=None,sname=None,job=None):
        check_infor=[]
        #user profile 基础页面
        print("-------------------")
        time.sleep(3)

        frst_name = Element(xpath="//input[@type='text']", index=3, timeout=3,describe="first_name 输入框")
        middle_name = Element(xpath="//input[@type='text']", index=4,timeout=3, describe="mname_name 输入框")
        surname_name = Element(xpath="//input[@type='text']", index=5,timeout=3, describe="suname_name 输入框")
        role = Element(xpath="//label[contains(text(),'Role')]/following-sibling::div[1]",index=0,timeout=3,describe="用户角色")
        pro_email = Element(xpath="//label[contains(text(),'Role')]/../following-sibling::div[1]/div",index=0,timeout=3,describe="用户email")

        job_title = Element(xpath="//label[contains(text(),'Job Title')]/following-sibling::div//input",  timeout=3,describe="job 输入框")
        save_btu= Element(xpath="//span[contains(text(),'Save')]",timeout=3,describe="保存按钮")
        edit_but= Element(xpath="//span[contains(text(),'Edit')]",timeout=3,describe="编辑按钮")
        if edit==1:#默认为1
            save_btu.click()
            frst_name.send_keys(fnmae)
            surname_name.send_keys(sname)
            job_title.send_keys(job)

            save_btu.click()
            time.sleep(3)
            check_infor.append(pro_email.get_attribute('textContent'))
            check_infor.append(role.get_attribute('textContent'))

            #return pro_email.get_attribute('textContent')+role.get_attribute('textContent')
            print(check_infor)
            return check_infor

        elif edit==2 :#需要编辑
            click_icon = Element(xpath="//div[@class='el-dropdown']", timeout=1, describe="点击头像")
            user_profile_but = Element(xpath="//ul/li[contains(text(),'User Profile')]", timeout=3,
                                       describe="logout web").click()
            edit_but.click()
            time.sleep(3)
            save_btu.click()
            pass

