from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

from DropDownmenu.selectoneBYone import count

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
driver.find_element(By.XPATH,'//a[contains(text(),"Digital downloads")]').click()
sleep(2)
sortBy = driver.find_element(By.ID,"products-orderby")
sel = Select(sortBy)
opts=sel.options
count=0

for opt in opts:
    sortBy = driver.find_element(By.ID, "products-orderby")
    sel = Select(sortBy)
    sel.select_by_index(count)
    count+=1
    sleep(2)

# driver.execute_script("arguments[0].click();", cart)
# if len(cart_product) > 0:
#     print("Product successfully added to cart ")
#     sleep(2)
#     driver.find_element(By.XPATH,'(//input[@type="checkbox"])[1]').click()
#     sleep(2)
#     driver.find_element(By.XPATH,'//input[@value="Update shopping cart"]').click()
#     sleep(2)
# else:
#     print('Product not added to cart ')
#     sleep(2)