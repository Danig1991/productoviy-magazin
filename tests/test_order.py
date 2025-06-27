import logging

import allure

from pages.checkout_complete_page import CheckoutCompletePage
from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.order_confirmation_page import OrderConfirmationPage
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.user_data_page import UserDataPage
from utils.config import UserData, ProductConfig


@allure.epic("Тест оформления заказа.")
@allure.title("Корректная передача данных.")
def test_order_1(shopper_auth, add_two_products, go_to_cart):
    driver = shopper_auth
    user_data = UserData().get_user_data()

    logging.info("Зафиксировать итоговую сумму.")
    user_data["Итоговая стоимость"] = ShoppingCartPage(driver).get_total_sum()

    # Нажать кнопку 'Оформить заказ'.
    ShoppingCartPage(driver).click_button_place_order()

    logging.info("Заполнение полей корректными данными.")
    UserDataPage(driver).add_user_data(
        first_name=user_data["Имя"],
        last_name=user_data["Фамилия"],
        middle_name=user_data["Отчество"],
        address=user_data["Адрес доставки"],
        card_number=user_data["Номер карты"]
    )
    # Нажать кнопку 'Оформить заказ'.
    UserDataPage(driver).click_button_place_order()

    logging.info("Сравнить ранее зафиксированные данные с данными на странице "
                 "'Оформление заказа: Подтверждение заказа'.")
    current_data = OrderConfirmationPage(driver).get_order_confirmation_data()

    for key in current_data:
        assert current_data[key] == user_data[key], (
            f"Ошибка: В поле '{key}' значение: '{current_data[key]}'. "
            f"Ожидаемое: '{user_data[key]}'"
        )
    logging.info("Итоговая сумма и данные для подтверждения заказа передаются корректно.")


@allure.epic("Тест оформления заказа.")
@allure.title("Оформление заказа.")
def test_order_2(shopper_auth):
    driver = shopper_auth
    product_name = ProductConfig.PRODUCT_NAME
    quantity_2 = ProductConfig.QUANTITY_2
    user_data = UserData().get_user_data()

    logging.info("Убедиться, что находимся на странице 'Продукты'.")
    title_products = ProductsPage(driver).get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок 'Продукты' на странице не найден!"
    logging.info("Выполнен переход на страницу 'Продукты'.")

    # Добавить один продукт в количестве 2 шт.
    ProductsPage(driver).set_product_quantity(product_name, quantity_2)
    # Перейти на страницу 'Корзинка' (нажать на иконку корзины).
    FixedPanelIcons(driver).click_shopping_cart()

    logging.info("Убедиться, что находимся на странице 'Корзинка'.")
    assert "cart" in driver.current_url, "Ошибка: Некорректная страница!"

    title_shopping_cart = ShoppingCartPage(driver).get_title_shopping_cart()
    assert title_shopping_cart == "Корзинка", \
        "Ошибка: Заголовок 'Корзинка' на странице не найден!"
    logging.info("Выполнен переход на страницу 'Корзинка'.")

    # Нажать кнопку 'Оформить заказ'.
    ShoppingCartPage(driver).click_button_place_order()

    logging.info("Убедиться, что находимся на странице 'Оформление заказа: Данные пользователя'.")
    assert "checkout" in driver.current_url, "Ошибка: Некорректная страница!"

    title_user_data = UserDataPage(driver).get_title_user_data()
    assert title_user_data == "Оформление заказа: Данные пользователя", \
        f"Ошибка: Некорректный заголовок страницы! Актуальный: {title_user_data}."
    logging.info("Корректный переход на страницу для заполнения данных о пользователе.")

    logging.info("Заполнение полей корректными данными.")
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

    # На странице 'Оформление заказа: Подтверждение заказа' нажать на кнопку 'Завершить заказ'.
    OrderConfirmationPage(driver).click_complete_order_button()

    logging.info("Убедиться в наличии сообщения 'Ваш заказ успешно создан'.")
    assert "checkoutComplete" in driver.current_url, "Ошибка: Некорректная страница!"

    title_order_successfully_created = CheckoutCompletePage(driver).get_title_order_successfully_created()
    assert title_order_successfully_created == "Оформление заказа: Заказ успешно создан", \
        f"Ошибка: Некорректный заголовок страницы! Актуальный: {title_order_successfully_created}."
    logging.info("Успешное оформление заказа.")
