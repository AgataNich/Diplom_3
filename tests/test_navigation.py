import allure
from ..pages.main_page import MainPage
from ..pages.order_list_page import OrderListPage


@allure.feature("Навигация по сайту")
class TestNavigation:

    @allure.title("Переход на 'Конструктор'")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_construction()
        assert main_page.is_constructor_visible()

    @allure.title("Переход на 'Ленту заказов'")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_button_order_list()

        order_feed = OrderListPage(driver)
        assert order_feed.is_feed_visible()
