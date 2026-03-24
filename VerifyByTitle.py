from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
expected_title='Demo Web Shop'
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
actual_title = driver.title
print(actual_title)
if expected_title == actual_title:
    print("I am in my targeted web-page")
    driver.find_element(By.CLASS_NAME,"ico-register").click()

else:
    driver.close()
    raise Exception("I am not in my targeted web-page")
