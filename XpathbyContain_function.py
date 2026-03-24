from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
driver.find_element(By.XPATH,'//a[contains(text()="Computer")]').click()
