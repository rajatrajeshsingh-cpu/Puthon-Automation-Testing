from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("file:///C:/Users/HP/OneDrive/Desktop/python_selenium/demo%20(1).html")
sleep(2)
multi = driver.find_element(By.ID,"multiple_cars")
sel=Select(multi)
sel.select_by_visible_text('Audi')
sleep(1)
sel.select_by_value('for')
sleep(1)
sel.select_by_index(5)
# if you want to deselect the data one by one.
# sel.deselect_by_visible_text('Audi')
# sleep(1)
# sel.deselect_by_visible_text('for')
# sleep(1)
# sel.deselect_by_index(5)
# if you want deselect the data at all.
sel.deselect_all()
sleep(2)
driver.close()