from poium import Page, Element

class inbound_notifications(Page):
    #left_table
    notifications_table=Element(xpath="//div[contains(text(),'Notifications')]",timeout=1,describe="left_table")
    Forms_table = Element(xpath="//div[contains(text(), 'Forms')]", timeout=1, describe="left_table")
    Reminders_table = Element(xpath="//div[contains(text(), 'Reminders')]", timeout=1, describe="left_table")
    Events_table = Element(xpath="//div[contains(text(), 'Events')]", timeout=1, describe="left_table")
    invit_email = Element(xpath='//textarea[@placeholder="Ensure there is only one email address per line if inviting multiple at one time"]')
    system_role = Element(xpath="//span[contains(text(),'Freemium')]")
