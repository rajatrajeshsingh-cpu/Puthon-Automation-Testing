from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.oracle.com/in/java/technologies/downloads/")
sleep(2)
lock_symbol=driver.find_element(By.LINK_TEXT,'jdk-17.0.18_linux-x64_bin.rpm')
driver.execute_script("arguments[0].scrollIntoView(false)",lock_symbol)
lock_symbol.click()
wait=WebDriverWait(driver,10)
disable_element=wait.until(Ec.presence_of_element_located((By.LINK_TEXT,'Download jdk-17.0.18_linux-x64_bin.rpm')))
driver.execute_script("arguments[0].click();",disable_element)