from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.shoppersstack.com/signup')
sleep(15)
reg= driver.find_element(By.ID,"Register")

if reg.is_enabled():
    driver.close()
    raise Exception("Register button is enabled and it is defect")

else:
    print("Register button is disabled and there is no Defect")

driver.close()