from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/ui/frames/nested?sublist=1")

sleep(3)

# 🔹 Switch to parent frame
parent_frame = driver.find_element(By.XPATH, "//iframe")
driver.switch_to.frame(parent_frame)

sleep(2)

#Switch to first child frame (Email)
child_frames = driver.find_elements(By.TAG_NAME, "iframe")
driver.switch_to.frame(child_frames[0])

driver.find_element(By.ID, "email").send_keys("rajat12@gmail.com")
sleep(2)

#Go back to parent frame
driver.switch_to.parent_frame()

sleep(2)

#Switch to second child frame (Password)
child_frames = driver.find_elements(By.TAG_NAME, "iframe")
driver.switch_to.frame(child_frames[0])

driver.find_element(By.ID, "password").send_keys("Rajput123")

#Go back to parent frame
driver.switch_to.parent_frame()
sleep(1)
#Switch to THird Child Frame(Confirm PassWord)
child_frames = driver.find_elements(By.TAG_NAME, "iframe")
driver.switch_to.frame(child_frames[0])
sleep(2)
driver.find_element(By.ID, "confirm-password").send_keys("Rajput123")
#Go back to parent frame
driver.switch_to.parent_frame()
sleep(2)
child_frames = driver.find_elements(By.TAG_NAME, "iframe")
driver.switch_to.frame(child_frames[0])
sleep(1)

driver.find_element(By.ID,"submitButton").click()
