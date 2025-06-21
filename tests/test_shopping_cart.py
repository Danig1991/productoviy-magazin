import logging

from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.shopping_cart_page import ShoppingCartPage
from pages.user_data_page import UserDataPage
from utils.config import ProductConfig
from utils.double import Double


def test_cart_1(shopper_auth):
    driver = shopper_auth
    logging.info("Вход в роли пользователя")

    fixed_panel_icons = FixedPanelIcons(driver)
    shopping_cart_page = ShoppingCartPage(driver)

    logging.info("На странице с продуктами найти и нажать на иконку корзины.")
    fixed_panel_icons.click_shopping_cart()

    logging.info("Убедиться, что находимся на странице \"Корзинка\".")
    assert "cart" in driver.current_url.lower(), "Ошибка: Некорректная страница!"

    title_shopping_cart = shopping_cart_page.get_title_shopping_cart()
    assert "Корзинка" in title_shopping_cart, \
        "Ошибка: Заголовок \"Корзинка\" на странице не найден!"
    Double.print_and_log("Выполнен переход на страницу \"Корзинка\".")


def test_cart_2(shopper_auth, add_two_products, go_to_cart):
    driver = shopper_auth
    logging.info("Вход в роли пользователя, добавлено 2 продукта, переход в корзину")

    shopping_cart_page = ShoppingCartPage(driver)
    product_name = ProductConfig.PRODUCT_NAME
    quantity_2 = ProductConfig.QUANTITY_2

    logging.info("Удалить товар из корзины - нажать на кнопку \"-\" 2 раза.")
    shopping_cart_page.decrease_product_quantity(product_name, quantity_2)

    logging.info("Убедиться, что корзина очищена, на странице отображается сообщение: "
                 "\"в корзине пока пусто\".")
    empty_cart_message = shopping_cart_page.get_empty_cart_message()
    assert "в корзине пока пусто" in empty_cart_message, "Ошибка: Текст сообщения не совпадает"
    Double.print_and_log("Отображается сообщение: \"в корзине пока пусто\".")


def test_cart_3(shopper_auth, add_two_products, go_to_cart):
    driver = shopper_auth
    logging.info("Вход в роли пользователя, добавлено 2 продукта, переход в корзину")

    shopping_cart_page = ShoppingCartPage(driver)

    logging.info("Убедиться, что кнопка \"Оформить заказ\" доступна.")
    button_place_order = shopping_cart_page.button_place_order()
    assert button_place_order.is_enabled(), "Ошибка: Кнопка \"Оформить заказ\" недоступна!"
    Double.print_and_log("Кнопка \"Оформить заказ\" доступна.")


def test_cart_4(shopper_auth, add_two_products, go_to_cart):
    driver = shopper_auth
    logging.info("Вход в роли пользователя, добавлено 2 продукта, переход в корзину")

    shopping_cart_page = ShoppingCartPage(driver)
    product_name = ProductConfig.PRODUCT_NAME
    quantity_2 = ProductConfig.QUANTITY_2

    logging.info("Убедиться, что у выбранного продукта в окне между \"-\" и \"+\" "
                 "отображается количество товара, равное 2.")
    counter_value = shopping_cart_page.get_product_counter_value(product_name)
    assert counter_value == quantity_2, \
        (f"Ошибка: Отображаемое количество продукта \"{product_name}\" - {counter_value} шт. "
         f"Ожидается: {quantity_2} шт.")
    Double.print_and_log("Количество добавленных продуктов в корзине отображается корректно.")


def test_cart_5(shopper_auth, add_two_products, go_to_cart):
    driver = shopper_auth
    logging.info("Вход в роли пользователя, добавлено 2 продукта, переход в корзину")

    shopping_cart_page = ShoppingCartPage(driver)
    product_name = ProductConfig.PRODUCT_NAME

    logging.info("Найти на странице строку с итоговой суммой (\"Итого:\" и конечная стоимость).")
    counter_value = shopping_cart_page.get_product_counter_value(product_name)
    product_price = shopping_cart_page.get_product_price(product_name)
    total_sum = shopping_cart_page.get_total_sum()

    logging.info("Убедиться, что сумма 2 товаров совпадает с конечной стоимостью.")
    assert total_sum == product_price * counter_value, \
        (f"Ошибка: Ожидаемая сумма: {product_price * counter_value} ₽, "
         f"Фактическая: {total_sum} ₽.")
    Double.print_and_log("Итоговая сумма отображается корректно.")


def test_cart_6(shopper_auth, add_two_products, go_to_cart):
    driver = shopper_auth
    logging.info("Вход в роли пользователя, добавлено 2 продукта, переход в корзину")

    shopping_cart_page = ShoppingCartPage(driver)
    user_data_page = UserDataPage(driver)

    logging.info("Нажать на кнопку \"Оформить заказ\".")
    shopping_cart_page.click_button_place_order()

    logging.info("Убедиться, что находимся на странице \"Оформление заказа: Данные пользователя\".")
    assert "checkout" in driver.current_url, "Ошибка: Некорректная страница!"

    title_user_data = user_data_page.get_title_user_data()
    assert title_user_data == "Оформление заказа: Данные пользователя", \
        f"Ошибка: Некорректный заголовок страницы! Актуальный: {title_user_data}."
    Double.print_and_log("Корректный переход на страницу для заполнения данных о пользователе.")
