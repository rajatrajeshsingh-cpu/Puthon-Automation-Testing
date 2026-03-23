from selenium import webdriver
driver = webdriver.Chrome()  #for opening the browser
 # maximize the browser
driver.maximize_window()
#enter into demowebshop
driver.get("https://onlinesbi.sbi.bank.in/")
#Now closed the browser
driver.close()