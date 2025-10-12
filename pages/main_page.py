import allure
from selenium.webdriver import ActionChains
from ..pages.base_page import BasePage
from ..locators import main_page_locators

class MainPage(BasePage):

    @allure.step("Кликнуть на Войти в аккаунт")
    def click_on_entrance(self):
        self.click_on_element(main_page_locators.MainPageLocators.ENTRANCE_ON_MAIN)

    @allure.step("Кликнуть на конструктор")
    def click_on_construction(self):
        self.click_on_element(main_page_locators.MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step("Получить текущее значение счётчика ингредиента")
    def get_ingredient_counter(self):
        counter_elem = self.wait_for_element(main_page_locators.MainPageLocators.INGREDIENT_COUNTER_BUN_FLU)
        return int(counter_elem.text) if counter_elem.text.isdigit() else 0

    @allure.step("Перетащить ингредиент в зону заказа")
    def drag_ingredient_to_order_area(self):
        ingredient_elem = self.wait_for_element(main_page_locators.MainPageLocators.INGREDIENT_BUN_FLU)
        order_area_elem = self.wait_for_element(main_page_locators.MainPageLocators.ORDER_AREA)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient_elem, order_area_elem).perform()

    @allure.step("Дождаться увеличения счётчика ингредиента")
    def wait_for_counter_increase(self, initial_count):
        self.wait.until(
            lambda d: self.get_ingredient_counter() != initial_count
        )

    @allure.step("Получить новое значение счётчика ингредиента")
    def get_new_ingredient_counter(self):
        return self.get_ingredient_counter()

    @allure.step("Переход в Ленту заказов")
    def click_on_button_order_list(self):
        self.click_on_element(main_page_locators.MainPageLocators.BUTTON_ORDER_LIST)

    @allure.step("Клик по ингредиенту для открытия деталей")
    def open_ingredient_details(self):
        self.click_on_element(main_page_locators.MainPageLocators.INGREDIENT_BUN_FLU)

    @allure.step("Клик на Оформить заказ")
    def click_on_button_arrange_order(self):
        self.click_on_element(main_page_locators.MainPageLocators.button_arrange_order)

    @allure.step("Получить значения номера заказа")
    def get_order_number(self):
        self.get_text(main_page_locators.MainPageLocators.ORDER_NUMBER)

    @allure.step("Подождать видимости элемента")
    def wait_for_element_bun_flu(self):
        self.wait_for_element(main_page_locators.MainPageLocators.INGREDIENT_BUN_FLU)

    @allure.step("Проверяем, что страница конструктора видна")
    def is_constructor_visible(self):
        element = self.wait_for_element(main_page_locators.MainPageLocators.INGREDIENT_BUN_FLU)
        return element.is_displayed()

