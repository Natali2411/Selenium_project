from selenium import webdriver


driver = webdriver.Firefox()
driver.get("https://www.google.com.ua/")
print(driver.current_window_handle)
