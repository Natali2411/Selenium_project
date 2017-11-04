from selenium import webdriver
import time
#driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
driver = webdriver.Firefox()
driver.get("https://www.google.com.ua/")

driver.find_element_by_id("lst-ib").send_keys('python')
driver.find_element_by_name('btnK').click()
time.sleep(3)
#driver.find_element_by_css_selector('.classname.anotherClassName')
t = driver.find_elements_by_partial_link_text('Python')
print(len(t))
t[2].click()


#driver.close()
