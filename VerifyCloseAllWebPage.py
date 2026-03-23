from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

expected_url='https://demowebshop.tricentis.com/'
driver=webdriver.Chrome(options=options)

driver.maximize_window()
expected_title="Demo Web Shop. Build your own cheap computer"
driver.get('https://demowebshop.tricentis.com/')
sleep(2)

if expected_url==driver.current_url:
    print("i am in dws Homepage")
    driver.find_element(By.XPATH,'(//input[@value="Add to cart"])[3]').click()
    sleep(2)
    if expected_title==driver.title:
        print("i am build your cheap computer form filling section")
        driver.find_element(By.ID,"product_attribute_72_5_18_65").click()
        driver.find_element(By.ID,"product_attribute_72_6_19_91").click()
        driver.find_element(By.ID,"product_attribute_72_3_20_58").click()
        driver.find_element(By.ID,"product_attribute_72_8_30_93").click()
        driver.find_element(By.ID,"product_attribute_72_8_30_94").click()
        driver.find_element(By.ID,"product_attribute_72_8_30_95").click()
        qty=driver.find_element(By.ID,"addtocart_72_EnteredQuantity")
        qty.clear()
        qty.send_keys("2")
        driver.find_element(By.ID,"add-to-cart-button-72").click()
        sleep(4)
        # driver.find_element(By.CLASS_NAME,"close").click()
        sleep(2)
        driver.find_element(By.LINK_TEXT,"Shopping cart").click()
        sleep(2)
        CheapComputer=driver.find_elements(By.XPATH,"//a[text()='Build your own cheap computer']")
        if len(CheapComputer)>0:
            print("product add sucessfully")
            driver.find_element(By.XPATH,'//input[@name="removefromcart"]').click()
            sleep(2)
            driver.find_element(By.XPATH,'//input[@name="updatecart"]').click()
            sleep(2)
            driver.close()
        else:
            driver.close()
            raise Exception("product is not added to the shopping card")


    else:
        driver.close()
        raise Exception("We are at wrong title ")

else:
    driver.close()
    raise Exception("We are not in web page url")




# actual_url=driver.current_url
# actual_title=driver.title
#
# print(actual_url)
# sleep(2)
# print(actual_title)
# sleep(2)
#
# if actual_url==expected_url:
#     driver.find_element(By.XPATH,'//a[text()="Build your own cheap computer"]').click()
#     sleep(2)
# else:
#     print('iam not in the targeted page')
#     sleep(2)
# expected_product_title='Demo Web Shop. Build your own cheap computer'
# actual_product_title=driver.title
# if actual_product_title==expected_product_title:
#     driver.find_element(By.XPATH, '//ul[@class="option-list"]/li[3]/input').click()
#     sleep(2)
#     driver.find_element(By.XPATH,'(//ul[@class="option-list"])[2]/li[1]/input').click()
#     sleep(2)
#     driver.find_element(By.XPATH,'(//ul[@class="option-list"])[3]/li[2]/input').click()
#     sleep(2)
#     driver.find_element(By.XPATH,'(//ul[@class="option-list"])[4]/li[2]/input').click()
#     qty=driver.find_element(By.XPATH,'//input[@value="1"]/../../div/input[1]')
#     qty.clear()
#     sleep(1)
#     qty.send_keys(2)
#     sleep(1)
#     driver.find_element(By.XPATH,'//input[@value="1"]/../../div/input[2]').click()
#     sleep(2)
# else:
#     print('I am not in the targeted product page')
#     sleep(2)
#
# #shopping cart
# cart = driver.find_element(By.XPATH,'//span[contains(text(),"Shopping cart")]')
# cart.click()
#
# sleep(2)
# cart_product=driver.find_elements(By.XPATH, '//a[text()="Build your own cheap computer"]')
# driver.find_element(By.XPATH,'(//input[@type="checkbox"])[1]').click()
# sleep(2)
# driver.find_element(By.XPATH,'//input[@value="Update shopping cart"]').click()
# sleep(2)
#
# driver.quit()