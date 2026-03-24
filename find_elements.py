from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
polls=driver.find_elements(By.NAME,"pollanswers-1")
for poll in polls:
    poll.click()
    sleep(2)
'''
#second ways to find the multiple element.
'''

# links = driver.find_elements(By.XPATH,'//div[@class="header-links"]/ul/li/a')
# for link in links:
#     link.click()
#     sleep(2)
#     driver.back()
#     sleep(2)