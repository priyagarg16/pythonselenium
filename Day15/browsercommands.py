cloud_url = 'http://192.168.23.74:30004/wd/hub'

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
options = Options()

options.browser_version = '111.0'
cloud_options = {
    'name': 'Browsercommands.py',
    'enableLogs': True,
    'enableVideo': True,
    'deviceName': 'Desktop',
    'screenResolution': '1366x768x24',
    'timeout': 60,
    'idleSessionTimeout': 60,
}
options.set_capability('cloudify:options', cloud_options)

driver = webdriver.Remote(cloud_url, options=options)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

time.sleep(5)

driver.quit()