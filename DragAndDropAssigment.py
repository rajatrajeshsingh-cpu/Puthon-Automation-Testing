from selenium import webdriver
from time import  sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/")
sleep(3)
driver.find_element(By.XPATH, "//section[@class='flex justify-between items-center w-[42vw]  gap-6']/a").click()
sleep(2)
driver.find_element(By.XPATH, "//section[text()='Web Elements']").click()
sleep(2)
driver.find_element(By.XPATH, "//section[text()='Mouse Actions']").click()
sleep(2)
driver.find_element(By.XPATH, "//section[text()='Drag & Drop']").click()
sleep(2)
driver.find_element(By.XPATH, "//a[text()='Drag Position']").click()
sleep(2)


actions = ActionChains(driver)

a=driver.find_element(By.XPATH, "//div[text()='Mobile Charger']")
b=driver.find_element(By.XPATH, "//div[text()='Laptop Charger']")
c=driver.find_element(By.XPATH, "//div[text()='Mobile Cover']")
d=driver.find_element(By.XPATH, "//div[text()='Laptop Cover']")

mobile=driver.find_element(By.XPATH, "//div[@class='drop-column  min-h-[200px] bg-slate-100']")
laptop=driver.find_element(By.XPATH, "//div[@class='drop-column  min-h-[200px] bg-slate-100']/../div[2]")

actions.click_and_hold(a).release(mobile).perform()
sleep(1)
actions.click_and_hold(c).release(mobile).perform()
sleep(1)
actions.click_and_hold(b).release(laptop).perform()
sleep(1)
actions.click_and_hold(d).release(laptop).perform()
sleep(1)