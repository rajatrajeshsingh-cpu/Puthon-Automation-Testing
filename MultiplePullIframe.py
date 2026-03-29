from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/ui/frames/multiple?sublist=2")

sleep(3)

#Switch to first main iframe
parent_iframe = driver.find_element(By.XPATH, "(//iframe)[1]")
driver.switch_to.frame(parent_iframe)

sleep(2)

#Switch to child iframe inside first iframe
child_iframe = driver.find_element(By.XPATH, "(//iframe)[1]")
driver.switch_to.frame(child_iframe)

sleep(2)

# Fill first form
driver.find_element(By.ID, "email").send_keys("rajat12@gmail.com")
driver.find_element(By.ID, "password").send_keys("rajat")
driver.find_element(By.ID, "confirm-password").send_keys("rajat")
driver.find_element(By.ID, "submitButton").click()