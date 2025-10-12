from selenium.webdriver.common.by import By

class OrderListLocators:
    TITLE_ORDER_LIST = (By.XPATH, "//h1[text()='Лента заказов']")
    COUNTER_TOTAL = (By.XPATH, '//div[@id="root"]//ul/following::div/div[2]/p[2]')
    COUNTER_TODAY = (By.XPATH, '//div[@id="root"]//ul/following::div/div[3]/p[2]')
    ORDERS_IN_PROGRESS_ITEMS = (By.XPATH, '//div[@id="root"]//main/div/div/div/div[1]/ul[2]/li')

