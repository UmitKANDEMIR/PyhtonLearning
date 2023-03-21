# Test Caseler;

    #Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.

    #Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.

    #Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.

    #Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)

    #Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
    #Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Sauce:
    def test_empty_username(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        erorMassage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = erorMassage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")

    def test_empty_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("user-name")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        erorMassage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = erorMassage.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")

    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("locked_out_user")
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        erorMassage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = erorMassage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")

    def test_icon(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        loginBtn = driver.find_element(By.CLASS_NAME, "error-button")
        # loginBtn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        loginBtn.click()
        sleep(20)

    def test_valid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(5)
        listOfProduct = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı {len(listOfProduct)} adet olmalıdır")

testClass = Test_Sauce()
testClass.test_empty_username()
testClass.test_empty_password()
testClass.test_invalid_login()
testClass.test_icon()
testClass.test_valid_login()