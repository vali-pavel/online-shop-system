from pytest_bdd import given, when, then, scenario, parsers

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
import time

browser = None


@pytest.fixture(scope="function")
def init_driver():
    global browser
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-web-security")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.delete_all_cookies()
    browser.get("http://localhost:3000/login")

    yield
    browser.quit()


@scenario(
    "../features/user.feature",
    "A user can Login",
)
def test_user_creation():
    pass


@given(parsers.parse("a user with email {email}"))
def email(init_driver, email):
    element = browser.find_element(by=By.NAME, value="email")
    element.send_keys(email)
    assert isinstance(email, str)


@given(parsers.parse("a password {password}"))
def password(password):
    element = browser.find_element(by=By.NAME, value="password")
    element.send_keys(password)
    assert isinstance(password, str)


@when("the login button is clicked")
def submit_login():
    element = browser.find_element(by=By.XPATH, value="//button[@type='submit']")
    element.click()


@then(parsers.parse("I should be redirected to the {path_location} page"))
def page_redirect(path_location):
    time.sleep(1)
    assert path_location in browser.current_url
