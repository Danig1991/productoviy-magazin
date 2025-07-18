import logging

import allure

from pages.products_page import ProductsPage
from utils.config import ProductConfig


@allure.epic("Тест 'действие с продуктом'.")
@allure.title("Увеличение одного и того же товара в количестве 2 шт. (страница 'Продукты').")
def test_prod_act_1(shopper_auth, add_two_products):
    driver = shopper_auth
    product_name = ProductConfig.PRODUCT_NAME
    quantity_2 = ProductConfig.QUANTITY_2

    logging.info("Убедиться, что у выбранного продукта в окне "
                 "между '-' и '+' отображается количество товара, равное 2.")
    product_counter_value = ProductsPage(driver).get_product_counter_value(product_name)
    assert product_counter_value == quantity_2, \
        (f"Ошибка: Отображаемое количество продукта '{product_name}' - "
         f"{product_counter_value} шт. Ожидается: {quantity_2} шт.")
    logging.info("Отображение количества товара происходит корректно.")


@allure.epic("Тест 'действие с продуктом'.")
@allure.title("Уменьшение количества товара до 1) (страница 'Продукты').")
def test_prod_act_2(shopper_auth, add_two_products):
    driver = shopper_auth
    product_name = ProductConfig.PRODUCT_NAME
    quantity_1 = ProductConfig.QUANTITY_1

    # Уменьшить количество товара - нажать на кнопку '-' 1 раз.
    ProductsPage(driver).decrease_product_quantity(product_name, quantity_1)

    logging.info("Убедиться, что у выбранного продукта в окне "
                 "между '-' и '+' отображается количество товара, равное 1.")
    product_counter_value = ProductsPage(driver).get_product_counter_value(product_name)
    assert product_counter_value == quantity_1, \
        (f"Ошибка: Отображаемое количество продукта '{product_name}' - {product_counter_value} шт. "
         f"Ожидается: {quantity_1} шт.")
    logging.info("Уменьшение количества товара происходит корректно.")


@allure.epic("Тест 'действие с продуктом'.")
@allure.title("Уменьшение товара на количество больше, чем есть (страница 'Продукты').")
def test_prod_act_3(shopper_auth, add_two_products):
    driver = shopper_auth
    product_name = ProductConfig.PRODUCT_NAME
    quantity_3 = ProductConfig.QUANTITY_3

    logging.info("Уменьшить количество товара - нажать на кнопку '-' 3 раза.")
    ProductsPage(driver).decrease_product_quantity(product_name, quantity_3)

    logging.info("Убедиться, что у выбранного продукта в окне между '-' и '+' "
                 "отображается количество товара, равное 0, не присутствует отрицательных значений.")
    product_counter_value = ProductsPage(driver).get_product_counter_value(product_name)
    assert product_counter_value == 0, \
        (f"Ошибка: Отображаемое количество продукта '{product_name}' - {product_counter_value} шт. "
         f"Ожидается: 0 шт.")
    logging.info("Уменьшение количества товара происходит корректно. Нет отрицательных значений.")
