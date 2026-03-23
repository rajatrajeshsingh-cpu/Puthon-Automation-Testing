from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=options)
options.add_argument("--disable-notifications")
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/")
sleep(2)
driver.find_element(By.XPATH,"//p[text()='UI Testing Concepts']").click()
sleep(2)
driver.find_element(By.XPATH,'//section[text()="Popups"]').click()
sleep(2)

# driver.find_element(By.XPATH,'//section[text()="Javascript"]').click()
# sleep(2)
# driver.find_element(By.XPATH,'//input[@type="checkbox"]').click()
# sleep(1)
# driver.find_element(By.XPATH,'(//input[@type="checkbox"])[2]').click()
# sleep(1)
# driver.find_element(By.XPATH,'(//input[@type="checkbox"])[3]').click()
# sleep(2)
# driver.find_element(By.XPATH,'(//input[@type="checkbox"])[4]').click()
# sleep(1)
# driver.find_element(By.ID,"deleteButton").click()
# sleep(1)
# alt=driver.switch_to.alert
# alt.accept()
# sleep(2)
#
# driver.find_element(By.XPATH,'//section[text()="Authentication"]').click()
# sleep(2)
# driver.get("https://admin:admin@basic-auth-git-main-shashis-projects-4fa03ca5.vercel.app/")
# sleep(2)
# driver.back()


# driver.find_element(By.XPATH,'//section[text()="File Uploads"]').click()
# sleep(1)
# driver.find_element(By.ID,"fullName").send_keys("Rajat")
# sleep(1)
# driver.find_element(By.ID,"emailId").send_keys("rajat.88@gmail.com")
# sleep(1)
# driver.find_element(By.ID,'password').send_keys("Rajat1")
# sleep(1)
# driver.find_element(By.ID,"mobile").send_keys("8805898769")
# sleep(2)
# selectfile=driver.find_element(By.XPATH,'//input[@type="file"]')
# sleep(2)
# selectfile.send_keys("C:\Harshal_Bramhankar_Mechanical_2025.pdf")
# sleep(1)
# driver.find_element(By.XPATH,'//select[@id="city"]//option[7]').click()
# sleep(1)
# driver.find_element(By.XPATH,'//option[@value="Javascript"]').click()
# sleep(1)
# driver.find_element(By.ID,"alert").click()
# sleep(1)
# driver.find_element(By.XPATH,'//button[@type="submit"]').click()


driver.find_element(By.XPATH,"//section[text()='Notifications']").click()
