import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from pages.PageBase import PageBase
from constans.globalconstans import *

@pytest.mark.usefixtures("setup")
class AnaGiris(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
   
    def ana_giris(self):
        self.wait_element_visibility(ANASAYFA_GIRISYAP_BUTONU).click()
        self.wait_element_visibility(GIRIS_MAIL).send_keys(LOGIN_MAIL)
        self.wait_element_visibility(GIRIS_SIFRE).send_keys(PASSWORD)
        self.wait_element_clickable(GIRIS_SAYFASI_GIRIS_YAP).click()

@pytest.mark.usefixtures("setup")
class Giris(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def anasayfada_giris_yap_butonuna_tikla(self):
        self.wait_element_visibility(ANASAYFA_GIRISYAP_BUTONU).click()
        
    
    def giris_yapmak_icin_mail_adresi_gir(self):
        self.wait_element_visibility(GIRIS_MAIL).send_keys(LOGIN_MAIL)
        self.wait_element_visibility(GIRIS_SIFRE).send_keys(PASSWORD)
    
    def giris_yap_butonuna_tikla(self):
        self.wait_element_visibility(GIRIS_SAYFASI_GIRIS_YAP).click()
    
    def giris_basarili(self):
        msg_box = self.wait_element_visibility(FLOW)
        return msg_box.text
        sleep(2)


@pytest.mark.usefixtures("setup")
class GirisBos(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    
    def anasayfada_giris_yap_butonuna_tikla(self):
        self.wait_element_visibility(ANASAYFA_GIRISYAP_BUTONU).click()

    def giris_yap_butonuna_tikla(self):
        self.wait_element_visibility(GIRIS_SAYFASI_GIRIS_YAP).click()
    
    def bos_birakilan_alanlar_hata_mesaji(self):
        msg_box = self.wait_element_visibility(BOS_UYARIMESAJI)
        return msg_box.text
    
        time.sleep(2)
    
