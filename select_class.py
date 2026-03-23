from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
driver.find_element(By.XPATH,'//a[contains(text(),"Digital downloads")]').click()
sleep(1)
addtocarts=driver.find_elements(By.XPATH,'//div[@class="add-info"]/div[2]/input')

for add in addtocarts:
    add.click()
    sleep(1)

driver.find_element(By.XPATH,'(//span[@class="cart-label"])[1]').click()
driver.find_element(By.XPATH,'(//input[@name="removefromcart"])[2]').click()
driver.find_element(By.XPATH,'//input[@name="updatecart"]').click()

driver.close()