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
driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()
sleep(2)
driver.switch_to.frame(1)
sleep(2)
InnerIframe=driver.find_element(By.XPATH,"//div[@class='iframe-container']//iframe")
driver.switch_to.frame(InnerIframe)
sleep(2)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Rajat Singh")
sleep(2)


