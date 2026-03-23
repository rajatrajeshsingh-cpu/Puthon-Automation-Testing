from selenium import webdriver
driver = webdriver.Chrome()  #for opening the browser
 # maximize the browser
driver.maximize_window()
#enter into demowebshop
driver.get("https://www.myntra.com/?utm_source=dms_google&utm_medium=dms_searchbrand_cpc&utm_campaign=dms_google_searchbrand_cpc_Search_Brand_Myntra_Brand_India_BM_TROAS_SOK_New&gad_source=1&gad_campaignid=20443628324&gbraid=0AAAAADoxBh44hu6fDIQsaBXiKbUqjxm6G&gclid=CjwKCAiA7LzLBhAgEiwAjMWzCDvZVvwxnsF0jDtL3-u1_R4WgU2Qv_32hWbY4uSCFuXVwsXRsLvoShoCJioQAvD_BwE")
#Now closed the browser
driver.close()