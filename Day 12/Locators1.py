
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#below we are launching the driver location
# serv_obj=Service("/home/priya/Drivers/chromedriver")
#below we are launching the browser
# driver=webdriver.Chrome()
driver=webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


#ID & name loactors
#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#linktext & partial linktext
#driver.find_element(By.LINK_TEXT,"Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"ist").click()

# driver.close()
# driver.text()

