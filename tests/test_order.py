import allure
import pytest
from ..pages import main_page, order_list_page
from ..curl import *


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается после создания заказа")
    def test_total_orders_increases(self, driver, login_existing_user):

        with allure.step("Авторизуемся"):
            driver = login_existing_user

        with allure.step("Получаем значение счётчика 'Выполнено за всё время' до создания заказа"):
            feed_page = order_list_page.OrderListPage(driver)
            feed_page.open(order_list)
            initial_total = feed_page.get_total_orders()

        with allure.step("Создаём новый заказ"):
            main = main_page.MainPage(driver)
            main.click_on_construction()
            initial_count = main.get_ingredient_counter()
            main.drag_ingredient_to_order_area()
            main.wait_for_counter_increase(initial_count)
            main.click_on_button_arrange_order()
            order_number = main.get_order_number()

        with allure.step("Обновляем страницу и повторно открываем ленту заказов"):
            feed_page.refresh_page()
            feed_page.open(order_list)

        with allure.step("Получаем значение счётчика 'Выполнено за всё время' после создания заказа"):
            new_total = feed_page.get_total_orders()

        with allure.step("Проверяем, что значение увеличилось"):
            assert new_total > initial_total
            assert order_number == new_total

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается после создания заказа")
    def test_today_orders_increases(self, driver, login_existing_user):
        with allure.step("Авторизуемся"):
            driver = login_existing_user

        feed_page = order_list_page.OrderListPage(driver)
        feed_page.open(order_list)

        with allure.step("Получаем значение счётчика 'Выполнено за сегодня' до создания заказа"):
            initial_today = feed_page.get_today_orders()

        with allure.step("Создаём новый заказ"):
            main = main_page.MainPage(driver)
            main.click_on_construction()
            initial_count = main.get_ingredient_counter()
            main.drag_ingredient_to_order_area()
            main.wait_for_counter_increase(initial_count)
            main.click_on_button_arrange_order()
            main.get_order_number()

        with allure.step("Обновляем страницу и повторно открываем ленту заказов"):
            feed_page.refresh_page()
            feed_page.open(order_list)

        with allure.step("Получаем значение счётчика 'Выполнено за сегодня' после создания заказа"):
            new_today = feed_page.get_today_orders()

        with allure.step("Проверяем, что значение увеличилось"):
            assert new_today > initial_today

    @allure.title("Номер нового заказа появляется в разделе 'В работе'")
    def test_order_appears_in_progress(self, driver, login_existing_user):
        with allure.step("Авторизуемся"):
            driver = login_existing_user

        feed_page = order_list_page.OrderListPage(driver)
        feed_page.open(order_list)

        with allure.step("Создаём новый заказ"):
            main = main_page.MainPage(driver)
            main.click_on_construction()
            initial_count = main.get_ingredient_counter()
            main.drag_ingredient_to_order_area()
            main.wait_for_counter_increase(initial_count)
            main.click_on_button_arrange_order()
            order_number = main.get_order_number()

        with allure.step("Обновляем страницу и повторно открываем ленту заказов"):
            feed_page.refresh_page()
            feed_page.open(order_list)

        with allure.step("Проверяем, что номер заказа появился в разделе 'В работе'"):
            assert feed_page.is_order_in_progress(order_number)
