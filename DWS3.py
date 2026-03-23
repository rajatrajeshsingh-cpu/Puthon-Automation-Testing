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
#Now open the Excellent Pole
searchField = driver.find_element(By.ID, "pollanswers-1")
print(searchField)
sleep(2)
#Now open the Good Pole
searchField = driver.find_element(By.ID, "pollanswers-2")
print(searchField)
sleep(2)
#Now open the poor Pole
searchField = driver.find_element(By.ID, "pollanswers-3")
print(searchField)
sleep(2)
#Now open the Very bad Pole
searchField = driver.find_element(By.ID, "pollanswers-4")
print(searchField)
#closed the browser
driver.close()