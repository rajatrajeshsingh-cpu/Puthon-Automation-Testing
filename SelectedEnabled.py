from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://demowebshop.tricentis.com/')


ele=driver.find_element(By.ID,"pollanswers-1")
ele.click()
sleep(2)
if ele.is_selected():
    print('Element module is Selected')
else:
    driver.close()
    raise Exception('Element module is not Selected')
driver.close()