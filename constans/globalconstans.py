from selenium.webdriver.common.by import By
import random

##ANASAYFA

BASE_URL = "https://www.deezer.com/tr/"
ANASAYFA_KAYITOL_BUTTON = (By.ID,"topbar-register-button")
ANASAYFA_GIRISYAP_BUTONU = (By.ID,"topbar-login-button")

#kayit ol sayfasi
EPOSTA = (By.ID, "register_form_mail_input")
KULLANICIAD = (By.ID, "register_form_username_input")
SIFRE = (By.ID,"register_form_password_input")
YAS = (By.ID,"register_form_age_input")
CINSIYETBUTTON = (By.ID, "register_form_gender_input")
CINSIYETKADINSEC= (By.XPATH,"//*[@id='register_form_gender_input']/option[2]")

KAYITOL = (By.ID, "register_form_submit")
VERI_IZNI_BUTTON = (By.ID,"register_form_explicit_consent")

SARKICISEC= (By.CLASS_NAME,"onboarding-screen-grid css-0")
SARKICISECXPATH =(By.XPATH,"//*[@id='artist-grid']/div/div/div/div[3]/div/div")

COOKIE_ACCEPT_LOCATE= (By.ID,"gdpr-btn-refuse-all")
#KAYIT BAŞARILI
FLOW = By.XPATH,"//*[@id='page_content']/div/div[3]/section[1]/div[1]/div/div/h2"
FLOW_TEXT = "Flow: ne hissediyorsan onu çal"

SANATCIYLA_DEVAM_ET=(By.XPATH,"//*[@id='chakra-modal--body-:rb:']/div[2]/div[4]/div/button")
PREMIUM_KAPAT= (By.CSS_SELECTOR,"section#chakra-modal-\:r4e\:  .chakra-icon.css-c1x3e4")
PREMIUM_KAPAT_XPATH=(By.XPATH,"//section[@id='chakra-modal-:r4e:']/button[@type='button']")

#bos eposta uyarısı
BOS_UYARIMESAJI = (By.ID, "login_error")
BOS_TEXT = "Bilgilerin hatalı. Lütfen tekrar dene."

#mevcut eposta ile giris ve sonrasında gorunen popup
MEVCUTEPOSTA_TEXT = "Bu e-posta ile zaten bir Deezer hesabı ilişkilendirilmiş"
MEVCUTEPOSTA_POPUP_XPATH =  (By.XPATH, "//*[@id='register_form']/form/div[1]/div")

#verilerin izin verilmemesi
VERI_IZNI_UYARISI= (By.CLASS_NAME,"form-control-error")
VERI_IZNI_UYARISI_TEXT = "Kaydolmak için izni vermen gerekiyor"

#LÜTFEN TÜM ALANLARI KONTROL ET
TUM_ALAN_KONTROL_ET_UYARISI = (By.ID,"register_form_global_error")
TUM_ALAN_KONTROL_ET_UYARISI_TEXT= "Lütfen tüm alanları kontrol et"

##GİRİŞ##


GIRIS_MAIL= (By.ID, "login_mail")
GIRIS_SIFRE = (By.ID, "login_password")
GIRIS_SAYFASI_GIRIS_YAP = (By.ID, "login_form_submit")

ERROR_TEXT_LOCATE = (By.ID, "login_error")
INVALID_LOGIN_ERROR_TEXT = "Bilgilerin hatalı. Lütfen tekrar dene."

##TEST DATA##

LOGIN_MAIL = ("logi_01_02@hotmail.com")
REGISTER_MAIL = ("logi_01_02@hotmail.com")
PASSWORD = ("logi0102")
NAME = ("gonca")
DAY = ("32")
CALMA_LISTESI_ISMI=("GONCA")
CALMA_LISTESI_TANIMI =("rahatlatıcı müzikler")


#valid giris

randonint = str(random.randint(1000, 9999))
kullanici_eposta= ("gonca"+ randonint +"@hotmail.com")
kullanici_ad = "gonca"
valid_password = "g123456789"
yas = "32"

# profil düzenleme

ANA_SAYFA_CALMA_LISTESI_OLUSTUR_BUTONU=(By.XPATH,"//*[@id='dzr-app']/div/div[5]/div[2]/div[2]/a[2]/div[2]/div/div/div/p")

ANA_SAYFA_OLUSTURULAN_CALMA_LISTESINE_TIKLA=(By.XPATH,"//*[@id='dzr-app']/div/div[5]/div[2]/div[2]/a[2]")
CALMA_LISTESI_ISMI_OLUSTUR=(By.XPATH,"//*[@id='chakra-modal--body-:r4k:']/div/div[1]/div[1]/input")
CALMA_LISTESI_OZEL_BUTONU_AKTIF_ET= (By.XPATH,"//*[@id='chakra-modal--body-:r4k:']/div/div[1]/div[3]/label[2]/span")
CALMA_LISTESINE_TANIM_EKLE=(By.XPATH,"//*[@id='chakra-modal--body-:r4k:']/div/div[2]/textarea")
OLUSTUR_TIKLA = (By.XPATH,"//*[@id='chakra-modal--body-:r4k:']/div/div[3]/button")


CALMA_LISTESI_OLUSTUR= (By.XPATH,"//*[@id='page_profile']/div[2]/div/div/div/section[1]/div/div[2]/div/div/ul/li/div[1]/button")
CALMA_LISTESI_OLUSTUR_RESIM_YUKLE= (By.XPATH,"//*[@id='chakra-modal--body-:r5c:']/div/figure/div[2]/span")

CALMA_LISTESI_OLUSTUR_BASARILI_POPUP_MESAJI=(By.XPATH,"//*[@id='dzr-app']/div/aside/div/h2")
CALMA_LISTESI_OLUSTUR_BASARILI_POPUP_MESAJI_TEXT= ("Çalma listesi başarıyla oluşturuldu")
OLUSTURULAN_CALMA_LISTESINE_TIKLA=(By.CLASS_NAME,"picture picture-link overlay-hidden no-background")
CALMA_LISTESINDE_3_NOKTAYA_TIKLA=(By.XPATH,"//*[@id='page_naboo_playlist']/div[1]/div/div[2]/div[1]/div[2]/div/button")
BU_CALMA_LISTESINI_SIL=(By.XPATH,"/html/body/div[7]/div/ul/li/button/span[2]")
CALMA_LISTESINI_SIL_ONAYI=(By.XPATH,"//*[@id='chakra-modal-:r4o:']/footer/div/button[2]")









