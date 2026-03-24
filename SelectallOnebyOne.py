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
single=driver.find_element(By.ID,"standard_cars")
sel=Select(single)
cars = sel.options  #options it is a method , it is used to get all Web-element present in the dropdown menu
count = 0
for car in cars:
    sel.select_by_index(count)
    count+=1
    sleep(2)
