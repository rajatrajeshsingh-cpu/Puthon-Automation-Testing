from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
expected_url='https://demowebshop.tricentis.com/'
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
actual_url = driver.current_url
print(actual_url)
if expected_url == actual_url:
    print("I am in my targeted web-page")
    driver.find_element(By.CLASS_NAME,"ico-register").click()

else:
    print("I am not in my targeted web-page")
