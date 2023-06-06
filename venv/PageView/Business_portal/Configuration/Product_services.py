from poium import Page, Element,Elements
import time

from poium.common import logging
class Product(Page):
    'product 的 相关 方法：创建product，编辑product'
    # Basic Information
    _create_button_id = 'system-product-edit-button-create'
    _name_id = 'addProduct-modal-dataForm-name-input-create'
    _segment_id = 'addProduct-modal-dataForm-type-select-create'
    _segment_corp_xpath = '//li/span[contains(text(),"Corporate")]'
    _segment_individual_xpath = '//li/span[contains(text(),"Individual")]'
    _status_id = 'addProduct-modal-dataForm-status-select'
    _status_enabled_xpath = '//li/span[contains(text(),"Enabled")]'

    _Searchable_xpath = "//span/span[contains(text(),'No')]"

    _Legal_Term_id = 'addProduct-modal-dataForm-validity-select'
    _Legal_Term_select_id = 'addProduct-modal-dataForm-validity-select-option0'

    _Jurisdiction_id = 'addProduct-modal-dataForm-jurisdiction-select'
    _Jurisdiction_country_id = 'addProduct-modal-dataForm-jurisdiction-select-option0'

    #note
    _note = 'addProduct-modal-dataForm-note-input'
    #Standard Due Diligence Documents
    _companu_information_id='addProduct-modal-dataForm-handleCheckAllChange-checkbox0'

    _next_button = 'addProduct-modal-next-btn'

    _docoument1 =  'addProduct-modal-docTypeList-radio0'
    _docoument2 =  'addProduct-modal-docTypeList-radio2'

    _create_product_button_id = 'addProduct-modal-handleCreate-btn'

    def OpenProuductPage(self):
        '打开页面'
        Element(xpath="//span[contains(text(),'Configuration')]").click()
        Element(id_='productsServices').click()
        time.sleep(3)


    def CreateOnlyCorp(self,Product_name,**kwargs):
        '创建一个只有corp文件的产品,这里暂时支持只有固定选择的'
        Element(id_=self._create_button_id).click()

        Element(id_=self._name_id).send_keys(Product_name)

        Element(id_=self._segment_id).click()
        Element(xpath=self._segment_corp_xpath).click()

        Element(id_=self._status_id).click()
        Element(xpath=self._status_enabled_xpath).click()

        Element(id_=self._Legal_Term_id).click()
        Element(id_=self._Legal_Term_select_id).click()

        Element(id_=self._Jurisdiction_id).click()
        Element(id_=self._Jurisdiction_country_id).click()

        Element(xpath=self._Searchable_xpath).click()

        # note
        if kwargs:
            Element(id_=self._note).send_keys(kwargs['Note'])

        Element(id_=self._next_button).click()

        Element(id_='addProduct-modal-dataForm-handleCheckAllChange-checkbox0').click()
        Element(id_=self._docoument1).click()
        Element(id_=self._docoument2).click()

        Element(id_=self._create_product_button_id).click()
        self.sleep(3)

        logging.info(f"OP ✅ CreateOnlyCorp :{Product_name} create success")
        return

    def CreateOnlyIndividual(self,Product_name,**kwargs):
#Name:
        Element(id_=self._create_button_id).click()
        Element(id_=self._name_id).send_keys(Product_name)
#Segment:
        Element(id_=self._segment_id).click()
        Element(xpath=self._segment_individual_xpath).click()
#Status:
        Element(id_=self._status_id).click()
        Element(xpath=self._status_enabled_xpath).click()
#Legal Term:
        Element(id_=self._Legal_Term_id).click()
        Element(id_=self._Legal_Term_select_id).click()
#Jurisdiction:
        Element(id_=self._Jurisdiction_id).click()
        Element(id_=self._Jurisdiction_country_id).click()
#Searchable on valid8Me
        Element(xpath=self._Searchable_xpath).click()
#note
        if kwargs:
            Element(id_=self._note).send_keys(kwargs['Note'])
#next
        Element(id_=self._next_button).click()
#Standard Due Diligence Documents
        Element(id_='addProduct-modal-dataForm-handleCheckAllChange-checkbox0').click()
        Element(id_='addProduct-modal-docTypeList-radio0').click() #passport
        Element(id_='addProduct-modal-docTypeList-radio2').click() #nation id card

        Element(id_=self._create_product_button_id).click()
        self.sleep(3)

        logging.info(f"OP ✅ CreateOnlyIndividual :{Product_name} create success")
        return

    def CreateWithReps(self,Num_Rep):

        return
    '''Create Product Step'''

    def Create_Basic_Inforamtion(self,Product_name,Segment,**kwargs):

        Element(id_=self._create_button_id).click()
        Element(id_=self._name_id).send_keys(Product_name)
        # Status:
        Element(id_=self._status_id).click()
        Element(xpath=self._status_enabled_xpath).click()
        # Legal Term:
        Element(id_=self._Legal_Term_id).click()
        Element(id_=self._Legal_Term_select_id).click()
        # Jurisdiction:
        Element(id_=self._Jurisdiction_id).click()
        Element(id_=self._Jurisdiction_country_id).click()
        # Searchable on valid8Me
        Element(xpath=self._Searchable_xpath).click()
        # Note
        if kwargs:
            Element(id_=self._note).send_keys(kwargs['Note'])

        Element(id_=self._segment_id).click()
        if Segment=='Corporate':

            Element(xpath=self._segment_corp_xpath).click()

        elif Segment=='Individual':

            # Segment:
            Element(xpath=self._segment_individual_xpath).click()

        Element(id_=self._next_button).click()


    def Create_Standard_Due_Diligence_Documents(self,*args):

        Company_Information=['Board Resolution Document','Memorandum of Association']

        Authorised_Representatives=['Authorised Signatory List (Headed Paper)','Official List of Company Directors']
        Ownership_Information = ['Beneficial Ownership/Control','Details of shareholding/ownership structure']

        _header = 'header-text'
        _left_caret_icon='left-caret-icon'
        reps = 'el-radio-button__inner'


        for i in range(0,len(args)):
            if args[i] in Company_Information:
                Element(class_name = _header,index=0).click()
            elif args[i] in Authorised_Representatives:
                Element(class_name=_header, index=1).click()
            elif args[i] in Ownership_Information:
                Element(class_name=_header, index=2).click()
                Element(class_name=_left_caret_icon, index=2).click();
                self.sleep(3)
            docNameCheck = '//p[contains(text(),"{}")]'.format(args[i])
            Element(xpath = docNameCheck).click();self.sleep(1)
        Element(class_name = reps,index=2).click()
        return


    def Create_Authorised_Representatives(self,RepNumber=0,*args):
        """

        :param RepNumber:
        :param args: rep 需要创建的文本元祖
        :return:
        """
        _CreateID = 'addProduct-modal-handleCreate-btn'
        _InputRep = '//div[@class="el-input"]/input'
        _header = 'header-text'
        _left_caret_icon = 'left-caret-icon'


        PhotoID = ['Passport','Driving Licence','National ID Card','Other Proof of Identity Documentation','Certified Document']
        Proof_of_Address = ['Utility Bill']

        if RepNumber==0:

            Element(id_=_CreateID).click();self.sleep(3)
            return
        else:
            Element(xpath = _InputRep).send_keys(RepNumber,clear=True)
            PhotoIDshow=0
            Proof_of_Address_show=0
            for i in range(0, len(args)):

                if args[i] in PhotoID:
                    if PhotoIDshow == 0:

                        Element(class_name=_header, index=0).click()
                        PhotoIDshow = 1
                    else: pass

                elif args[i] in Proof_of_Address:
                    if Proof_of_Address_show==0:

                        Element(class_name=_header, index=1).click()
                        Proof_of_Address_show=1
                    else:pass

                docNameCheck = '//p[contains(text(),"{}")]'.format(args[i])
                Element(xpath=docNameCheck,describe='勾选所选文件').click();
                self.sleep(1)

                Element(id_=_CreateID).click();
                self.sleep(3)
                logging.info(f'product create successfully')
                return



    def getIndividualDOC(self):

        DOC=Elements(id_='NormalTextTooltipol-visibilityChange').find(self)
        docc=[]
        for d in DOC:
            docc.append(d.text)
        logging.info(f'list {docc}')
        print(docc)















