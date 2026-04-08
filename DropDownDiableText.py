from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://demoapps.qspiders.com/ui/dropdown/disabled?sublist=3")
sleep(2)

country=driver.find_element(By.ID,"SelectCountry")
driver.execute_script("arguments[0].value='India';",country)
sleep(2)

state=driver.find_element(By.ID,"slectState")
driver.execute_script("arguments[0].value='Maharashtra';",state)
sleep(2)

city=driver.find_element(By.ID,"citySelect")
driver.execute_script("arguments[0].value='Mumbai';",city)
sleep(2)

quant=driver.find_element(By.ID,"select_quantity")
driver.execute_script("arguments[0].value='2';",quant)
sleep(2)

driver.find_element(By.ID,"submit_btn").click()
sleep(2)

driver.close()