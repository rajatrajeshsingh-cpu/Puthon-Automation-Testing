from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/ui/dragDrop/dragToMultiple?sublist=3")
sleep(3)
action=ActionChains(driver)
MobileCover=driver.find_element(By.ID,"dragElement2")
MobileCharger=driver.find_element(By.ID,"dragElement4")
MobiledropZone=driver.find_element(By.ID,"dropZone1")
(action.click(MobileCover).click(MobileCharger).click_and_hold(MobileCover).release(MobiledropZone)).perform()

laptop= driver.find_elements(By.XPATH,'//div[@class="draggable-elemment"]')
sleep(1)
for i in laptop:
    action=ActionChains(driver)
    sleep(1)
    if i.get_attribute("id") in ["dragElement1","dragElement3"]:
        target=driver.find_element(By.ID,"dropZone2")
        action.click_and_hold(i).release(target).perform()
