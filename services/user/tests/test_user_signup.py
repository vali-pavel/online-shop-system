from pytest_bdd import given, when, then, scenario, parsers

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest

browser = None


@pytest.fixture(scope="function")
def init_driver():
    global browser
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-web-security")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.delete_all_cookies()
    browser.get("http://localhost:3000/signup")

    yield
    browser.quit()


@scenario(
    "../features/user.feature",
    "The system can create a user",
)
def test_user_creation():
    pass


@given(parsers.parse("email {email}"))
def email(init_driver, email):
    element = browser.find_element(by=By.NAME, value="email")
    element.send_keys(email)
    assert isinstance(email, str)


@given(parsers.parse("password {password}"))
def password(password):
    element = browser.find_element(by=By.NAME, value="password")
    element.send_keys(password)
    assert isinstance(password, str)


@given(parsers.parse("full name {full_name}"))
def full_name(full_name):
    element = browser.find_element(by=By.NAME, value="full_name")
    element.send_keys(full_name)
    assert isinstance(full_name, str)


@given(parsers.parse("phone number {phone_number}"))
def phone_number(phone_number):
    element = browser.find_element(by=By.NAME, value="phone_number")
    element.send_keys(phone_number)
    assert isinstance(int(phone_number), int)


@when("creating a new user with the above details")
def submit_user():
    element = browser.find_element(by=By.XPATH, value="//button[@type='submit']")
    element.click()


@then(parsers.parse("fields validation {result}"))
def fields_validation(result):
    element = browser.find_element(by=By.NAME, value="email")
    element_attribute = element.get_attribute("validationMessage")
    if element_attribute:
        assert result == "fails"
    else:
        assert result == "succeeds"
