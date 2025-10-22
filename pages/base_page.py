import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..data import global_timeout



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    @allure.step("Развернуть окно браузера")
    def maximize_window(self):
        self.driver.maximize_window()

    @allure.step("Закрыть браузер")
    def quit_browser(self):
        self.driver.quit()

    @allure.step("Обновить текущую страницу")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Обновить текущую страницу")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=global_timeout):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Поиск элементов {locator}")
    def find_elements(self, locator):
        self.driver.find_elements(*locator)

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        element = self.wait_for_element(locator, global_timeout)
        element.click()

    @allure.step("Получаем текст элемента: {locator}")
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step('Подождать пока элемент не станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Открываем страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Получаем список элементов: {locator}")
    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Открываем страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ввод данных")
    def send_keys(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

