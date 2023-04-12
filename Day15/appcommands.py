cloud_url = 'http://192.168.23.74:30004/wd/hub'

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.browser_version = '111.0'
cloud_options = {
    'name': 'Appcommands.py',
    'enableLogs': True,
    'enableVideo': True,
    'deviceName': 'Desktop',
    'screenResolution': '1366x768x24',
    'timeout': 60,
    'idleSessionTimeout': 60,
}
options.set_capability('cloudify:options', cloud_options)
driver = webdriver.Remote(cloud_url, options=options)

# pass the application url
driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()
