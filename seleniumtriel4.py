from selenium import webdriver

import time

from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\selenium\chromedriver_win32\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")




drop_down= driver.find_element_by_id("RESULT_RadioButton-9")
drop_down_object= Select(drop_down)
drop_down_object.select_by_value("Radio-2")