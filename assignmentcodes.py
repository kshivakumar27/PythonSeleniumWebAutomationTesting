from selenium import webdriver

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time

#from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\selenium\chromedriver_win32\chromedriver.exe")

driver.get('http://automationpractice.com/index.php') 



#abc=driver.find_element_by_xpath("//*[@id='header']").click()
#abc.click()
#alert_button= driver.find_element_by_id("header")

#alert_button.click()
a1= driver.find_element_by_class_name("login")

a1.click()

#

a2=driver.find_element_by_id("email_create").send_keys("kshivakumar145@gmail.com")
time.sleep(2)
a3=driver.find_element_by_id("SubmitCreate")
#

a3.click()
time.sleep(2)


#SubmitLogin


a4=driver.find_element_by_id("id_gender1")


a4.click()
time.sleep(2)


a5=driver.find_element_by_id("customer_firstname").send_keys("shiva")
time.sleep(2)


a6=driver.find_element_by_id("customer_lastname").send_keys("kumarK")
time.sleep(2)
a7=driver.find_element_by_id("passwd").send_keys("zxcvbnml")
time.sleep(2)


a9=driver.find_element_by_id("firstname").send_keys("shiva")
time.sleep(2)


a10=driver.find_element_by_id("lastname").send_keys("kumarK")
time.sleep(2)

a8=driver.find_element_by_id("address1").send_keys("Mellahalli")
time.sleep(2)


a11=driver.find_element_by_id("city").send_keys("KGF")
time.sleep(2)


a12=driver.find_element_by_id("id_state").send_keys("karnataka")
time.sleep(2)




a13=driver.find_element_by_id("postcode").send_keys("5700")
time.sleep(2)

#uniform-id_country



a9=driver.find_element_by_id("submitAccount")
#

a9.click()


"""


# each step validation checking by adding one-one test script please go through ......


a2=driver.find_element_by_id("email").send_keys("kshivakumar145@gmail.com")
time.sleep(2)
a2=driver.find_element_by_id("passwd").send_keys("zxcvbnml")
time.sleep(2)
time.sleep(2)
a3=driver.find_element_by_id("SubmitLogin")
#

a3.click()
time.sleep(2)
"""

