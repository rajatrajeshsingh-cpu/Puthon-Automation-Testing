from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
num = random.randint(1,10)
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
action = ActionChains(driver)
for i in range(2):
    action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.ENTER).perform()
sleep(2)
for i in range(25):
    action.key_down(Keys.TAB).perform()
action.send_keys(Keys.SPACE).perform()
sleep(1)
action.key_down(Keys.TAB).perform()
action.send_keys('Rajat').perform()
sleep(1)
action.send_keys(Keys.TAB).perform()
action.send_keys('Singh').perform()
sleep(1)
action.send_keys(Keys.TAB).perform()
action.send_keys('rajatsingh'+ str(num) +'@gmail.com').perform()
sleep(1)
action.send_keys(Keys.TAB).perform()
action.send_keys('Rajat@12').perform()
sleep(1)
action.send_keys(Keys.TAB).perform()
action.send_keys('Rajat@12').perform()
sleep(1)
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.SPACE).perform()
sleep(2)
driver.close()