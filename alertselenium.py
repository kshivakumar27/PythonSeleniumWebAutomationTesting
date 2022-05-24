from selenium import webdriver

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time

#from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\selenium\chromedriver_win32\chromedriver.exe")

driver.get('https://demoqa.com/alerts')

alert_button= driver.find_element_by_id("button")

alert_button.click()

time.sleep()

alert_object=Alert(driver)
alert_object.accept()
