import pytest
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from pathlib import Path
from datetime import date

class Test_Homework:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True) 

    def teardown_method(self):
        self.driver.quit()

    def waitDriver(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator)) 
    
    def test_Empty_Username(self):
        self.waitDriver((By.ID, "login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.waitDriver((By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"))
        errorMassage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_username.png")
        assert errorMassage.text == "Epic sadface: Username is required"

    @pytest.mark.parametrize("username, password", [("1","1"), ("username1","123")])
    def test_Invalid_Login(self,username,password):
        self.waitDriver((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys(username)
        self.waitDriver((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys(password)
        self.waitDriver((By.ID, "login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMassage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_invalid_login_{username}_{password}.png")
        assert errorMassage.text == "Epic sadface: Username and password do not match any user in this service"

    def test_Error_Icon(self):
        self.waitDriver((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("username")
        self.waitDriver((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("password")
        self.waitDriver((By.ID, "login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMassage = self.driver.find_element(By.CLASS_NAME, "error-message-container")
        xBtn = self.driver.find_element(By.CLASS_NAME, "error-button")
        xBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_invalid_login_username_password.png")
        assert errorMassage.text == ""

    @pytest.mark.parametrize("username, password", [("standard_user","secret_sauce"), ("performance_glitch_user","secret_sauce")])
    def test_Valid_Login(self,username,password):
        self.waitDriver((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys(username)
        self.waitDriver((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys(password)
        self.waitDriver((By.ID, "login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.waitDriver((By.ID, "add-to-cart-sauce-labs-backpack"),10)
        self.driver.save_screenshot(f"{self.folderPath}/test_valid_login_{username}_{password}.png")

    def test_addToCard(self):
        self.waitDriver((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        self.waitDriver((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        self.waitDriver((By.ID, "login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.waitDriver((By.ID, "add-to-cart-sauce-labs-backpack"))
        addProductBtn = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        addProductBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_addToCard.png")

    def test_removeToCard(self):
        self.waitDriver((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        self.waitDriver((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        self.waitDriver((By.ID, "login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.waitDriver((By.ID, "add-to-cart-sauce-labs-backpack"))
        addProduct1Btn = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        addProduct1Btn.click()
        addProduct2Btn = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        addProduct2Btn.click()
        toCard = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        toCard.click()
        removeToProduct1 = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        removeToProduct1.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_removeToCard.png")

    def test_buyProduct(self):
        self.waitDriver((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        self.waitDriver((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        self.waitDriver((By.ID, "login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.waitDriver((By.ID, "add-to-cart-sauce-labs-backpack"))
        addProduct1Btn = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        addProduct1Btn.click()
        addProduct2Btn = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        addProduct2Btn.click()
        toCard = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        toCard.click()
        checkoutBtn = self.driver.find_element(By.ID,"checkout")
        checkoutBtn.click()
        firstName = self.driver.find_element(By.ID,"first-name")
        firstName.send_keys("ali")
        lastName = self.driver.find_element(By.ID,"last-name")
        lastName.send_keys("kara")
        zipCode = self.driver.find_element(By.ID,"postal-code")
        zipCode.send_keys("0000")   
        continueBtn = self.driver.find_element(By.ID,"continue")
        continueBtn.click()
        finishBtn = self.driver.find_element(By.ID,"finish")
        finishBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_buyProduct.png")



