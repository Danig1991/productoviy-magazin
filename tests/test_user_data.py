import logging

import allure

from pages.order_confirmation_page import OrderConfirmationPage
from pages.products_page import ProductsPage
from pages.user_data_page import UserDataPage
from utils.config import UserData


@allure.epic("Тест страницы 'Оформление заказа: Данные пользователя'.")
@allure.title("Кнопка 'Обратно в магазин' служит для перевода на страницу выбора продуктов.")
def test_us_data_1(shopper_auth, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = shopper_auth

    # Нажать на кнопку 'Обратно в магазин'.
    UserDataPage(driver).click_button_back_to_shop()

    logging.info("Убедиться, что находимся на странице 'Продукты'.")
    title_products = ProductsPage(driver).get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок 'Продукты' на странице не найден!"
    logging.info("Выполнен корректный переход на страницу 'Продукты'.")


@allure.epic("Тест страницы 'Оформление заказа: Данные пользователя'.")
@allure.title("Заполнение полей для оформления заказа корректными данными.")
def test_us_data_2(shopper_auth, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = shopper_auth
    user_data = UserData().get_user_data()

    logging.info("Заполнить поля: 'Имя', 'Фамилия', 'Отчество', 'Адрес доставки', 'Номер карты' "
                 "корректными данными.")
    UserDataPage(driver).add_user_data(
        first_name=user_data["Имя"],
        last_name=user_data["Фамилия"],
        middle_name=user_data["Отчество"],
        address=user_data["Адрес доставки"],
        card_number=user_data["Номер карты"]
    )

    # Нажать кнопку 'Оформить заказ'.
    UserDataPage(driver).click_button_place_order()

    logging.info("Убедиться, что находимся на странице 'Оформление заказа: Подтверждение заказа'.")
    assert "checkoutOverview" in driver.current_url, "Ошибка: Некорректная страница!"

    title_order_confirmation = OrderConfirmationPage(driver).get_title_order_confirmation()
    assert title_order_confirmation == "Оформление заказа: Подтверждение заказа", \
        f"Ошибка: Некорректный заголовок страницы! Актуальный: {title_order_confirmation}."
    logging.info("Корректный переход на страницу для подтверждения заказа.")


@allure.epic("Тест страницы 'Оформление заказа: Данные пользователя'.")
@allure.title("Проверка оформления заказа со всеми пустыми полями.")
def test_us_data_3(shopper_auth, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = shopper_auth

    logging.info("Оставить все поля для заполнения пустыми.")
    # Нажать кнопку 'Оформить заказ'.
    UserDataPage(driver).click_button_place_order()

    logging.info("Убедиться в наличии сообщения об ошибке.")
    assert "checkoutOverview" not in driver.current_url, "Ошибка: Некорректная страница!"

    error_message = UserDataPage(driver).get_error_message()
    assert error_message.is_displayed(), "Ошибка: Сообщение об ошибке отсутствует!"
    logging.info("Присутствует сообщение об ошибке, так как поля для заполнения оставлены пустыми.")


@allure.epic("Тест страницы 'Оформление заказа: Данные пользователя'.")
@allure.title("Проверка оформления заказа с пустым полем номера карты.")
def test_us_data_4(shopper_auth, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = shopper_auth
    user_data = UserData().get_user_data()

    logging.info("Заполнить все поля корректными данными, кроме поля "
                 "'Номер карты' - его оставить пустым.")
    UserDataPage(driver).add_user_data(
        first_name=user_data["Имя"],
        last_name=user_data["Фамилия"],
        middle_name=user_data["Отчество"],
        address=user_data["Адрес доставки"]
    )
    # Нажать кнопку 'Оформить заказ'.
    UserDataPage(driver).click_button_place_order()

    logging.info("Убедиться в наличии сообщения об ошибке.")
    assert "checkoutOverview" not in driver.current_url, "Ошибка: Некорректная страница!"

    error_message = UserDataPage(driver).get_error_message()
    assert error_message.is_displayed(), "Ошибка: Сообщение об ошибке отсутствует!"

    expected_text = "Введите номер карты"
    assert error_message.text == expected_text, \
        ("Ошибка: Некорректное сообщение об ошибке! "
         f"Получено: '{error_message.text}'. Ожидалось: '{expected_text}'.")
    logging.info(f"Присутствует сообщение об ошибке: '{error_message.text}', "
                 f"так как поле 'Номер карты' оставлено пустым.")


@allure.epic("Тест страницы 'Оформление заказа: Данные пользователя'.")
@allure.title("Проверка оформления заказа. Ввод в поле номера карты нечислового значения.")
def test_us_data_5(shopper_auth, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = shopper_auth
    user_data = UserData().get_user_data()

    logging.info("Заполнить все поля корректными данными, кроме поля "
                 "'Номер карты' - его заполнить нечисловым значением.")
    UserDataPage(driver).add_user_data(
        first_name=user_data["Имя"],
        last_name=user_data["Фамилия"],
        middle_name=user_data["Отчество"],
        address=user_data["Адрес доставки"],
        card_number=user_data["Нечисловой номер карты"]
    )
    # Нажать кнопку 'Оформить заказ'.
    UserDataPage(driver).click_button_place_order()

    logging.info("Убедиться в наличии сообщения об ошибке.")
    assert "checkoutOverview" not in driver.current_url, "Ошибка: Некорректная страница! Выполнен переход."

    error_message = UserDataPage(driver).get_error_message()
    assert error_message.is_displayed(), "Ошибка: Сообщение об ошибке отсутствует!"
    logging.info(
        "Присутствует сообщение об ошибке, так как поле 'Номер карты' заполнено нечисловыми значениями.")
