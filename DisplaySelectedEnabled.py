from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://demowebshop.tricentis.com/')

ele=driver.find_element(By.XPATH,'//a[contains(text(),"Electronics")]')
sleep(2)
if ele.is_displayed():
    print('Element module is displayed')
else:
    driver.close()
    raise Exception('Element module is not displayed')
driver.close()