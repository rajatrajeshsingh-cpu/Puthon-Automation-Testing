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
# multi = driver.find_element(By.ID,"standard_cars")  # for checking single select
# multi = driver.find_element(By.ID,"multiple_cars") # for checking multiple select.
#
#
# sel = Select(multi)
# ref = sel.is_multiple
#
# if ref:
#     sel.select_by_visible_text('Audi')
#     sleep(1)
#     sel.select_by_value('for')
#     sleep(1)
#     sel.select_by_index(5)
#     sleep(2)
#     sel.deselect_all()
# else:
#     print("the deselect option we can't perform becuses it is single level selector")
#
# sleep(2)
# driver.close()
sel = driver.find_elements(By.XPATH,'//select[@id="standard_cars"]/options')
for i in sel:
    i.click()
    sleep(1)

