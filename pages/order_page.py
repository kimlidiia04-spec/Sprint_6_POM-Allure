import allure

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderPage(BasePage):

    NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    SURNAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    METRO_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
    METRO_OPTION = (By.XPATH, '//*[normalize-space()="{}"]')
    PHONE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')

    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    DELIVERY_DATE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')

    RENTAL_PERIOD = (By.XPATH, '//div[text()="* Срок аренды"]')
    RENTAL_PERIOD_1 = (By.XPATH, '//div[text()="сутки"]')
    RENTAL_PERIOD_2 = (By.XPATH, '//div[text()="двое суток"]')
    RENTAL_PERIOD_3 = (By.XPATH, '//div[text()="трое суток"]')
    RENTAL_PERIOD_4 = (By.XPATH, '//div[text()="четверо суток"]')
    RENTAL_PERIOD_5 = (By.XPATH, '//div[text()="пятеро суток"]')
    RENTAL_PERIOD_6 = (By.XPATH, '//div[text()="шестеро суток"]')
    RENTAL_PERIOD_7 = (By.XPATH, '//div[text()="семеро суток"]')

    BLACK_SCOOTER_CHECKBOX = (By.ID, "black")
    GREY_SCOOTER_CHECKBOX = (By.ID, "grey")

    COMMENT_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')

    ORDER_BUTTON = (By.XPATH, '(//button[text()="Заказать"])[2]')
    CONFIRM_ORDER_BUTTON = (By.XPATH, '//button[text()="Да"]')
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(text(), "Заказ оформлен")]')
    VIEW_STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')

    @allure.step("Заполнить данные пользователя")
    def fill_user_info(self, name, surname, address, metro, phone):
        self.type_text(self.NAME_INPUT, name)
        self.type_text(self.SURNAME_INPUT, surname)
        self.type_text(self.ADDRESS_INPUT, address)
        self.type_text(self.METRO_INPUT, metro)
        self.select_metro_station(metro)
        self.type_text(self.PHONE_INPUT, phone)

    
    def get_metro_option_locator(self, metro_station):
        return (By.XPATH, self.METRO_OPTION[1].format(metro_station))

    @allure.step("Выбрать станцию метро")
    def select_metro_station(self, metro_station):
        self.click(self.get_metro_option_locator(metro_station))

    @allure.step("Перейти к следующему шагу оформления заказа")
    def click_next(self):
        self.click(self.NEXT_BUTTON)

    @allure.step("Заполнить данные заказа")
    def fill_order_details(self, delivery_date, comment):
        self.select_delivery_date(delivery_date)
        self.type_text(self.COMMENT_INPUT, comment)

    @allure.step("Выбрать дату доставки")
    def select_delivery_date(self, delivery_date):
        self.click(self.DELIVERY_DATE_INPUT)
        day = delivery_date.split(".")[0]
        date_option = (By.XPATH, f'//div[contains(@class, "react-datepicker__day") and normalize-space()="{day}"]')
        self.click(date_option)

    @allure.step("Выбрать срок аренды")
    def select_rental_period(self, rental_period):
        self.click(self.RENTAL_PERIOD)
        self.click(rental_period)

    @allure.step("Выбрать цвет самоката")
    def select_scooter_color(self, color):
        color_locator = self.BLACK_SCOOTER_CHECKBOX if color == "black" else self.GREY_SCOOTER_CHECKBOX
        self.click(color_locator)

    @allure.step("Нажать кнопку «Заказать»")
    def click_order(self):
        self.click(self.ORDER_BUTTON)

    @allure.step("Подтвердить создание заказа")
    def confirm_order(self):
        self.click(self.CONFIRM_ORDER_BUTTON)

    @allure.step("Проверить сообщение об успешном создании заказа")
    def is_order_created(self):
        return self.wait_visible(self.SUCCESS_MESSAGE) is not None

    @allure.step("Нажать «Посмотреть статус»")
    def click_view_status(self):
        self.click(self.VIEW_STATUS_BUTTON)