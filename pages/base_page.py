import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)
        return self

    @allure.step("Дождаться элемента и кликнуть по нему")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Кликнуть по уже найденному элементу")
    def click_element(self, element):
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        element = self.wait_visible(locator)
        return element.text

    @allure.step('Ввести текст "{text}" в поле')
    def type_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Проверить отображение элемента")
    def is_displayed(self, locator):
        return self.wait_visible(locator).is_displayed()

    @property
    def current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на новую вкладку")
    @allure.link("https://dzen.ru/", name="Дзен")
    def switch_to_new_window(self, windows_before):
        self.wait.until(lambda d: len(d.window_handles) > len(windows_before))
        new_window = [w for w in self.driver.window_handles if w not in windows_before][0]
        self.driver.switch_to.window(new_window)
        self.wait.until(lambda d: "dzen.ru" in d.current_url)
