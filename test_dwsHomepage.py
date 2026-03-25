import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

@pytest.fixture()

def pre_and_post():
    driver = webdriver.Chrome(options = options)
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://demowebshop.tricentis.com/")
    driver.find_element(By.CLASS_NAME,"ico-login").click()
    driver.find_element(By.ID,"Email").send_keys("admin02@gmail.com")
    driver.find_element(By.ID,"Password").send_keys("Admin02")
    driver.find_element(By.CSS_SELECTOR,".button-1.login-button").click()
    yield driver
    driver.find_element(By.CSS_SELECTOR,"ico-logout").click()
    driver.quit()

def test_tc_001(pre_and_post):
    expected_Url = "https://demowebshop.tricentis.com/books"
    pre_and_post.find_element(By.XPATH,"//a[contains(text(),'Books')]").click()
    actural_Url = pre_and_post.current_url
    assert expected_Url == actural_Url,"navigated to the book section"

def test_tc_002(pre_and_post):
    expected_Url = "https://demowebshop.tricentis.com/computers"
    pre_and_post.find_element(By.XPATH,"//a[contains(text(),'Computers')]").click()
    actural_Url = pre_and_post.current_url
    assert expected_Url == actural_Url,"navigated to the computers section"

def test_tc_003(pre_and_post):
    expected_Url = "https://demowebshop.tricentis.com/electronics"
    pre_and_post.find_element(By.XPATH,"//a[contains(text(),'Electronics')]").click()
    actural_Url = pre_and_post.current_url
    assert expected_Url == actural_Url,"navigated to the electronics section"

def test_tc_004(pre_and_post):
    expected_Url = "https://demowebshop.tricentis.com/apparel-shoes"
    pre_and_post.find_element(By.XPATH, "//a[contains(text(),'Apparel & Shoes')]").click()
    actural_Url = pre_and_post.current_url
    assert expected_Url == actural_Url, "navigated to the Apparel & Shoes section"

def test_tc_005(pre_and_post):
    expected_Url = "https://demowebshop.tricentis.com/digital-downloads"
    pre_and_post.find_element(By.XPATH, "//a[contains(text(),'Digital downloads')]").click()
    actural_Url = pre_and_post.current_url
    assert expected_Url == actural_Url, "navigated to the Digital downloads section"

def test_tc_006(pre_and_post):
    expected_Url = "https://demowebshop.tricentis.com/jewelry"
    pre_and_post.find_element(By.XPATH, "//a[contains(text(),'Jewelry')]").click()
    actural_Url = pre_and_post.current_url
    assert expected_Url == actural_Url, "navigated to the Jewelry section"

def test_tc_007(pre_and_post):
    expected_Url = "https://demowebshop.tricentis.com/gift-cards"
    pre_and_post.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')]").click()
    actural_Url = pre_and_post.current_url
    assert expected_Url == actural_Url, "navigated to the Gift Cards section"


