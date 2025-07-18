import logging

import allure

from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingCartPage
from utils.config import ProductConfig


@allure.epic("Тест максимальных значений.")
@allure.title("Максимальное количество товаров в корзине - 100 единиц одного наименования.")
def test_max_1(shopper_auth):
    driver = shopper_auth
    product_name = ProductConfig.PRODUCT_NAME
    quantity_105 = ProductConfig.QUANTITY_105

    # Добавить в корзину один продукт в количестве 105 шт.
    ProductsPage(driver).set_product_quantity(product_name, quantity_105)
    # Перейти на страницу 'Корзинка' (нажать на иконку корзины).
    FixedPanelIcons(driver).click_shopping_cart()

    logging.info("Убедиться, что товара добавлено только 100 шт.")
    counter_value = ShoppingCartPage(driver).get_product_counter_value(product_name)
    assert counter_value <= 100, f"Ошибка: Добавлено {counter_value} шт. продукта! Максимум 100."
    logging.info("Добавлено не более 100 единиц одного наименования продукта.")


@allure.epic("Тест максимальных значений.")
@allure.title("Общая сумма заказа не должна превышать 100000 ₽.")
def test_max_2(shopper_auth):
    driver = shopper_auth
    product_name = ProductConfig.PRODUCT_NAME
    quantity_505 = ProductConfig.QUANTITY_505

    # Добавить в корзину один продукт на сумму более 100000 ₽ (505 шт. при цене 199 р.).
    ProductsPage(driver).set_product_quantity(product_name, quantity_505)
    # Перейти на страницу 'Корзинка' (нажать на иконку корзины).
    FixedPanelIcons(driver).click_shopping_cart()

    logging.info("Убедиться, что общая сумма заказа не более 100000 ₽.")
    total_sum = ShoppingCartPage(driver).get_total_sum()
    assert total_sum <= 100_000, f"Ошибка: Общая сумма заказа {total_sum} ₽! Максимум 100000₽."
    logging.info("Общая сумма заказа не превышает 100000 ₽.")
