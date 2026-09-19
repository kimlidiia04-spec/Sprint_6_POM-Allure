import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.main_page import MainPage, URL, DZEN_URL

ORDER_TEST_DATA = [
    {
        "entry_point": MainPage.ORDER_BUTTON_TOP,
        "name": "Иван",
        "surname": "Петров",
        "address": "Москва, Тверская, 23",
        "metro": "Тверская",
        "phone": "+79161234567",
        "date": "10.09.2026",
        "rental_period": OrderPage.RENTAL_PERIOD_1,
        "color": "black",
        "comment": "Позвонить за 15 минут",
    },
    {
        "entry_point": MainPage.ORDER_BUTTON_BOTTOM,
        "name": "Мария",
        "surname": "Сидорова",
        "address": "Москва, Усачева, 33",
        "metro": "Чеховская",
        "phone": "+79031112233",
        "date": "30.09.2026",
        "rental_period": OrderPage.RENTAL_PERIOD_2,
        "color": "grey",
        "comment": "",
    },
]

@allure.epic("Заказ самоката")
@allure.feature("Позитивный сценарий оформления заказа")
class TestOrder:

    @allure.description("Заполнение формы заказа валидными данными и проверка успешного создания заказа")
    @allure.link("https://qa-scooter.praktikum-services.ru/", name="Сайт Яндекс Самокат")
    @pytest.mark.parametrize("entry_point_name, order_data",
    [("1. Оформление заказа через верхнюю кнопку Заказать", ORDER_TEST_DATA[0]),
     ("2. Оформление заказа через нижнюю кнопку Заказать", ORDER_TEST_DATA[1])])
    
    @allure.title("Оформление заказа: {entry_point_name}")
    def test_positive_order(self, driver, entry_point_name, order_data):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.confirm_cookies()
        main_page.click_order_button(order_data["entry_point"])

        order_page = OrderPage(driver)
        order_page.fill_user_info(order_data["name"], order_data["surname"], order_data["address"], order_data["metro"], order_data["phone"])
        order_page.click_next()

        order_page.fill_order_details(order_data["date"], order_data["comment"])
        order_page.select_rental_period(order_data["rental_period"])
        order_page.select_scooter_color(order_data["color"])
        order_page.click_order()

        order_page.confirm_order()
        assert order_page.is_order_created(), "Должно появиться сообщение об успешном создании заказа"

        order_page.click_view_status()

    @allure.title("Переход на главную по логотипу «Самокат»")
    def test_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.confirm_cookies()
        main_page.click_scooter_logo()
        assert main_page.current_url == URL, "Логотип «Самокат» должен вести на главную страницу"


    @allure.title("Переход в Дзен по логотипу «Яндекса»")
    def test_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.confirm_cookies()
        windows_before = driver.window_handles
        main_page.click_yandex_logo()
        main_page.switch_to_new_window(windows_before)
        assert DZEN_URL in main_page.current_url, "Логотип Яндекса должен открыть главную страницу Дзена"
