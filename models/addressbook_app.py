from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common import by

class AddressbookApp:
    def __init__(self, driver, base_url):
        self.wd = driver
        self.wd.implicitly_wait(5)
        self.wd.get(base_url)
        self.wait = WebDriverWait(driver, 10)


    def creategroup(self, groupname, header, footer):
        wd = self.open_group_page()
        # Initialize group create
        # wd.find_element_by_name("new").click()

        gr_button = self.wait.until(ec.element_to_be_clickable((by.XPATH, '//*[@id="content"]/form/input[1]')))
        gr_button.click
        #wd.find_element_by_xpath('//*[@id="content"]/form/input[1]').click()
        # Fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(groupname)
        if not wd.find_element_by_xpath(
                "//div[@id='content']//select[normalize-space(.)='[none]']//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']//select[normalize-space(.)='[none]']//option[1]").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        wd.find_element_by_xpath("//div[@id='content']/form").click()
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.returngroup()
        self.logout()

    def returngroup(self):
        # Return to group page
        self.wd.find_element_by_link_text("group page").click()

    def open_group_page(self):
        # Open group page
        wd = self.wd
        wd.find_element_by_xpath('//*[@id="nav"]//a').click()
        return wd

    def delete_group_by_number(self, number):
        self.open_group_page()
        check_boxes = self.wd.find_elements_by_name('selected[]')
        check_boxes[number].click()
        self.wd.find_elements_by_name('delete').click()
        self.returngroup()

    def count_groups(self):
        self.open_group_page()
        return len(self.wd.find_elements_by_name('selected[]'))

    def logout(self):
        self.wd.find_element_by_xpath('//*[id="top"]//a').click()

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def quit(self):
        self.wd.quit()