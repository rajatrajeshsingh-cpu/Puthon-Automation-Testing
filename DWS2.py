from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt= webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
# open the browser

driver=webdriver.Chrome(options=opt)
#maximize the browser
driver.maximize_window()
# enter into dws webpage
driver.get("https://demowebshop.tricentis.com/")
searchField = driver.find_element(By.CLASS_NAME, "ico-register")
print(searchField)
sleep(3)
#Now open the login page
searchField = driver.find_element(By.CLASS_NAME, "ico-login")
print(searchField)
print(3)
#Now opening the showing Card
searchField = driver.find_element(By.CLASS_NAME, "cart-label")
print(searchField)
print(3)
searchField = driver.find_element(By.CLASS_NAME, "cart-label")
print(searchField)
print(3)
#closed the browser
driver.close()