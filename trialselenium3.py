from selenium import webdriver

import time

#from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\selenium\chromedriver_win32\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

driver.find_element_by_id("RESULT_TextField-1").send_keys("shiv")

time.sleep(5)

driver.find_element_by_id("RESULT_TextField-2").send_keys("karthik")



time.sleep(5)

driver.find_element_by_id("RESULT_TextField-3").send_keys("8722748066")



time.sleep(5)

driver.find_element_by_id("RESULT_TextField-4").send_keys("karnataka")




time.sleep(5)

driver.find_element_by_id("RESULT_TextField-5").send_keys("mysure")






time.sleep(5)

driver.find_element_by_id("RESULT_TextField-6").send_keys("shiv@gmail.com")

time.sleep(5)
radio_var=driver.find_element_by_id("RESULT_RadioButton-7_0")

radio_var.click()
time.sleep(5)









#radio_var=driver.find_element_by_id("RESULT_RadioButton-7_0")

#radio_var.click()

#time.sleep(5)

driver.find_element_by_xpath("//*[@id='RESULT_CheckBox-8_0']").click()

#driver.find_element_by_id("RESULT_CheckBox-8_0").click()

#driver.find





#checkbox_var=driver.find_element_by_id("RESULT_CheckBox-8_0")

#checkbox_var.click()





#RESULT_CheckBox-8_0













#radio_var=driver.find_element_by_xpath("//*[@id="RESULT_RadioButton-7_0"]")


#radio_object=Select(radio_var) 
#driver.find_element_by_id("RESULT_RadioButton-7_0").send_keys("radio")


#q26 > table > tbody > tr:nth-child(1) > td > label

#RESULT_RadioButton-7_0