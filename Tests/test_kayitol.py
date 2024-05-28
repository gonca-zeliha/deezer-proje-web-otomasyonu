from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.kayitol import *
import allure
import softest
import unittest
import pytest
from constest import *

@pytest.mark.usefixtures("setup")
@ddt
class TestRegister(softest.TestCase, unittest.TestCase):
    


    def test_basarili_giris_yap(self):
       
      
        kayitol = KayitOl(self.driver)
        kayitol.cerezleri_kabul_et()
        kayitol.anasayfada_kabul_et_butonuna_tikla()
        kayitol.kayit_icin_gecerli_mail_adresi_gir()
        kayitol.kayit_icin_kullanici_adi_gir()
        kayitol.kayit_icin_sifre_gir()
        kayitol.kayit_icin_yasini_gir()
        kayitol.cinsiyetini_tikla()
        kayitol.cinsiyetini_kadin_sec()
        kayitol.veri_iznine_tikla()
        kayitol.son_kayit_ol_butonuna_tikla()
    
      
        