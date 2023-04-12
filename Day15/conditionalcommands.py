from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("/home/priya/Drivers/chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# is_displayed()  Is_enabled()
searchbox=driver.find_element(By.XPATH,"//*[@id='small-searchterms']")

print("Display status:",searchbox.is_displayed())  #True
print("Enabled status:",searchbox.is_enabled())    #True



#is_seleted(for radio buttons and checkboxes)

rd_male=driver.find_element(By.XPATH,"//*[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//*[@id='gender-female']")

print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()