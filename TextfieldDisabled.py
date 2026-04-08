from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys
from time import sleep
opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/ui?scenario=1")
sleep(2)
driver.find_element(By.XPATH,'//li[text()="Disabled"]').click()
sleep(2)
disable_name=driver.find_element(By.ID,'name')
driver.execute_script("arguments[0].value='Admin@gmail.com'",disable_name)
sleep(2)
disable_email=driver.find_element(By.ID,'email')
driver.execute_script("arguments[0].value='Admin@gmail.com'",disable_email)
sleep(2)
disable_pass=driver.find_element(By.ID,'password')
driver.execute_script("arguments[0].value='Admin@1234'",disable_pass)
sleep(2)
driver.close()