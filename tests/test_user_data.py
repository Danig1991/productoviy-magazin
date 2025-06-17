import pytest

from configurations.user_data import FIRST_NAME, LAST_NAME, MIDDLE_NAME, ADDRESS, CARD_NUMBER, NON_NUMERIC_CARD_NUMBER
from pages.order_confirmation_page import OrderConfirmationPage
from pages.products_page import ProductsPage
from pages.user_data_page import UserDataPage


# вход в роли пользователя, добавлено 2 продукта, переход в корзину, переход для ввода данных пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_us_data_1(authorization, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = authorization

    # Нажать на кнопку "Обратно в магазин".
    UserDataPage(driver).click_button_back_to_shop()

    # Убедиться, что находимся на странице "Продукты".
    title_products = ProductsPage(driver).get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок \"Продукты\" на странице не найден!"
    print("Выполнен корректный переход на страницу \"Продукты\".")


# вход в роли пользователя, добавлено 2 продукта, переход в корзину, переход для ввода данных пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_us_data_2(authorization, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = authorization

    user_data_page = UserDataPage(driver)

    # Заполнить поля: "Имя", "Фамилия", "Отчество", "Адрес доставки", "Номер карты" корректными данными.
    user_data_page.add_first_name(first_name=FIRST_NAME)
    user_data_page.add_last_name(last_name=LAST_NAME)
    user_data_page.add_middle_name(middle_name=MIDDLE_NAME)
    user_data_page.add_address(address=ADDRESS)
    user_data_page.add_card_number(card_number=CARD_NUMBER)

    # Нажать кнопку "Оформить заказ".
    user_data_page.click_button_place_order()

    # Убедиться, что находимся на странице "Оформление заказа: Подтверждение заказа".
    assert "checkoutOverview" in driver.current_url, "Ошибка: Некорректная страница!"

    title_order_confirmation = OrderConfirmationPage(driver).get_title_order_confirmation()
    assert title_order_confirmation == "Оформление заказа: Подтверждение заказа", \
        f"Ошибка: Некорректный заголовок страницы! Актуальный: {title_order_confirmation}."
    print("Корректный переход на страницу для подтверждения заказа.")


# вход в роли пользователя, добавлено 2 продукта, переход в корзину, переход для ввода данных пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_us_data_3(authorization, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = authorization

    user_data_page = UserDataPage(driver)

    # Оставить все поля для заполнения пустыми.
    # Нажать кнопку "Оформить заказ".
    user_data_page.click_button_place_order()

    # Убедиться в наличии сообщения об ошибке.
    assert "checkoutOverview" not in driver.current_url, "Ошибка: Некорректная страница!"

    error_message = user_data_page.get_error_message()
    assert error_message.is_displayed(), "Ошибка: Сообщение об ошибке отсутствует!"
    print("Присутствует сообщение об ошибке, так как поля для заполнения оставлены пустыми.")


# вход в роли пользователя, добавлено 2 продукта, переход в корзину, переход для ввода данных пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_us_data_4(authorization, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = authorization

    user_data_page = UserDataPage(driver)

    # Заполнить все поля корректными данными, кроме поля "Номер карты" - его оставить пустым.
    user_data_page.add_first_name(first_name=FIRST_NAME)
    user_data_page.add_last_name(last_name=LAST_NAME)
    user_data_page.add_middle_name(middle_name=MIDDLE_NAME)
    user_data_page.add_address(address=ADDRESS)

    # Нажать кнопку "Оформить заказ".
    user_data_page.click_button_place_order()

    # Убедиться в наличии сообщения об ошибке.
    assert "checkoutOverview" not in driver.current_url, "Ошибка: Некорректная страница!"

    error_message = user_data_page.get_error_message()
    assert error_message.is_displayed(), "Ошибка: Сообщение об ошибке отсутствует!"

    expected_text = "Введите номер карты"
    assert error_message.text == expected_text, \
        ("Ошибка: Некорректное сообщение об ошибке! "
         f"Получено: \"{error_message.text}\". Ожидалось: \"{expected_text}\".")
    print(f"Присутствует сообщение об ошибке: \"{error_message.text}\", "
          f"так как поле \"Номер карты\" оставлено пустым.")


# вход в роли пользователя, добавлено 2 продукта, переход в корзину, переход для ввода данных пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_us_data_5(authorization, add_two_products, go_to_cart, go_to_checkout_user_data):
    driver = authorization

    user_data_page = UserDataPage(driver)

    # Заполнить все поля корректными данными, кроме поля "Номер карты" - его заполнить нечисловым значением.
    user_data_page.add_first_name(first_name=FIRST_NAME)
    user_data_page.add_last_name(last_name=LAST_NAME)
    user_data_page.add_middle_name(middle_name=MIDDLE_NAME)
    user_data_page.add_address(address=ADDRESS)
    user_data_page.add_card_number(card_number=NON_NUMERIC_CARD_NUMBER)

    # Нажать кнопку "Оформить заказ".
    user_data_page.click_button_place_order()

    # Убедиться в наличии сообщения об ошибке.
    assert "checkoutOverview" not in driver.current_url, "Ошибка: Некорректная страница!"

    error_message = user_data_page.get_error_message()
    assert error_message.is_displayed(), "Ошибка: Сообщение об ошибке отсутствует!"
    print("Присутствует сообщение об ошибке, так как поле \"Номер карты\" заполнено нечисловыми значениями.")
