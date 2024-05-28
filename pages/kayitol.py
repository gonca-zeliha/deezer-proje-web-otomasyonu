import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from pages.PageBase import PageBase
from constans.globalconstans import *


@pytest.mark.usefixtures("setup")
class KayitOl(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def cerezleri_kabul_et(self):
        cookies = self.wait_element_visibility(COOKIE_ACCEPT_LOCATE)
        cookies.click()

   #geçerli kayıt olma işlemi

    def anasayfada_kabul_et_butonuna_tikla(self): 
        self.wait_element_visibility(ANASAYFA_KAYITOL_BUTTON).click()
       

    def kayit_icin_gecerli_mail_adresi_gir(self):
        self.wait_element_visibility(EPOSTA).send_keys(kullanici_eposta)
       
        sleep(1)

    def kayit_icin_kullanici_adi_gir(self):
        self.wait_element_visibility(KULLANICIAD).send_keys(NAME)
       
    
    def kayit_icin_sifre_gir(self):
        self.wait_element_visibility(SIFRE).send_keys(valid_password)
      
        sleep(1)
    
    def kayit_icin_yasini_gir(self):
        self.wait_element_visibility(YAS).send_keys(DAY)
    
    def cinsiyetini_tikla(self):
        self.wait_element_visibility(CINSIYETBUTTON).click()
        
    def cinsiyetini_kadin_sec(self):
        self.wait_element_visibility(CINSIYETKADINSEC).click()
    
    def veri_iznine_tikla(self):
        self.wait_element_visibility(VERI_IZNI_BUTTON).click()
    
    def son_kayit_ol_butonuna_tikla(self):
        self.wait_element_visibility(KAYITOL).click()
        sleep(5)

