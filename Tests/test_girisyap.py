from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.giris import *
from pages.kayitol import *
import allure
import softest
import unittest
import pytest
from constest import *

@pytest.mark.usefixtures("setup")
@ddt
class TestGirisYap(softest.TestCase, unittest.TestCase):
    


    def test_giris_yap(self):
        girisyap = Giris(self.driver)
        kayitol = KayitOl(self.driver)
        kayitol.cerezleri_kabul_et()
        girisyap.anasayfada_giris_yap_butonuna_tikla()
        girisyap.giris_yapmak_icin_mail_adresi_gir()
        girisyap.giris_yap_butonuna_tikla()
        girisyap.giris_basarili()

        #manuel robotu geç
   
    
    def test_giris_islemleri_bos(self):
        girisyap = GirisBos(self.driver)
        kayitol = KayitOl(self.driver)
        kayitol.cerezleri_kabul_et()
        girisyap.anasayfada_giris_yap_butonuna_tikla()
        girisyap.giris_yap_butonuna_tikla()
        girisyap.bos_birakilan_alanlar_hata_mesaji()
    
     

      
        