from selenium.webdriver.common.by import By

class IngredientDetailsPageLocators:
    WINDOW_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    BUTTON_CLOSE = (By.XPATH, "//section[contains(@class,'modal')]//button")
