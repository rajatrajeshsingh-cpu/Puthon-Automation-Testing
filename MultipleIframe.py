from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/ui/frames?sublist=0")

sleep(3)

# 🔹 Switch to iframe first
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# 🔹 Now interact with elements inside iframe
driver.find_element(By.ID, "username").send_keys("Rajat")
sleep(2)

driver.find_element(By.ID, "password").send_keys("Rajput")
sleep(2)

driver.find_element(By.ID, "submitButton").click()