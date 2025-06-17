import pytest

from configurations.action_with_product import PRODUCT_NAME, QUANTITY_2
from configurations.user_data import FIRST_NAME, LAST_NAME, MIDDLE_NAME, ADDRESS, CARD_NUMBER
from pages.checkout_complete_page import CheckoutCompletePage
from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.order_confirmation_page import OrderConfirmationPage
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.user_data_page import UserDataPage


# вход в роли пользователя, добавлено 2 продукта, переход в корзину
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_order_1(authorization, add_two_products, go_to_cart):
    driver = authorization

    shopping_cart_page = ShoppingCartPage(driver)
    user_data_page = UserDataPage(driver)
    order_confirmation_page = OrderConfirmationPage(driver)

    # Зафиксировать итоговую сумму.
    expected_total_sum = shopping_cart_page.get_total_sum()

    # Нажать кнопку "Оформить заказ".
    shopping_cart_page.click_button_place_order()

    # Заполнение полей корректными данными.
    expected_first_name = user_data_page.add_first_name(first_name=FIRST_NAME)
    expected_last_name = user_data_page.add_last_name(last_name=LAST_NAME)
    expected_middle_name = user_data_page.add_middle_name(middle_name=MIDDLE_NAME)
    expected_address = user_data_page.add_address(address=ADDRESS)
    expected_card_number = user_data_page.add_card_number(card_number=CARD_NUMBER)

    # Нажать кнопку "Оформить заказ".
    user_data_page.click_button_place_order()

    # Сравнить ранее зафиксированные данные с данными на странице "Оформление заказа: Подтверждение заказа".
    expected_data = {
        "Имя": expected_first_name,
        "Фамилия": expected_last_name,
        "Отчество": expected_middle_name,
        "Адрес доставки": expected_address,
        "Номер карты": expected_card_number,
        "Итоговая стоимость": expected_total_sum
    }
    current_data = order_confirmation_page.get_order_confirmation_data()

    for key in expected_data:
        assert current_data[key] == expected_data[key], (
            f"Ошибка: В поле \"{key}\" значение: \"{current_data[key]}\". "
            f"Ожидаемое: \"{expected_data[key]}\""
        )
    print("Итоговая сумма и данные для подтверждения заказа передаются корректно.")


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_order_2(authorization):
    driver = authorization

    products_page = ProductsPage(driver)
    fixed_panel_icons = FixedPanelIcons(driver)
    shopping_cart_page = ShoppingCartPage(driver)
    user_data_page = UserDataPage(driver)
    order_confirmation_page = OrderConfirmationPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

    # Убедиться, что находимся на странице "Продукты".
    title_products = products_page.get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок \"Продукты\" на странице не найден!"
    print("Выполнен переход на страницу \"Продукты\".")

    # Добавить один продукт в количестве 2 шт.
    products_page.set_product_quantity(product_name=PRODUCT_NAME, target_quantity=QUANTITY_2)

    # Перейти на страницу "Корзинка" (нажать на иконку корзины).
    fixed_panel_icons.click_shopping_cart()

    # Убедиться, что находимся на странице "Корзинка".
    assert "cart" in driver.current_url, "Ошибка: Некорректная страница!"

    title_shopping_cart = shopping_cart_page.get_title_shopping_cart()
    assert title_shopping_cart == "Корзинка", \
        "Ошибка: Заголовок \"Корзинка\" на странице не найден!"
    print("Выполнен переход на страницу \"Корзинка\".")

    # Нажать кнопку "Оформить заказ".
    shopping_cart_page.click_button_place_order()

    # Убедиться, что находимся на странице "Оформление заказа: Данные пользователя".
    assert "checkout" in driver.current_url, "Ошибка: Некорректная страница!"

    title_user_data = user_data_page.get_title_user_data()
    assert title_user_data == "Оформление заказа: Данные пользователя", \
        f"Ошибка: Некорректный заголовок страницы! Актуальный: {title_user_data}."
    print("Корректный переход на страницу для заполнения данных о пользователе.")

    # Заполнение полей корректными данными.
    user_data_page.add_first_name(first_name=FIRST_NAME)
    user_data_page.add_last_name(last_name=LAST_NAME)
    user_data_page.add_middle_name(middle_name=MIDDLE_NAME)
    user_data_page.add_address(address=ADDRESS)
    user_data_page.add_card_number(card_number=CARD_NUMBER)

    # Нажать кнопку "Оформить заказ".
    user_data_page.click_button_place_order()

    # Убедиться, что находимся на странице "Оформление заказа: Подтверждение заказа".
    assert "checkoutOverview" in driver.current_url, "Ошибка: Некорректная страница!"

    title_order_confirmation = order_confirmation_page.get_title_order_confirmation()
    assert title_order_confirmation == "Оформление заказа: Подтверждение заказа", \
        f"Ошибка: Некорректный заголовок страницы! Актуальный: {title_order_confirmation}."
    print("Корректный переход на страницу для подтверждения заказа.")

    # На странице "Оформление заказа: Подтверждение заказа" нажать на кнопку "Завершить заказ".
    order_confirmation_page.click_complete_order_button()

    # Убедиться в наличии сообщения "Ваш заказ успешно создан".
    assert "checkoutComplete" in driver.current_url, "Ошибка: Некорректная страница!"

    title_order_successfully_created = checkout_complete_page.get_title_order_successfully_created()
    assert title_order_successfully_created == "Оформление заказа: Заказ успешно создан", \
        f"Ошибка: Некорректный заголовок страницы! Актуальный: {title_order_successfully_created}."
    print("Успешное оформление заказа.")
