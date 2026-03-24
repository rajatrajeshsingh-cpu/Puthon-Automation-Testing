from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.myntra.com/?utm_source=dms_google&utm_medium=dms_searchbrand_cpc&utm_campaign=dms_google_searchbrand_cpc_Search_Brand_Myntra_Brand_India_BM_TROAS_SOK_New&gad_source=1&gad_campaignid=20443628324&gbraid=0AAAAADoxBh7IhGhn_Qj241C657ZWALF9G&gclid=CjwKCAiAtLvMBhB_EiwA1u6_Pt818SPcJqoKgv4-GC3w_w4auEqy9CiZWSc_ZxhVGzLoO70WnnlNZhoCKR4QAvD_BwE')
sleep(2)
driver.find_element(By.XPATH,'//a[@data-group="beauty"]').click()
sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Beauty Gift')]").click()