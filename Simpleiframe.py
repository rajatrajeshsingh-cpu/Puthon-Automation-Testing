from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")
sleep(2)
#by iframe
# driver.switch_to.frame(0)

#by using string
driver.switch_to.frame("SingleFrame")

#by using webelement
# iframe=driver.find_element(By.NAME,"SingleFrame")
# driver.switch_to.frame(iframe)
# act=ActionChains(driver)
# act.key_down(Keys.PAGE_DOWN).perform()
# sleep(2)


driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("Rajat")
sleep(2)

#when we have to switch to main parent page
#by using praent_frame


driver.switch_to.parent_frame()
sleep(2)
driver.find_element(By.XPATH,"//a[text()='Home']").click()
