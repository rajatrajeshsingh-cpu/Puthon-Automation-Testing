from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/")
sleep(2)
driver.find_element(By.XPATH, "//a[@class='block w-[100%] h-full']/div/main").click()
sleep(2)
driver.find_element(By.XPATH, "//section[@class='poppins text-[15px]']/../section[2]").click()
sleep(2)
driver.find_element(By.XPATH, "//section[@class='poppins text-[15px]']/../../li[7]/section[2]").click()
sleep(2)
driver.find_element(By.XPATH, "//section[text()='iframes']").click()
sleep(2)
driver.find_element(By.XPATH, "//a[text()='Nested with Multiple iframe']").click()
sleep(2)
driver.switch_to.frame(0)
sleep(2)

second_frame=driver.find_element(By.XPATH, "//div[@class='form_container']/iframe")
sleep(2)
driver.switch_to.frame(second_frame)
sleep(2)

third_frame=driver.find_element(By.XPATH, "//div[@class='form-group']/iframe")
driver.switch_to.frame(third_frame)
sleep(2)
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("Admin@gmail.com")
sleep(2)
driver.switch_to.parent_frame()

fourth_frame=driver.find_element(By.XPATH, "(//div[@class='form-group']/iframe)[2]")
driver.switch_to.frame(fourth_frame)
sleep(2)
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Admin@1234")
sleep(2)
driver.switch_to.parent_frame()


fifth_frame=driver.find_element(By.XPATH, "(//div[@class='form-group']/iframe)[3]")
driver.switch_to.frame(fifth_frame)
sleep(2)
driver.find_element(By.XPATH, "//input[@id='confirm']").send_keys("Admin@1234")
sleep(2)
driver.switch_to.parent_frame()


six_frame=driver.find_element(By.XPATH, "(//div[@class='form-group']/iframe)[4]")
driver.switch_to.frame(six_frame)
sleep(2)
driver.find_element(By.XPATH, "//button[@id='submitButton']").click()
sleep(2)

driver.switch_to.parent_frame()
sleep(2)

