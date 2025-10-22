import allure
from ..locators.ingredient_details_locators import IngredientDetailsPageLocators
from ..pages.base_page import BasePage
from ..locators.order_list_locators import OrderListLocators
from ..locators import main_page_locators


class OrderListPage(BasePage):

    @allure.step("Подождать загрузки раздела Лента заказов")
    def wait_for_window_ingredient_details(self):
        self.wait_for_element(IngredientDetailsPageLocators.WINDOW_DETAILS)

    @allure.step("Получаем значение счётчика 'Выполнено за всё время'")
    def get_total_orders(self):
        return int(self.get_text(OrderListLocators.COUNTER_TOTAL))

    @allure.step("Получаем значение счётчика 'Выполнено за сегодня'")
    def get_today_orders(self):
        return int(self.get_text(OrderListLocators.COUNTER_TODAY))

    @allure.step("Получаем список номеров заказов 'В работе'")
    def get_orders_in_progress(self):
        elements = self.find_elements(OrderListLocators.ORDERS_IN_PROGRESS_ITEMS)
        return [el.text for el in elements]

    @allure.step("Проверяем, что заказ с номером {order_number} появился в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        orders = self.get_orders_in_progress()
        return order_number in orders

    @allure.step("Кликнуть на конструктор")
    def click_on_construction(self):
        self.click_on_element(main_page_locators.MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step("Проверяем, что лента заказов отображается")
    def is_feed_visible(self):
        element = self.wait_for_element(OrderListLocators.TITLE_ORDER_LIST)
        return element.is_displayed()