import pytest

from configurations.action_with_product import PRODUCT_NAME, QUANTITY_105, QUANTITY_505
from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingCartPage


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_max_1(authorization):
    driver = authorization

    products_page = ProductsPage(driver)

    # Добавить в корзину один продукт в количестве 105 шт.
    products_page.set_product_quantity(product_name=PRODUCT_NAME, target_quantity=QUANTITY_105)
    # Перейти на страницу "Корзинка" (нажать на иконку корзины).
    FixedPanelIcons(driver).click_shopping_cart()

    # Убедиться, что товара добавлено только 100 шт.
    counter_value = ShoppingCartPage(driver).get_product_counter_value(product_name=PRODUCT_NAME)
    assert counter_value <= 100, f"Ошибка: Добавлено {counter_value} шт. продукта! Максимум 100."
    print("Добавлено не более 100 единиц одного наименования продукта.")


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_max_2(authorization):
    driver = authorization

    products_page = ProductsPage(driver)

    # Добавить в корзину один продукт на сумму более 100000 ₽ (505 шт. при цене 199 р.).
    products_page.set_product_quantity(product_name=PRODUCT_NAME, target_quantity=QUANTITY_505)

    # Перейти на страницу "Корзинка" (нажать на иконку корзины).
    FixedPanelIcons(driver).click_shopping_cart()

    # Убедиться, что общая сумма заказа не более 100000 ₽.
    total_sum = ShoppingCartPage(driver).get_total_sum()
    assert total_sum <= 100_000, f"Ошибка: Общая сумма заказа {total_sum} ₽! Максимум 100000₽."
    print("Общая сумма заказа не превышает 100000 ₽.")
