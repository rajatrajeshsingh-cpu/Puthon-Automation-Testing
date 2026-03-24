from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Digital downloads')]").click()
sleep(2)
# albhum3rd=driver.find_element(By.XPATH,"//a[text()='3rd Album']/../../div[3]/div/span")
# print(albhum3rd.text)
albhum3rd=driver.find_element(By.XPATH,"//a[text()='3rd Album']/../following-sibling::div[3]/div/span")
print(albhum3rd.text)
music1 = driver.find_element(By.XPATH,'//a[contains(text(),"Music 2")]/../../div[3]/div/span')
print(music1.text)
# music =