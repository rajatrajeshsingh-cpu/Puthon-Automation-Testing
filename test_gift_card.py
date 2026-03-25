import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


@pytest.fixture()
def Pre_And_Gift():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://demowebshop.tricentis.com/")

    driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')]").click()

    yield driver

    driver.find_element(By.CSS_SELECTOR, ".ico-cart").click()
    driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()
    driver.find_element(By.XPATH, '//input[@name="updatecart"]').click()
    driver.quit()


def test_gift_001(Pre_And_Gift):
    Expected_url = "https://demowebshop.tricentis.com/5-virtual-gift-card"

    Pre_And_Gift.find_element(By.XPATH, '//input[@value="Add to cart"]').click()
    Pre_And_Gift.find_element(By.ID, "giftcard_1_RecipientName").send_keys("gift card")
    Pre_And_Gift.find_element(By.ID, "giftcard_1_RecipientEmail").send_keys("rajat.rajesh.singh@gmail.com")
    Pre_And_Gift.find_element(By.ID, "giftcard_1_SenderName").send_keys("Rajat")
    Pre_And_Gift.find_element(By.ID, "giftcard_1_SenderEmail").send_keys("rajat.rajesh.singh@gmail.com")
    Pre_And_Gift.find_element(By.ID, "giftcard_1_Message").send_keys("Hi")
    Pre_And_Gift.find_element(By.ID, "add-to-cart-button-1").click()

    Actual_Url = Pre_And_Gift.current_url
    assert Expected_url == Actual_Url, "gift card one is added"


def test_gift_002(Pre_And_Gift):
    Expected_url = "https://demowebshop.tricentis.com/5-virtual-gift-card"

    Pre_And_Gift.find_element(By.XPATH, '//input[@value="Add to cart"]').click()
    Pre_And_Gift.find_element(By.ID, "giftcard_1_RecipientName").send_keys("gift card")
    Pre_And_Gift.find_element(By.ID, "giftcard_1_RecipientEmail").send_keys("rajat.rajesh.singh@gmail.com")
    Pre_And_Gift.find_element(By.ID, "giftcard_1_SenderName").send_keys("Rajat")
    Pre_And_Gift.find_element(By.ID, "giftcard_1_SenderEmail").send_keys("rajat.rajesh.singh@gmail.com")
    Pre_And_Gift.find_element(By.ID, "giftcard_1_Message").send_keys("Hi")
    Pre_And_Gift.find_element(By.ID, "add-to-cart-button-1").click()

    Actual_Url = Pre_And_Gift.current_url
    assert Expected_url == Actual_Url, "gift card two is added"


def test_gift_003(Pre_And_Gift):
    Expected_url = "https://demowebshop.tricentis.com/5-virtual-gift-card"

    Pre_And_Gift.find_element(By.XPATH, '//input[@value="Add to cart"]').click()
    Pre_And_Gift.find_element(By.ID, "giftcard_1_RecipientName").send_keys("gift card")
    Pre_And_Gift.find_element(By.ID, "giftcard_1_SenderName").send_keys("Rajat")
    Pre_And_Gift.find_element(By.ID, "giftcard_1_Message").send_keys("Hi")
    Pre_And_Gift.find_element(By.ID, "add-to-cart-button-1").click()

    Actual_Url = Pre_And_Gift.current_url
    assert Expected_url == Actual_Url, "gift card three is added"


def test_gift_004(Pre_And_Gift):
    Expected_url = "https://demowebshop.tricentis.com/5-virtual-gift-card"

    Pre_And_Gift.find_element(By.XPATH, '//input[@value="Add to cart"]').click()
    Pre_And_Gift.find_element(By.ID, "giftcard_1_RecipientName").send_keys("gift card")
    Pre_And_Gift.find_element(By.ID, "giftcard_1_SenderName").send_keys("Rajat")
    Pre_And_Gift.find_element(By.ID, "giftcard_1_Message").send_keys("Hi")
    Pre_And_Gift.find_element(By.ID, "add-to-cart-button-1").click()

    Actual_Url = Pre_And_Gift.current_url
    assert Expected_url == Actual_Url, "gift card four is added"