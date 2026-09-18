import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

URL = "https://qa-scooter.praktikum-services.ru/"
DZEN_URL = "dzen.ru"


class MainPage(BasePage):

    COOKIES_CONFIRM_BUTTON = (By.ID, "rcc-confirm-button")

    ACCORDION_QUESTION_1 = (By.ID, "accordion__heading-0")
    ACCORDION_ANSWER_1 = (By.ID, "accordion__panel-0")

    ACCORDION_QUESTION_2 = (By.ID, "accordion__heading-1")
    ACCORDION_ANSWER_2 = (By.ID, "accordion__panel-1")

    ACCORDION_QUESTION_3 = (By.ID, "accordion__heading-2")
    ACCORDION_ANSWER_3 = (By.ID, "accordion__panel-2")

    ACCORDION_QUESTION_4 = (By.ID, "accordion__heading-3")
    ACCORDION_ANSWER_4 = (By.ID, "accordion__panel-3")

    ACCORDION_QUESTION_5 = (By.ID, "accordion__heading-4")
    ACCORDION_ANSWER_5 = (By.ID, "accordion__panel-4")

    ACCORDION_QUESTION_6 = (By.ID, "accordion__heading-5")
    ACCORDION_ANSWER_6 = (By.ID, "accordion__panel-5")

    ACCORDION_QUESTION_7 = (By.ID, "accordion__heading-6")
    ACCORDION_ANSWER_7 = (By.ID, "accordion__panel-6")

    ACCORDION_QUESTION_8 = (By.ID, "accordion__heading-7")
    ACCORDION_ANSWER_8 = (By.ID, "accordion__panel-7")

    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, 'div[class*="Header_Nav"] button')
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, 'div[class*="Home_FinishButton"] button')

    SCOOTER_LOGO = (By.CSS_SELECTOR, '.Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CSS_SELECTOR, '.Header_LogoYandex__3TSOI')

    @allure.step("Принять cookies")
    def confirm_cookies(self):
        self.click(self.COOKIES_CONFIRM_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(self.COOKIES_CONFIRM_BUTTON))

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(URL)

    @allure.step("Открыть вопрос FAQ")
    def open_faq_answer(self, accordion_question):
        self.click(accordion_question)

    @allure.step("Получить текст ответа FAQ")
    def get_faq_answer_text(self, accordion_answer):
        return self.get_text(accordion_answer)

    @allure.step("Нажать кнопку «Заказать»")
    def click_order_button(self, order_button):
        self.click(order_button)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)