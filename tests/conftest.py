import pytest
from selenium import webdriver
from ..curl import *
from ..helper import *
from ..pages.entrance_page import EntrancePage
from ..pages.main_page import MainPage
from ..pages.base_page import BasePage
import requests


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        driver_instance = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver_instance = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    base_page = BasePage(driver_instance)
    base_page.maximize_window()
    base_page.open(main_site)

    yield driver_instance

    base_page.quit_browser()


@pytest.fixture
def create_new_user():
    email, password, name = generate_registration_data()
    payload_data = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(create_user, json=payload_data)
    response_data = response.json()

    response_data["email"] = email
    response_data["password"] = password

    return response_data


@pytest.fixture
def login_existing_user(driver, create_new_user):
    login_page = EntrancePage(driver)
    login_page.open_login_page()
    login_page.login(create_new_user["email"], create_new_user["password"])
    return driver


