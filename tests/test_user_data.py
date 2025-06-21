import logging

from pages.order_confirmation_page import OrderConfirmationPage
from pages.products_page import ProductsPage
from pages.user_data_page import UserDataPage
from utils.config import UserData
from utils.double import Double


def test_us_data_1(shopper_auth, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = shopper_auth
    logging.info("Вход в роли пользователя, добавлено 2 продукта, "
                 "переход в корзину, переход для ввода данных пользователя")

    user_data_page = UserDataPage(driver)
    products_page = ProductsPage(driver)

    logging.info("Нажать на кнопку \"Обратно в магазин\".")
    user_data_page.click_button_back_to_shop()

    logging.info("Убедиться, что находимся на странице \"Продукты\".")
    title_products = products_page.get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок \"Продукты\" на странице не найден!"
    Double.print_and_log("Выполнен корректный переход на страницу \"Продукты\".")


def test_us_data_2(shopper_auth, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = shopper_auth
    logging.info("Вход в роли пользователя, добавлено 2 продукта, "
                 "переход в корзину, переход для ввода данных пользователя")

    user_data_page = UserDataPage(driver)
    order_confirmation_page = OrderConfirmationPage(driver)
    user_data = UserData()
    first_name = user_data.get_first_name()
    last_name = user_data.get_last_name()
    middle_name = user_data.get_middle_name()
    address = user_data.get_address()
    card_number = user_data.get_card_number()

    logging.info("Заполнить поля: \"Имя\", \"Фамилия\", \"Отчество\", \"Адрес доставки\", \"Номер карты\" "
                 "корректными данными.")
    user_data_page.add_first_name(first_name)
    user_data_page.add_last_name(last_name)
    user_data_page.add_middle_name(middle_name)
    user_data_page.add_address(address)
    user_data_page.add_card_number(card_number)

    logging.info("Нажать кнопку \"Оформить заказ\".")
    user_data_page.click_button_place_order()

    logging.info("Убедиться, что находимся на странице \"Оформление заказа: Подтверждение заказа\".")
    assert "checkoutOverview" in driver.current_url, "Ошибка: Некорректная страница!"

    title_order_confirmation = order_confirmation_page.get_title_order_confirmation()
    assert title_order_confirmation == "Оформление заказа: Подтверждение заказа", \
        f"Ошибка: Некорректный заголовок страницы! Актуальный: {title_order_confirmation}."
    Double.print_and_log("Корректный переход на страницу для подтверждения заказа.")


def test_us_data_3(shopper_auth, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = shopper_auth
    logging.info("Вход в роли пользователя, добавлено 2 продукта, "
                 "переход в корзину, переход для ввода данных пользователя")

    user_data_page = UserDataPage(driver)

    logging.info("Оставить все поля для заполнения пустыми.")
    logging.info("Нажать кнопку \"Оформить заказ\".")
    user_data_page.click_button_place_order()

    logging.info("Убедиться в наличии сообщения об ошибке.")
    assert "checkoutOverview" not in driver.current_url, "Ошибка: Некорректная страница!"

    error_message = user_data_page.get_error_message()
    assert error_message.is_displayed(), "Ошибка: Сообщение об ошибке отсутствует!"
    Double.print_and_log("Присутствует сообщение об ошибке, так как поля для заполнения оставлены пустыми.")


def test_us_data_4(shopper_auth, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = shopper_auth
    logging.info("Вход в роли пользователя, добавлено 2 продукта, "
                 "переход в корзину, переход для ввода данных пользователя")

    user_data_page = UserDataPage(driver)
    user_data = UserData()
    first_name = user_data.get_first_name()
    last_name = user_data.get_last_name()
    middle_name = user_data.get_middle_name()
    address = user_data.get_address()

    logging.info("Заполнить все поля корректными данными, кроме поля "
                 "\"Номер карты\" - его оставить пустым.")
    user_data_page.add_first_name(first_name)
    user_data_page.add_last_name(last_name)
    user_data_page.add_middle_name(middle_name)
    user_data_page.add_address(address)

    logging.info("Нажать кнопку \"Оформить заказ\".")
    user_data_page.click_button_place_order()

    logging.info("Убедиться в наличии сообщения об ошибке.")
    assert "checkoutOverview" not in driver.current_url, "Ошибка: Некорректная страница!"

    error_message = user_data_page.get_error_message()
    assert error_message.is_displayed(), "Ошибка: Сообщение об ошибке отсутствует!"

    expected_text = "Введите номер карты"
    assert error_message.text == expected_text, \
        ("Ошибка: Некорректное сообщение об ошибке! "
         f"Получено: \"{error_message.text}\". Ожидалось: \"{expected_text}\".")
    Double.print_and_log(f"Присутствует сообщение об ошибке: \"{error_message.text}\", "
                         f"так как поле \"Номер карты\" оставлено пустым.")


def test_us_data_5(shopper_auth, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = shopper_auth
    logging.info("Вход в роли пользователя, добавлено 2 продукта, "
                 "переход в корзину, переход для ввода данных пользователя")

    user_data_page = UserDataPage(driver)
    user_data = UserData()
    first_name = user_data.get_first_name()
    last_name = user_data.get_last_name()
    middle_name = user_data.get_middle_name()
    address = user_data.get_address()
    non_numeric_card_number = user_data.get_non_numeric_card_number()

    logging.info("Заполнить все поля корректными данными, кроме поля "
                 "\"Номер карты\" - его заполнить нечисловым значением.")
    user_data_page.add_first_name(first_name)
    user_data_page.add_last_name(last_name)
    user_data_page.add_middle_name(middle_name)
    user_data_page.add_address(address)
    user_data_page.add_card_number(non_numeric_card_number)

    logging.info("Нажать кнопку \"Оформить заказ\".")
    user_data_page.click_button_place_order()

    logging.info("Убедиться в наличии сообщения об ошибке.")
    assert "checkoutOverview" not in driver.current_url, "Ошибка: Некорректная страница!"

    error_message = user_data_page.get_error_message()
    assert error_message.is_displayed(), "Ошибка: Сообщение об ошибке отсутствует!"
    Double.print_and_log(
        "Присутствует сообщение об ошибке, так как поле \"Номер карты\" заполнено нечисловыми значениями.")
