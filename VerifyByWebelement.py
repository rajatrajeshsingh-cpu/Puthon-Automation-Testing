from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()
sleep(2)
# try:
#     poll=driver.find_element(By.XPATH,"//strong[text()='Community poll']")
#     driver.find_element(By.ID,"pollanswers-1").click()
#     print("I am in  my Target web Element")
# except BaseException:
#     driver.close()
#     raise Exception("I am not in my target web-element")
#
# sleep(2)
# driver.close()
poll=driver.find_elements(By.XPATH,"//strong[text()='Community poll']")
sleep(2)
if  len(poll)>0:
    driver.find_element(By.ID, "pollanswers-1").click()
    print("I am in  my Target web Element")

else:
    driver.close()
    raise Exception("I am not in my target web-element")

sleep(2)
driver.close()

