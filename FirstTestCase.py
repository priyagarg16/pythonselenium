#Test Case
#----------
#1) Open Web Browser (Chrome/firefox/Edge).
#2) Open URL https://opensource-demo.orangehrmlive.com/
#3) Enter username (Admin).
#4) Enter password (admin123).
#5) Click on Login.
#6) Capture title of the home page. (Actual title)
#7) Verify title of the page: OrangeHRM (Expected)
#8) close browser


from selenium import webdriver
driver=webdriver.Chrome(executable_path="/home/priya/Drivers/chromedriver")
# above statement will launch our browser
driver.get("https://opensource-demo.orangehrmlive.com/")
# above statement wi ll launch the url on browser
