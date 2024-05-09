#Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

class Sauce:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.saucedemo.com/")
        time.sleep(2)

        self.browser.find_element(By.ID, "user-name").send_keys(self.username)
        self.browser.find_element(By.NAME, "password").send_keys(self.password)
        time.sleep(1)
        self.browser.find_element(By.ID, "login-button").click()


        # sayfaya yönlendirme işlemi
        self.browser.get("https://www.saucedemo.com/inventory.html")

        # Ürün sayısını kontrol etme
        products = self.browser.find_elements(By.CLASS_NAME, "inventory_item_label")
        if len(products) == 6:
            print("Test Başarılı: Kullanıcı başarılı bir şekilde giriş yaptı ve doğru sayfaya yönlendirildi. Ürün sayısı doğru.")
        else:
            print("Test Başarısız: Ürün sayısı doğru değil.")

# giriş işlemleri burada gerçekleştirilir
username = "standard_user"  # kullanıcı adınızı buraya girin
password = "secret_sauce"  # şifrenizi buraya girin

sauce = Sauce(username, password)
sauce.signIn()
