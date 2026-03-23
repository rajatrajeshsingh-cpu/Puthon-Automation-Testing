from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()
sleep(2)
#click on the digital download
driver.find_element(By.XPATH,'//a[contains(text(),"Digital downloads")]').click()
sleep(2)


sortby=driver.find_element(By.ID,'products-orderby')
sel=Select(sortby)
opts=sel.options
count=0
for option in opts:
    sortby = driver.find_element(By.ID, 'products-orderby')
    sel=Select(sortby)
    sel.select_by_index(count)
    count+=1
    sleep(2)


Display=driver.find_element(By.ID,'products-pagesize')
sel=Select(Display)
opts=sel.options
count=0
for option in opts:
    Display = driver.find_element(By.ID, 'products-pagesize')
    sel=Select(Display)
    sel.select_by_index(count)
    count+=1
    sleep(2)



Viewas=driver.find_element(By.ID,'products-viewmode')
sel=Select(Viewas)
opts=sel.options
count=0
for option in opts:
    Viewas = driver.find_element(By.ID, 'products-viewmode')
    sel=Select(Viewas)
    sel.select_by_index(count)
    count+=1
    sleep(2)

driver.quit()