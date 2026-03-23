from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)

excellent=driver.find_element(By.XPATH,"//label[text()='Excellent']")
print(excellent.text)
excellent.click()

sleep(2)

good=driver.find_element(By.XPATH,"//label[text()='Good']")
print(good.text)
good.click()

sleep(2)

Bad=driver.find_element(By.XPATH,"//label[text()='Poor']")
print(Bad.text)
Bad.click()

sleep(2)

VBad=driver.find_element(By.XPATH,"//label[text()='Very bad']")
print(VBad.text)
VBad.click()

sleep(2)

driver.close()