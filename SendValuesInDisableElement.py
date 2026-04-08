from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys
options = webdriver.ChromeOptions()
options.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Datepicker.html")
sleep(3)
diableElement=driver.find_element(By.ID,"datepicker1")
driver.execute_script("arguments[0].value='02/28/2026';",diableElement)