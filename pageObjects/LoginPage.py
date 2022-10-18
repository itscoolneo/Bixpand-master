from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium

class LoginPage:
    email_xpath="//input[@name='email']"
    pass_xpath="//input[@id='outlined-adornment-password']"
    login_xpath="//span[@class='MuiButton-label']"
    alert_popup_xpath="//button[@aria-label='close']"
    profile_xpath="//button[3]"
    logout_xpath="/html[1]/body[1]/div[2]/div[3]/ul[1]/div[2]/p[1]"
    logout_agree_xpath="//span[normalize-space()='Agree']"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)

    def clickPassword(self):
        self.driver.find_element(By.XPATH,self.pass_xpath).click()

    def setPassword(self,userpass):
        self.driver.find_element(By.XPATH,"//input[@id='outlined-adornment-password']").send_keys(userpass)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.login_xpath).click()

    def closeAlertLogin(self):
        self.driver.find_element(By.XPATH,self.alert_popup_xpath).click()

    def clickOnprofile(self):
        self.driver.find_element(By.XPATH,self.profile_xpath).click()

    def clickOnlogout(self):
        self.driver.find_element(By.XPATH,self.logout_xpath).click()

    def clickOnlogoutAgreebutton(self):
        self.driver.find_element(By.XPATH,self.logout_agree_xpath).click()