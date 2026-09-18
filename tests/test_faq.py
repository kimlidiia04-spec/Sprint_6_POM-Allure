import allure
import pytest

from pages.main_page import MainPage

@allure.epic("Главная страница")
@allure.feature("Находим раздел «Вопросы о важном»")
@pytest.mark.parametrize("question_name, question_locator, answer_locator, expected_answer",
    [("1. Стоимость аренды", MainPage.ACCORDION_QUESTION_1, MainPage.ACCORDION_ANSWER_1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
     ("2. Несколько самокатов", MainPage.ACCORDION_QUESTION_2, MainPage.ACCORDION_ANSWER_2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
     ("3. Время аренды", MainPage.ACCORDION_QUESTION_3, MainPage.ACCORDION_ANSWER_3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
     ("4. Доставка сегодня", MainPage.ACCORDION_QUESTION_4, MainPage.ACCORDION_ANSWER_4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
     ("5. Отмена заказа", MainPage.ACCORDION_QUESTION_5, MainPage.ACCORDION_ANSWER_5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
     ("6. Зарядка самоката", MainPage.ACCORDION_QUESTION_6, MainPage.ACCORDION_ANSWER_6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
     ("7. Отмена после доставки", MainPage.ACCORDION_QUESTION_7, MainPage.ACCORDION_ANSWER_7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
     ("8. Доставка в область", MainPage.ACCORDION_QUESTION_8, MainPage.ACCORDION_ANSWER_8, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")])

def test_faq_answers(driver, question_name, question_locator, answer_locator, expected_answer):
    allure.dynamic.title(f"Проверка соответствия вопроса и ответа: {question_name}")
    main_page = MainPage(driver)

    main_page.open_main_page()
    main_page.confirm_cookies()
    main_page.open_faq_answer(question_locator)

    actual_answer = main_page.get_faq_answer_text(answer_locator)

    assert actual_answer == expected_answer, "Текст ответа FAQ не соответствует ожидаемому"