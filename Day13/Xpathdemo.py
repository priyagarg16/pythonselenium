cloud_url = 'http://192.168.23.74:30004/wd/hub'

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()

options.browser_version = '111.0'
cloud_options = {
    'name': 'xpathdemo',
    'enableLogs': True,
    'enableVideo': True,
    'deviceName': 'Desktop',
    'screenResolution': '1366x768x24',
    'timeout': 60,
    'idleSessionTimeout': 60,
}
options.set_capability('cloudify:options', cloud_options)

driver = webdriver.Remote(cloud_url, options=options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# absolutexpath
driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("Books")
driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()

# relative xpath
# driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("Books")

driver.quit()