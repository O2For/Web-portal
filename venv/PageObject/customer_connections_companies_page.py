from poium import Page, Element,Elements
import time


class Companies(Page):

    def ReturnSharedDocuments(self):
        shareDocument=Element(xpath='//*[@id="component-toolTip-visibilityChange"]/text()')
        print(type(shareDocument))


        return shareDocument