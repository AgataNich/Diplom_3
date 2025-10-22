import allure
from ..pages.base_page import BasePage
from ..locators.ingredient_details_locators import IngredientDetailsPageLocators


class IngredientDetailsPage(BasePage):
    locators = IngredientDetailsPageLocators

    @allure.step("Ожидание появления окна деталей ингредиента")
    def wait_for_ingredient_details_window(self):
        return self.wait_for_element(self.locators.WINDOW_DETAILS)

    @allure.step("Закрыть окно деталей ингредиента")
    def close_ingredient_details_window(self):
        return self.click_on_element(self.locators.BUTTON_CLOSE)

    @allure.step("Проверка, что окно деталей ингредиента закрылось")
    def wait_for_window_close(self):
        return self.wait_for_element_hide(self.locators.WINDOW_DETAILS)
