from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys

def test_starting():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(40)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
    driver.find_element(By.XPATH,'//input[@type="password"]').send_keys("admin123")
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    assignLeave=driver.find_element(By.XPATH,'//button[@title="Assign Leave"]')

    if assignLeave.is_enabled():
        print("There is no defect")
        driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()
    #
    else:
        raise Exception("assignleave is Disabled and that is a defect")

def test_leave_List():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(40)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
    driver.find_element(By.XPATH,'//input[@type="password"]').send_keys("admin123")
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    LeaveList=driver.find_element(By.XPATH,'//button[@title="Leave List"]')

    if LeaveList.is_enabled():
        print("There is no defect")
        driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()

    else:
        raise Exception("assignleave is Disabled and that is a defect")

def test_time_sheets():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(40)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
    driver.find_element(By.XPATH,'//input[@type="password"]').send_keys("admin123")
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    TimeSheets=driver.find_element(By.XPATH,'//button[@title="Timesheets"]')

    if TimeSheets.is_enabled():
        print("There is no defect")
        driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()

    else:
        raise Exception("assignleave is Disabled and that is a defect")


def test_Apply_Live():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(40)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
    driver.find_element(By.XPATH,'//input[@type="password"]').send_keys("admin123")
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    Applyleave=driver.find_element(By.XPATH,'//button[@title="Apply Leave"]')

    if Applyleave.is_enabled():
        print("There is no defect")
        driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()

    else:
        raise Exception("assignleave is Disabled and that is a defect")

def test_My_leave():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(40)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
    driver.find_element(By.XPATH,'//input[@type="password"]').send_keys("admin123")
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    Myleave=driver.find_element(By.XPATH,'//button[@//button[@title="My Leave"]]')

    if Myleave.is_enabled():
        print("There is no defect")
        driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()

    else:
        raise Exception("assignleave is Disabled and that is a defect")

def test_My_Timesheet():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(40)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
    driver.find_element(By.XPATH,'//input[@type="password"]').send_keys("admin123")
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    MyTimeSheets=driver.find_element(By.XPATH,'//button[@title="My Timesheet"]')

    if MyTimeSheets.is_enabled():
        print("There is no defect")
        driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
        driver.find_element(By.LINK_TEXT,"Logout").click()

    else:
        raise Exception("assignleave is Disabled and that is a defect")