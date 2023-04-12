from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service ("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/login/")
driver.maximize_window()

# tag&ID
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")

# tag&class
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")

# tag&attribute
# driver.find_element(By.CSS_SELECTOR,"input[aria-label=Email address or phone number]").send_keys("abc@gmail.com")


# tag class& attribute
driver.find_elements(By.CSS_SELECTOR,"input.inputtext[]").send_keys("abc@gmail.com")
