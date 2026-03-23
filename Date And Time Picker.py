from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=options)
options.add_argument("--disable-notifications")
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/")
sleep(2)
driver.find_element(By.XPATH,"//p[text()='UI Testing Concepts']").click()
sleep(2)
driver.find_element(By.XPATH,"//section[text()='Date & Time Picker']").click()
sleep(2)
driver.find_element(By.XPATH,"//section[text()='Date Picker']").click()
sleep(1)
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("25-02-2026")
sleep(2)
driver.find_element(By.XPATH,"//section[text()='Time Picker']").click()