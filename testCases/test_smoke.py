import time

from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest
from pageObjects.dashboard_page import DashboardPage

class Test_001_login:
    baseurl = ReadConfig.getAppUrl()
    useremail = ReadConfig.getEmail()
    userpass = ReadConfig.getPassword()

    def test_login(self,setup):
        self.driver = setup
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


    def test_invalid_login(self,setup):
        self.driver = setup
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

    def test_Logout(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@1234")
        self.lp.clickLogin()
        self.lp.closeAlertLogin()
        time.sleep(4)
        self.lp.clickOnprofile()
        time.sleep(2)
        self.lp.clickOnlogout()
        self.lp.clickOnlogoutAgreebutton()
        login_text=self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/p[1]").text
        if login_text=="Login":
            assert True
            print("logout test pass")
            self.driver.close()
        else:
            print("logout fail")
            self.driver.close()
            assert False

    def test_lead_finder(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@1234")
        self.lp.clickLogin()
        self.lp.closeAlertLogin()
        time.sleep(4)
        self.db=DashboardPage(self.driver)
        self.db.clickOnLeadfinder()
        lead_text=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Lead Finder']").text
        if lead_text=="Lead Finder":
            print("Lead finder page is not blank test pass")
            assert True
            self.driver.close()
        else:
            print("Lead finder page is having some issue")
            self.driver.close()
            assert False

    def test_appointment(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@1234")
        self.lp.clickLogin()
        self.lp.closeAlertLogin()
        time.sleep(4)
        self.db = DashboardPage(self.driver)
        self.db.clickOnAppointment()
        appointment_text=self.driver.find_element(By.XPATH,"//span[normalize-space()='Events']").text
        if appointment_text=="Events":
            print("Appointment page is not blank")
            assert True
            self.driver.close()
        else:
            print("Appointment page is having some issue")
            self.driver.close()
            assert False

    def test_capture_leads(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@1234")
        self.lp.clickLogin()
        self.lp.closeAlertLogin()
        time.sleep(10)
        self.db = DashboardPage(self.driver)
        self.db.clickOnCaptureLeads()
        time.sleep(10)
        leads_text=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Capture Leads (Website Forms)']").text
        if leads_text=="Capture Leads (Website Forms)":
            print("Capture Leads page is not blank test pass")
            assert True
            self.driver.close()
        else:
            print("Capture page is having some isssue")
            self.driver.close()
            assert False

    def test_contacts(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@1234")
        self.lp.clickLogin()
        self.lp.closeAlertLogin()
        time.sleep(10)
        self.db = DashboardPage(self.driver)
        self.db.clickOnContacts()
        contact_grid_text=self.driver.find_element(By.XPATH,"//div[contains(text(),'Name')]").text
        if contact_grid_text=="Name":
            print("Contact page is not blank test case pass")
            assert True
            self.driver.close()
        else:
            print("Contact page is having some issue")
            self.driver.close()
            assert False

    def test_email_marketing(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@1234")
        self.lp.clickLogin()
        self.lp.closeAlertLogin()
        time.sleep(5)
        self.db = DashboardPage(self.driver)
        self.db.clickOnEmailMarketing()
        email_marketing_text=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Email Marketing Campaigns']").text
        if email_marketing_text=="Email Marketing Campaigns":
            print("Email Marketing page is not blank test pass...!")
            assert True
            self.driver.close()
        else:
            print("Email marketing page is having some issue")
            self.driver.close()
            assert False

    def test_text_marketing(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@1234")
        self.lp.clickLogin()
        self.lp.closeAlertLogin()
        time.sleep(5)
        self.db = DashboardPage(self.driver)
        self.db.clickOnTextMarketing()
        text_marketing_text=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Text Marketing Campaigns']").text
        if text_marketing_text=="Text Marketing Campaigns":
            print("Text marketing page is not blank")
            assert True
            self.driver.close()
        else:
            print("There is some issue in text marketing page")
            self.driver.close()
            assert False

    # def test_sales_pipeline(self,setup):
    #     self.driver = setup
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(1000)
    #     self.driver.get(self.baseurl)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setEmail(self.useremail)
    #     self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@1234")
    #     self.lp.clickLogin()
    #     self.lp.closeAlertLogin()
    #     time.sleep(5)
    #     self.db = DashboardPage(self.driver)
    #     self.db.clickOnSalesPipeline()
    #     sales_pipeline_text=self.driver.find_element(By.XPATH,"")

    def test_manage_reputation(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@1234")
        self.lp.clickLogin()
        self.lp.closeAlertLogin()
        time.sleep(10)
        self.db = DashboardPage(self.driver)
        self.db.clickOnManageReputation()
        time.sleep(5)
        reputation_text=self.driver.find_element(By.XPATH,"//h1[normalize-space()='Reputation Board']").text
        if reputation_text=="Reputation Board":
            print("Manage Reputation Page is not blank test pass")
            assert True
            self.driver.close()
        else:
            print("Manage reputation board is having some issue")
            self.driver.close()
            assert False

    def test_settings(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@1234")
        self.lp.clickLogin()
        self.lp.closeAlertLogin()
        time.sleep(10)
        self.db = DashboardPage(self.driver)
        self.db.clickOnSettings()
        time.sleep(5)
        setting_text=self.driver.find_element(By.XPATH,"//b[normalize-space()='Business Settings']").text
        if setting_text=="Business Settings":
            print("Settings page is not blank")
            assert True
            self.driver.close()
        else:
            print("Setting page is having some issue")
            self.driver.close()
            assert False

    def test_favourite(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@1234")
        self.lp.clickLogin()
        self.lp.closeAlertLogin()
        time.sleep(10)
        self.db = DashboardPage(self.driver)
        self.db.clickOnLeadfinder()
        time.sleep(2)
        self.db.clickOnFavourite()
        favoorite_text=self.driver.find_element(By.XPATH,"//h1[normalize-space()='Favourites']").text
        if favoorite_text=="Favourites":
            print("Dashboard page is not blank")
            self.driver.close()
            assert True
        else:
            print("Dashboard page is having issue")
            self.driver.close()
            assert False


    def test_bixbox(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@1234")
        self.lp.clickLogin()
        self.lp.closeAlertLogin()
        time.sleep(10)
        self.db = DashboardPage(self.driver)
        self.db.clickOnBixbox()
        time.sleep(3)
        bixbox_text=self.driver.find_element(By.XPATH,"//*[contains(text(),'BixBox')]").text
        if bixbox_text=="BixBox":
            print("BixBox is working fine")
            assert True
            self.driver.close()
        else:
            print("There is some issue in bixbox")
            self.driver.close()
            assert False


    def test_notification(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@1234")
        self.lp.clickLogin()
        self.lp.closeAlertLogin()
        time.sleep(10)
        self.db = DashboardPage(self.driver)
        time.sleep(5)
        # self.db.clickOnNotification()
        notification_button = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/a[3]/span[1]/button[1]")
        self.driver.execute_script("arguments[0].click();", notification_button)
        notification_text=self.driver.find_element(By.XPATH,"//h1[normalize-space()='Notifications']").text
        if notification_text=="Notifications":
            print("Notification working fine")
            assert True
            self.driver.close()
        else:
            print("There is some issue in notification window")
            self.driver.close()
            assert False

    def test_help(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.useremail)
        self.driver.find_element(By.XPATH, "//input[@id='outlined-adornment-password']").send_keys("bix@1234")
        self.lp.clickLogin()
        self.lp.closeAlertLogin()
        time.sleep(10)
        self.db = DashboardPage(self.driver)
        time.sleep(3)
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/a[4]/*[name()='svg'][1]").click()
        help_text=self.driver.find_element(By.XPATH,"//h1[normalize-space()='Connect to Grow Sales']").text
        if help_text=="Connect to Grow Sales":
            print("Help section working fine")
            assert True
            self.driver.close()
        else:
            print("There is some issue in help ssection")
            self.driver.close()
            assert False

