from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

def test_dws():
    expected_Url = "https://demowebshop.tricentis.com/"
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://demowebshop.tricentis.com/")
    actual_Url = driver.current_url
    assert expected_Url == actual_Url
    driver.find_element(By.CLASS_NAME,"ico-register").click()
