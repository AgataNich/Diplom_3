from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка "Войти в аккаунт"
    ENTRANCE_ON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка "Конструктор"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")

    # Кнопка "Лента заказов"
    BUTTON_ORDER_LIST = (By.XPATH, "//p[text()='Лента Заказов']")

    # Ингредиент "Флюоресцентная булка R2-D3"
    INGREDIENT_BUN_FLU = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")

    # Счётчик ингредиента
    INGREDIENT_COUNTER_BUN_FLU = (By.XPATH, "//p[contains(@class,'counter_counter__num__3nue1')]")

    # Зона заказа
    ORDER_AREA = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket__list__l9dp_')]")

    # Кнопка "Оформить заказ"
    button_arrange_order = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

    # Номер заказа
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title__2L34m')]")




