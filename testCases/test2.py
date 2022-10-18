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
    notification_button=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/a[3]/span[1]/button[1]")
    driver.execute_script("arguments[0].click();",notification_button)
