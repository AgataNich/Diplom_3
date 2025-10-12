import allure
from ..pages.base_page import BasePage
from ..locators.entrance_page_locators import EntrancePageLocators
from ..curl import *

class EntrancePage(BasePage):

    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        self.open(login_user)

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.wait_for_element(EntrancePageLocators.EMAIL_FIELD)
        self.send_keys(EntrancePageLocators.EMAIL_FIELD, email)

    @allure.step("Ввести пароль")
    def enter_password(self,  password):
        self.wait_for_element(EntrancePageLocators.PASSWORD_FIELD)
        self.send_keys(EntrancePageLocators.PASSWORD_FIELD, password)

    @allure.step("Кликнуть на Войти в аккаунт")
    def click_login_button(self):
        self.click_on_element(EntrancePageLocators.ENTRANCE_BUTTON)

    @allure.step("Авторизоваться под пользователем")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

