import logging

from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingCartPage
from utils.config import ProductConfig
from utils.double import Double


def test_max_1(shopper_auth):
    driver = shopper_auth
    logging.info("Вход в роли пользователя")

    products_page = ProductsPage(driver)
    shopping_cart_page = ShoppingCartPage(driver)
    fixed_panel_icons = FixedPanelIcons(driver)
    product_name = ProductConfig.PRODUCT_NAME
    quantity_105 = ProductConfig.QUANTITY_105

    logging.info("Добавить в корзину один продукт в количестве 105 шт.")
    products_page.set_product_quantity(product_name, quantity_105)

    logging.info("Перейти на страницу \"Корзинка\" (нажать на иконку корзины).")
    fixed_panel_icons.click_shopping_cart()

    logging.info("Убедиться, что товара добавлено только 100 шт.")
    counter_value = shopping_cart_page.get_product_counter_value(product_name)
    assert counter_value <= 100, f"Ошибка: Добавлено {counter_value} шт. продукта! Максимум 100."
    Double.print_and_log("Добавлено не более 100 единиц одного наименования продукта.")


def test_max_2(shopper_auth):
    driver = shopper_auth
    logging.info("Вход в роли пользователя")

    products_page = ProductsPage(driver)
    shopping_cart_page = ShoppingCartPage(driver)
    fixed_panel_icons = FixedPanelIcons(driver)
    product_name = ProductConfig.PRODUCT_NAME
    quantity_505 = ProductConfig.QUANTITY_505

    logging.info("Добавить в корзину один продукт на сумму более 100000 ₽ (505 шт. при цене 199 р.).")
    products_page.set_product_quantity(product_name, quantity_505)

    logging.info("Перейти на страницу \"Корзинка\" (нажать на иконку корзины).")
    fixed_panel_icons.click_shopping_cart()

    logging.info("Убедиться, что общая сумма заказа не более 100000 ₽.")
    total_sum = shopping_cart_page.get_total_sum()
    assert total_sum <= 100_000, f"Ошибка: Общая сумма заказа {total_sum} ₽! Максимум 100000₽."
    Double.print_and_log("Общая сумма заказа не превышает 100000 ₽.")
