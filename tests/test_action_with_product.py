import pytest

from configurations.action_with_product import PRODUCT_NAME, QUANTITY_1, QUANTITY_2, QUANTITY_3
from pages.products_page import ProductsPage


# вход в роли пользователя, добавлено 2 продукта
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_prod_act_1(authorization, add_two_products):
    driver = authorization

    # Убедиться, что у выбранного продукта в окне между "-" и "+" отображается количество товара, равное 2.
    product_counter_value = ProductsPage(driver).get_product_counter_value(product_name=PRODUCT_NAME)
    assert product_counter_value == QUANTITY_2, \
        (f"Ошибка: Отображаемое количество продукта \"{PRODUCT_NAME}\" - {product_counter_value} шт. "
         f"Ожидается: {QUANTITY_2} шт.")
    print("Отображение количества товара происходит корректно.")


# вход в роли пользователя, добавлено 2 продукта
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_prod_act_2(authorization, add_two_products):
    driver = authorization
    products_page = ProductsPage(driver)

    # Уменьшить количество товара - нажать на кнопку "-" 1 раз.
    products_page.decrease_product_quantity(product_name=PRODUCT_NAME, decrease_by=QUANTITY_1)

    # Убедиться, что у выбранного продукта в окне между "-" и "+" отображается количество товара, равное 1.
    product_counter_value = products_page.get_product_counter_value(product_name=PRODUCT_NAME)
    assert product_counter_value == QUANTITY_1, \
        (f"Ошибка: Отображаемое количество продукта \"{PRODUCT_NAME}\" - {product_counter_value} шт. "
         f"Ожидается: {QUANTITY_1} шт.")
    print("Уменьшение количества товара происходит корректно.")


# вход в роли пользователя, добавлено 2 продукта
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_prod_act_3(authorization, add_two_products):
    driver = authorization
    products_page = ProductsPage(driver)

    # Уменьшить количество товара - нажать на кнопку "-" 3 раза.
    products_page.decrease_product_quantity(product_name=PRODUCT_NAME, decrease_by=QUANTITY_3)

    # Убедиться, что у выбранного продукта в окне между "-" и "+" отображается количество товара,
    # равное 0, не присутствует отрицательных значений.
    product_counter_value = products_page.get_product_counter_value(product_name=PRODUCT_NAME)
    assert product_counter_value == 0, \
        (f"Ошибка: Отображаемое количество продукта \"{PRODUCT_NAME}\" - {product_counter_value} шт. "
         f"Ожидается: 0 шт.")
    print("Уменьшение количества товара происходит корректно. Нет отрицательных значений.")
