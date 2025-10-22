import allure
from ..pages import main_page
from ..pages.ingredient_details_page import IngredientDetailsPage

@allure.feature("Ингредиенты")
class TestIngredients:

    @allure.title("Открытие окна деталей ингредиента")
    def test_open_ingredient_details(self, driver):
        main = main_page.MainPage(driver)
        main.open_ingredient_details()

        details = IngredientDetailsPage(driver)
        assert details.wait_for_ingredient_details_window()

    @allure.title("Закрытие окна деталей ингредиента")
    def test_close_ingredient_details(self, driver):
        main = main_page.MainPage(driver)
        main.open_ingredient_details()

        details = IngredientDetailsPage(driver)
        details.wait_for_ingredient_details_window()

        details.close_ingredient_details_window()
        assert details.wait_for_window_close()

    @allure.title("Перетаскивание ингредиента увеличивает счётчик")
    def test_drag_and_drop_increases_counter(self, driver):
        main = main_page.MainPage(driver)
        main.click_on_construction()

        initial_count = main.get_ingredient_counter()

        main.drag_ingredient_to_order_area()

        main.wait_for_counter_increase(initial_count)
        new_count = main.get_new_ingredient_counter()

        assert new_count == initial_count + 2