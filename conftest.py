import pytest
from selenium import webdriver
from models.addressbook_app import AddressbookApp


@pytest.fixture(scope="session")
def app():
    driver = webdriver.Chrome()
    base_url = "http://192.168.0.61/addressbook/"
    appl = AddressbookApp(driver, base_url)
    yield appl
    appl.quit()


@pytest.fixture(app)
def login_admin(app):
    app.login(username="admin", password="secret")
    app.logout()