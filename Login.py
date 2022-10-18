import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(1000)

driver.get("https://staging.bixpand.com/app/home/dashboard")

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

driver.find_element(By.XPATH,"//button[3]").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[3]/ul[1]/div[2]/p[1]").click()