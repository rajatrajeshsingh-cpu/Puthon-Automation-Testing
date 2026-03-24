from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

from Basic.VerifyByURL import actual_url

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
expected_rss = "https://demowebshop.tricentis.com/news/rss/1"
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://demowebshop.tricentis.com/')
sleep(2)
elinks = driver.find_elements(By.XPATH,'//div[@class="column follow-us"]/ul/li/a')

for elink in elinks:
    actual_url=driver.current_url
    if actual_url == expected_rss:
        driver.back()
    elink.click()
    sleep(2)

driver.quit()