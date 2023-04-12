#Test Case
# 1) Open Web Browser (Chrome/firefox/Edge).
# 2) Open URL https://opensource-demo.orangehrmlive.com/
# 3) Enter username (Admin).
# 4) Enter password (admin123).
# 5) Click on Login.
# 6) Capture title of the home page. (Actual title)
# 7) Verify title of the page: OrangeHRM (Expected)
# 8) close browser
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("/home/priya/Drivers/chromedriver")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button").click()

act_title=driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

    driver.close()



