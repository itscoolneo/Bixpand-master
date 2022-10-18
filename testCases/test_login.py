import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
import pytest


class Test_001_login:
    baseurl = ReadConfig.getAppUrl()
    useremail = ReadConfig.getEmail()
    userpass = ReadConfig.getPassword()

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp =LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH,"//input[@id='outlined-adornment-password']").send_keys("bix@1234")
        # self.lp.setPassword(self.userpass)
        self.lp.clickLogin()
        self.lp.closeAlertLogin()
        dashboard_text= self.driver.find_element(By.XPATH,"//h1[normalize-space()='Favourites']").text
        if dashboard_text=="Favourites":
            self.driver.save_screenshot(".\\Screenshots\\" + "Dashboard.png")
            assert True
            print("Login Test Passed..!")
            time.sleep(3)
            self.driver.close()
        else:
            print("Login Test Failed..!")
            self.driver.close()
            assert False


    def test_invalid_login(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp =LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH,"//input[@id='outlined-adornment-password']").send_keys("bix@12345")
        # self.lp.setPassword(self.userpass)
        self.lp.clickLogin()
        time.sleep(3)
        status_msg=self.driver.find_element(By.XPATH,"//div[@role='alert']").text
        print(status_msg)
        if status_msg=="Invalid password.":
            assert True
            print("Invalid login failed,test case passed..!")
            self.driver.close()
        else:
            print("Invalid login test passed..!")
            self.driver.close()

    # def test_Logout(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(1000)
    #     self.driver.get(self.baseurl)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setEmail(self.useremail)
    #     self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@12345")
    #     # self.lp.setPassword(self.userpass)
    #     self.lp.clickLogin()
    #     self.lp.clickOnprofile()