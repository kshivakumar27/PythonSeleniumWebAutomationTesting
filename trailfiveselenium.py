from selenium import webdriver


from selenium.webdriver.common.alert import Alert

import time

#from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\selenium\chromedriver_win32\chromedriver.exe")

driver.get("https://en.wikipedia.org/wiki/Main_Page")


#driver.find_element_by_xpath("//*[@id='mainContent']").click()

time.sleep(5)

driver.execute_script("window.scrollTo(0,document.body.scrollHieght);")