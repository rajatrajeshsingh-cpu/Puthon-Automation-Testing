import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


@pytest.fixture()
def Pre_And_Digital():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(20)

    driver.get("https://demowebshop.tricentis.com/")

    # login
    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.ID, "Email").send_keys("rajat.rajesh.singh@gmail.com")
    driver.find_element(By.ID, "Password").send_keys("yourpassword")
    driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

    driver.find_element(By.LINK_TEXT, "Digital downloads").click()

    yield driver

    # teardown
    try:
        driver.find_element(By.LINK_TEXT, "Log out").click()
    except:
        pass

    driver.quit()


def test_digital_downloads(Pre_And_Digital):

    Expected_url = "https://demowebshop.tricentis.com/cart"

    # add all products
    products = Pre_And_Digital.find_elements(By.XPATH, "//input[@value='Add to cart']")

    for product in products:
        product.click()

    # open cart
    Pre_And_Digital.find_element(By.CSS_SELECTOR, ".ico-cart").click()

    # get all prices
    prices = Pre_And_Digital.find_elements(By.CSS_SELECTOR, "span.product-unit-price")

    price_list = []

    for p in prices:
        value = p.text.replace("$", "")
        price_list.append(float(value))

    max_price = max(price_list)

    # remove highest price product
    rows = Pre_And_Digital.find_elements(By.XPATH, "//tr[contains(@class,'cart-item-row')]")

    for row in rows:
        price = row.find_element(By.CSS_SELECTOR, "span.product-unit-price").text.replace("$", "")

        if float(price) == max_price:
            row.find_element(By.NAME, "removefromcart").click()
            break

    Pre_And_Digital.find_element(By.NAME, "updatecart").click()

    Actual_url = Pre_And_Digital.current_url

    assert Expected_url in Actual_url, "Digital download test completed"