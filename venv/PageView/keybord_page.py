from poium import Element,Page

#//*[@id="dq"]/app-keystroke-auth-box/div/div/div[1]/text()[2]
class LOGIN(Page):
    un=Element(xpath="//input",index=0)
    pw=Element(xpath="//input",index=1)
    sign=Element(xpath="//button",index=2)

    #
    uscen=Element(xpath="//a",index=5)
    keyst = Element(xpath="//a", index=6)
    #page3
    samply0=Element(class_name='text')
    us_input=Element(xpath="//textarea",index=0)
    samply1=Element(class_name='text',index=1)
    pw_input=Element(xpath="//textarea",index=1)

    num=Element(xpath='//button',index=2)