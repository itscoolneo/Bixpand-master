from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium

class DashboardPage:
    lead_finder_xpath="//*[name()='path' and contains(@d,'M5.02893 1')]"
    appointment_xpath="//*[name()='path' and contains(@d,'M27 6H3V26')]"
    capture_leads_xpath="//p[normalize-space()='Capture Leads (Forms)']"
    contact_xpath="/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/center[1]/div[1]/div[4]/div[1]/div[1]/div[1]/center[1]/div[1]"
    email_marketing_xpath="(//center)[7]"
    text_marketing_xpath="(//center)[8]"
    sales_pipeline_xpath="(//center)[9]"
    manage_reputation_xpath="(//center)[10]"
    setting_xpath="//*[name()='path' and contains(@d,'M229.149,2')]"
    favourite_icon_xpath="//a[@title='Favorites']"
    bixbox_xpath="//a[@href='/app/chat']"
    notification_xpath="/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/a[3]/span[1]/button[1]"
    help_xpath="/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/a[4]/*[name()='svg'][1]"

    def __init__(self,driver):
        self.driver=driver


    def clickOnLeadfinder(self):
        self.driver.find_element(By.XPATH,self.lead_finder_xpath).click()

    def clickOnAppointment(self):
        self.driver.find_element(By.XPATH,self.appointment_xpath).click()

    def clickOnCaptureLeads(self):
        self.driver.find_element(By.XPATH,self.capture_leads_xpath).click()

    def clickOnContacts(self):
        self.driver.find_element(By.XPATH,self.contact_xpath).click()

    def clickOnEmailMarketing(self):
        self.driver.find_element(By.XPATH,self.email_marketing_xpath).click()

    def clickOnTextMarketing(self):
        self.driver.find_element(By.XPATH,self.text_marketing_xpath).click()

    def clickOnSalesPipeline(self):
        self.driver.find_element(By.XPATH,self.sales_pipeline_xpath).click()

    def clickOnManageReputation(self):
        self.driver.find_element(By.XPATH,self.manage_reputation_xpath).click()

    def clickOnSettings(self):
        self.driver.find_element(By.XPATH,self.setting_xpath).click()

    def clickOnFavourite(self):
        self.driver.find_element(By.XPATH,self.favourite_icon_xpath).click()

    def clickOnBixbox(self):
        self.driver.find_element(By.XPATH,self.bixbox_xpath).click()

    def clickOnNotification(self):
    #     self.driver.find_element(By.XPATH,self.notification_xpath).click()
        self.driver.execute_script("arguments[0].click();",self.notification_xpath)

    # def clickOnHelp(self):
    #     self.driver.execute_script("arguments[0].click();",self.help_xpath)

