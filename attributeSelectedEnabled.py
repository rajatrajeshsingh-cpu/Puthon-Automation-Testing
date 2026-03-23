from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://demowebshop.tricentis.com/')
sleep(2)
pass_data = "Mobile"
SearchField = driver.find_element(By.ID,"small-searchterms")
present_data = SearchField.get_attribute("value")
print(present_data)
SearchField.send_keys(pass_data)
sleep(2)
present_data = SearchField.get_attribute("value")
print(present_data)

if present_data==pass_data:
    print("data is sucessfully passed")

else:
    driver.close()
    raise Exception("data is not present with the expected and it is defeted ")