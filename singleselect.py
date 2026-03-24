from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)

driver.get("file:///C:/Users/HP/OneDrive/Desktop/python_selenium/demo%20(1).html")
driver.maximize_window()
sleep(2)
single=driver.find_element(By.ID,"standard_cars")
sel=Select(single)
sleep(2)
sel.select_by_visible_text("BMW")
sleep(2)
sel.select_by_value("jgr")
sleep(2)
sel.select_by_index(6) # here index will be start from Zero.
sleep(1)
sel.deselect_by_index(6)
sleep(1)
sel.deselect_by_visible_text("BMW")
sleep(2)
sel.deselect_by_value("jgr")
sleep(2)
driver.close()