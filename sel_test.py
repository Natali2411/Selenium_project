from selenium import webdriver
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time
#driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
driver = webdriver.Firefox()
#driver.implicitly_wait(5)
driver.get("https://www.google.com.ua/")
'''
driver.find_element_by_id("lst-ib").send_keys('python')
driver.find_element_by_name('btnK').click()
time.sleep(3)
#driver.find_element_by_css_selector('.classname.anotherClassName')
t = driver.find_elements_by_partial_link_text('Python')
print(len(t))
t[2].click()'''

driver.find_element_by_id("lst-ib").send_keys('python')
driver.find_element_by_name('btnK').click()
wait = WebDriverWait(driver, 15)
el = wait.until(presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, 'Python')))
print(len(el))
el[2].click()

#driver.close()
