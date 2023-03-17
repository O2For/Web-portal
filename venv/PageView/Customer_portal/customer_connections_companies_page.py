from poium import Page, Element,Elements
import time
from poium.common import logging

class Companies(Page):

    def ReturnSharedDocuments(self):
        shareDocument=Element(xpath='//*[@id="component-toolTip-visibilityChange"]').text

        logging.info(f"OP ✅ ReturnSharedDocuments :{shareDocument}")

        return shareDocument