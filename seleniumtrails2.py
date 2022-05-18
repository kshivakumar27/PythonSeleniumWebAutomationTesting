from selenium import webdriver
#from selenium.webdriver.common.keys import keys
driver = webdriver.Chrome(executable_path="D:\selenium\chromedriver_win32\chromedriver.exe")
driver.get("http://tutorialsninja.com/demo/index.php?route=common/home")
#search_bar = driver.find_element_by_name("search")
search_bar1 = driver.find_element_by_class_name("dropdown-toggle")
search_bar2 = driver.find_elements_by_id("cart")
#search_bar3 = driver.find_elements_by_css_selector("")
driver.find_element_by_name('search').send_keys('iPhone')
#driver.find_elements_by_css_selector(".center")
#search_bar7 = driver.find_element_by_xpath("//button[@class='btn btn-default btn-lg']").click()
search_bar4 = driver.find_element_by_xpath("//*[@id='search']/input")
#search_bar5 = driver.implicitly_wait(2)

search_bar6 = driver.find_element_by_css_selector("[alt='iPhone']")

#print(search_bar)
print(search_bar1)
print(search_bar2)
#print(search_bar3)
print(search_bar4)
#print(search_bar5)
print(search_bar6)
#print(search_bar7)



