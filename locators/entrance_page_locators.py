from selenium.webdriver.common.by import By

class EntrancePageLocators:

    # Поле email
    EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')

    # Поле Пароль
    PASSWORD_FIELD = (By.XPATH, '//input[@name="Пароль"]')

    # Кнопка Войти
    ENTRANCE_BUTTON = (By.XPATH, '//button')