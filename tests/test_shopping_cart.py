import pytest

from configurations.action_with_product import QUANTITY_2, PRODUCT_NAME
from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.shopping_cart_page import ShoppingCartPage
from pages.user_data_page import UserDataPage


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_cart_1(authorization):
    driver = authorization

    # На странице с продуктами найти и нажать на иконку корзины.
    FixedPanelIcons(driver).click_shopping_cart()

    # Убедиться, что находимся на странице "Корзинка".
    assert "cart" in driver.current_url.lower(), "Ошибка: Некорректная страница!"

    title_shopping_cart = ShoppingCartPage(driver).get_title_shopping_cart()
    assert "Корзинка" in title_shopping_cart, \
        "Ошибка: Заголовок \"Корзинка\" на странице не найден!"
    print("Выполнен переход на страницу \"Корзинка\".")


# вход в роли пользователя, добавлено 2 продукта, переход в корзину
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_cart_2(authorization, add_two_products, go_to_cart):
    driver = authorization

    shopping_cart_page = ShoppingCartPage(driver)

    # Удалить товар из корзины - нажать на кнопку "-" 2 раза.
    shopping_cart_page.decrease_product_quantity(product_name=PRODUCT_NAME, decrease_by=QUANTITY_2)

    # Убедиться, что корзина очищена, на странице отображается сообщение: "в корзине пока пусто".
    empty_cart_message = shopping_cart_page.get_empty_cart_message()
    assert "в корзине пока пусто" in empty_cart_message, "Ошибка: Текст сообщения не совпадает"
    print("Отображается сообщение: \"в корзине пока пусто\".")


# вход в роли пользователя, добавлено 2 продукта, переход в корзину
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_cart_3(authorization, add_two_products, go_to_cart):
    driver = authorization

    # Убедиться, что кнопка "Оформить заказ" доступна.
    button_place_order = ShoppingCartPage(driver).button_place_order()
    assert button_place_order.is_enabled(), "Ошибка: Кнопка \"Оформить заказ\" недоступна!"
    print("Кнопка \"Оформить заказ\" доступна.")


# вход в роли пользователя, добавлено 2 продукта, переход в корзину
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_cart_4(authorization, add_two_products, go_to_cart):
    driver = authorization

    # Убедиться, что у выбранного продукта в окне между "-" и "+" отображается количество товара, равное 2.
    counter_value = ShoppingCartPage(driver).get_product_counter_value(product_name=PRODUCT_NAME)
    assert counter_value == QUANTITY_2, \
        (f"Ошибка: Отображаемое количество продукта \"{PRODUCT_NAME}\" - {counter_value} шт. "
         f"Ожидается: {QUANTITY_2} шт.")
    print("Количество добавленных продуктов в корзине отображается корректно.")


# вход в роли пользователя, добавлено 2 продукта, переход в корзину
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_cart_5(authorization, add_two_products, go_to_cart):
    driver = authorization

    shopping_cart_page = ShoppingCartPage(driver)

    # Найти на странице строку с итоговой суммой ("Итого:" и конечная стоимость).
    counter_value = shopping_cart_page.get_product_counter_value(product_name=PRODUCT_NAME)
    product_price = shopping_cart_page.get_product_price(product_name=PRODUCT_NAME)
    total_sum = shopping_cart_page.get_total_sum()

    # Убедиться, что сумма 2 товаров совпадает с конечной стоимостью.
    assert total_sum == product_price * counter_value, \
        (f"Ошибка: Ожидаемая сумма: {product_price * counter_value} ₽, "
         f"Фактическая: {total_sum} ₽.")
    print("Итоговая сумма отображается корректно.")


# вход в роли пользователя, добавлено 2 продукта, переход в корзину
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_cart_6(authorization, add_two_products, go_to_cart):
    driver = authorization

    # Нажать на кнопку "Оформить заказ".
    ShoppingCartPage(driver).click_button_place_order()

    # Убедиться, что находимся на странице "Оформление заказа: Данные пользователя".
    assert "checkout" in driver.current_url, "Ошибка: Некорректная страница!"

    title_user_data = UserDataPage(driver).get_title_user_data()
    assert title_user_data == "Оформление заказа: Данные пользователя", \
        f"Ошибка: Некорректный заголовок страницы! Актуальный: {title_user_data}."
    print("Корректный переход на страницу для заполнения данных о пользователе.")
