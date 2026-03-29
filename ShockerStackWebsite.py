from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.shoppersstack.com/")
sleep(10)
driver.find_element(By.ID,'loginBtn').click()
