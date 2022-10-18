import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(1000)

driver.get("https://staging.bixpand.com/app/home/dashboard")
for i in range(30):
    driver.find_element(By.XPATH,"//input[@name='email']").click()
    driver.find_element(By.XPATH,"//input[@name='email']").send_keys("coolneo81@gmail.com")
    driver.find_element(By.XPATH,"//input[@id='outlined-adornment-password']").send_keys("bix@1234")
    driver.find_element(By.XPATH,"//span[@class='MuiButton-label']").click()
    driver.find_element(By.XPATH,"//button[@aria-label='close']").click()
    dashboard_text = driver.find_element(By.XPATH,"//h1[normalize-space()='Favourites']").text
    if dashboard_text=="Favourites":
        assert True
        print("Login test pass")
    else:
        print("Something went wrong login test failed")
    time.sleep(5)
    driver.find_element(By.XPATH,"//*[name()='path' and contains(@d,'M5.02893 1')]").click() #lead finder xpath
    time.sleep(20)
    driver.back()
    time.sleep(10)
    driver.find_element(By.XPATH,"//*[name()='path' and contains(@d,'M27 6H3V26')]").click()
    time.sleep(20)
    driver.back()
    time.sleep(10)
    driver.find_element(By.XPATH,"//p[normalize-space()='Capture Leads (Forms)']").click()
    time.sleep(25)
    driver.back()
    time.sleep(5)
    driver.find_element(By.XPATH,"(//center)[6]").click()
    time.sleep(10)
    driver.back()
    time.sleep(10)
    driver.find_element(By.XPATH,"(//center)[7]").click()
    time.sleep(15)
    driver.back()
    time.sleep(5)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/center[1]/div[1]/div[4]/div[1]/div[1]/div[1]/center[1]/div[1]").click()
    time.sleep(20)
    driver.back()
    time.sleep(10)
    driver.find_element(By.XPATH,"//button[3]").click()
    time.sleep(20)
    driver.find_element(By.XPATH,"/html[1]//div[2]/p[1]").click()
    time.sleep(20)
    driver.find_element(By.XPATH,"//span[normalize-space()='Agree']").click()
    time.sleep(20)
