from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_PyTestClass:
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://saucedemo.com/")
        self.driver.maximize_window()
        self.folderPath=str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
       
    def teardown_method(self):
        self.driver.quit()   
        
    def  test_loginBlank(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-blank-login.png")
        assert errorMessage.text =="Epic sadface: Username is required"
    
    
    @pytest.mark.parametrize("username,password",[("1",""),("kullaniciadim",""),("problem_user","")])      
    def test_NullPassword(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("1")
        passwordInput.send_keys("")
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-blank-password.png")
        assert errorMessage.text =="Epic sadface: Password is required"


    def test_LockedLogin(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),10)  
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-Locked.png")
        assert errorMessage.text =="Epic sadface: Sorry, this user has been locked out."
        
    def test_X(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),10)  
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("")
        passwordInput.send_keys("")    
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        xlen=len(self.driver.find_elements(By.CLASS_NAME,"error_icon"))
        if(xlen==2):
            errorBtn = self.driver.find_element(By.CLASS_NAME,"error-button")
            errorBtn.click()
            xlen=len(self.driver.find_elements(By.CLASS_NAME,"error_icon"))
            self.driver.save_screenshot(f"{self.folderPath}/test-x.png")
            assert xlen!=2
        else:False
   
    def test_routingLogin(self):
        self.loginOl
        getUrl=self.driver.current_url
        self.driver.save_screenshot(f"{self.folderPath}/test-routing.png")
        assert getUrl=="https://www.saucedemo.com/inventory.html"
        
        
    def test_proCount(self):
        self.loginOl  
        self.waitForElementVisible((By.CLASS_NAME, 'inventory_item'))
        count=len(self.driver.find_elements(By.CLASS_NAME, 'inventory_item'))
        self.driver.save_screenshot(f"{self.folderPath}/test-proCount.png")
        assert count==6
        
     #tüm ürünleri sepete ekleme   
    def test_addToBasket(self):
        self.loginOl()
        self.waitForElementVisible((By.CLASS_NAME, 'btn_inventory'))
        inventoryButonList=self.driver.find_elements(By.CLASS_NAME,"btn_inventory")
        for inventoryItem in inventoryButonList:
            inventoryItem.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-addtobasket.png")    
      #tüm ürünleri sepetten çıkarma  
    def test_removeToCart(self):
        self.loginOl()
        self.waitForElementVisible((By.CLASS_NAME, 'btn_inventory'))
        inventoryButonList=self.driver.find_elements(By.CLASS_NAME,"btn_inventory")
        for inventoryItem in inventoryButonList:
            inventoryItem.click()
            
        shoppingButon=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")   
        shoppingButon.click() 
        self.waitForElementVisible((By.CLASS_NAME,"cart_button"))    
        removeButonList=self.driver.find_elements(By.CLASS_NAME,"btn btn_secondary btn_small cart_button")
  
        for removeItem in removeButonList:
            removeItem.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-removetocart.png")
    
    def test_createOrder(self):
        self.loginOl()
        self.waitForElementVisible((By.CLASS_NAME, 'btn_inventory'))
        inventoryButonList=self.driver.find_elements(By.CLASS_NAME,"btn_inventory")
        for inventoryItem in inventoryButonList:
            inventoryItem.click()
        shoppingButon=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")   
        shoppingButon.click() 
        checkBtn = self.driver.find_element(By.ID, 'checkout')
        checkBtn.click()
        self.waitForElementVisible((By.ID, 'first-name'))
        firstNameInput = self.driver.find_element(By.ID, "first-name")
        self.waitForElementVisible((By.ID, 'last-name'))
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        self.waitForElementVisible((By.ID, 'postal-code'))
        postalCodeInput = self.driver.find_element(By.ID, "postal-code")    
        firstNameInput.send_keys("sena")
        lastNameInput.send_keys("ozdogan")
        postalCodeInput.send_keys("9")
        self.waitForElementVisible((By.ID, 'continue'))
        continueBtn = self.driver.find_element(By.ID, "continue")
        continueBtn.click()
        finishBtn = self.driver.find_element(By.ID, "finish")
        finishBtn.click()
        self.waitForElementVisible((By.XPATH,'//*[@id="checkout_complete_container"]/h2'))
        uyari=self.driver.find_element(By.XPATH,'//*[@id="checkout_complete_container"]/h2')
        assert uyari.text=="Thank you for your order!"
                
        
    def loginOl(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),10)  
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")    
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()   
            
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located(locator))