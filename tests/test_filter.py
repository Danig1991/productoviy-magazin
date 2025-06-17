import pytest

from configurations.values_for_filter import (
    SORT_BY_PRICE_LOW_TO_HIGH,
    SORT_BY_PRICE_HIGH_TO_LOW,
    SORT_BY_NAME_A_TO_Z,
    SORT_BY_NAME_Z_TO_A,
    BURGER,
    PIE,
    ROLL,
    SANDWICH,
    MIN_PRICE,
    MAX_PRICE
)
from pages.products_page import ProductsPage


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_filter_1(authorization):
    driver = authorization

    products_page = ProductsPage(driver)

    # На странице с продуктами найти и нажать выпадающий список.
    # В выпадающем списке выбрать значение: "Цена: Сначала подешевле".
    products_page.select_dropdown_option(value=SORT_BY_PRICE_LOW_TO_HIGH)

    # Убедиться, что ассортимент товара отсортирован верно.
    product_prices = products_page.get_list_of_product_prices()
    assert product_prices == sorted(product_prices), \
        f"Ошибка: Цены не отсортированы по возрастанию! Фактический порядок: {product_prices}"
    print("Товар отображается по цене от меньшей к большей.")


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_filter_2(authorization):
    driver = authorization

    products_page = ProductsPage(driver)

    # На странице с продуктами найти и нажать выпадающий список.
    # В выпадающем списке выбрать значение: "Цена: Сначала подороже".
    products_page.select_dropdown_option(value=SORT_BY_PRICE_HIGH_TO_LOW)

    # Убедиться, что ассортимент товара отсортирован верно.
    product_prices = products_page.get_list_of_product_prices()
    assert product_prices == sorted(product_prices, reverse=True), \
        f"Ошибка: Цены не отсортированы по убыванию! Фактический порядок: {product_prices}"
    print("Товар отображается по цене от большей к меньшей.")


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_filter_3(authorization):
    driver = authorization

    products_page = ProductsPage(driver)

    # На странице с продуктами найти и нажать выпадающий список.
    # В выпадающем списке выбрать значение: "Наименование: от А до Я".
    products_page.select_dropdown_option(value=SORT_BY_NAME_A_TO_Z)

    # Убедиться, что ассортимент товара отсортирован верно.
    product_names = products_page.get_list_of_product_names()
    assert product_names == sorted(product_names), \
        f"Ошибка: Наименования продуктов не отсортированы по алфавиту! Фактический порядок: {product_names}"
    print("Товар отображается в алфавитном порядке.")


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_filter_4(authorization):
    driver = authorization

    products_page = ProductsPage(driver)

    # На странице с продуктами найти и нажать выпадающий список.
    # В выпадающем списке выбрать значение: "Наименование: от Я до А".
    products_page.select_dropdown_option(value=SORT_BY_NAME_Z_TO_A)

    # Убедиться, что ассортимент товара отсортирован верно.
    product_names = products_page.get_list_of_product_names()
    assert product_names == sorted(product_names, reverse=True), \
        (f"Ошибка: Наименования продуктов не отсортированы по алфавиту в обратном порядке! "
         f"Фактический порядок: {product_names}")
    print("Товар отображается по алфавиту в обратном порядке.")


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_filter_5(authorization):
    driver = authorization

    products_page = ProductsPage(driver)

    # На странице с продуктами найти и нажать кнопку фильтра (иконка с ползунками).
    # В блоке "Категории" оставить активным чек-бокс "Бургер".
    products_page.click_filter_menu()
    products_page.checkbox_activation(value=BURGER, activate=True)
    products_page.checkbox_activation(value=SANDWICH, activate=False)
    products_page.checkbox_activation(value=PIE, activate=False)
    products_page.checkbox_activation(value=ROLL, activate=False)
    products_page.click_filter_menu()

    # Убедиться, что товар соответствует выбранной категории.
    product_names = ProductsPage(driver).get_list_of_product_names()
    for name in product_names:
        assert "Бургер" in name, \
            f"Ошибка: Продукт: \"{name}\" - не соответствует категории \"Бургер\"!"
    print("Продукты соответствуют категории \"Бургер\".")


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_filter_6(authorization):
    driver = authorization

    products_page = ProductsPage(driver)

    # На странице с продуктами найти и нажать кнопку фильтра (иконка с ползунками).
    # В блоке "Категории" оставить активным чек-бокс "Сэндвич".
    products_page.click_filter_menu()
    products_page.checkbox_activation(value=SANDWICH, activate=True)
    products_page.checkbox_activation(value=BURGER, activate=False)
    products_page.checkbox_activation(value=PIE, activate=False)
    products_page.checkbox_activation(value=ROLL, activate=False)
    products_page.click_filter_menu()

    # Убедиться, что товар соответствует выбранной категории.
    product_names = ProductsPage(driver).get_list_of_product_names()
    for name in product_names:
        assert "Сэндвич" in name, \
            f"Ошибка: Продукт: \"{name}\" - не соответствует категории \"Сэндвич\"!"
    print("Продукты соответствуют категории \"Сэндвич\".")


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_filter_7(authorization):
    driver = authorization

    products_page = ProductsPage(driver)

    # На странице с продуктами найти и нажать кнопку фильтра (иконка с ползунками).
    # В блоке "Категории" не активен ни один чек-бокс.
    products_page.click_filter_menu()
    products_page.checkbox_activation(value=SANDWICH, activate=False)
    products_page.checkbox_activation(value=BURGER, activate=False)
    products_page.checkbox_activation(value=PIE, activate=False)
    products_page.checkbox_activation(value=ROLL, activate=False)
    products_page.click_filter_menu()

    # Убедиться, что товар отсутствует.
    product_card_count = products_page.get_product_card_count()
    assert product_card_count == 0, \
        f"Ошибка: Найдено {product_card_count} товаров, ожидалось: 0"
    print("Ни один товар не отображается.")


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_filter_8(authorization):
    driver = authorization

    products_page = ProductsPage(driver)

    # На странице с продуктами найти и нажать кнопку фильтра (иконка с ползунками).
    # В блоке "Цена" ввести данные: в поле "от" - 100, в поле "до" - 150.
    products_page.click_filter_menu()
    products_page.set_price_filter_range(min_price=MIN_PRICE, max_price=MAX_PRICE)
    products_page.click_filter_menu()

    # Убедиться, что товар соответствует введенному ценовому диапазону.
    product_prices = products_page.get_list_of_product_prices()
    for price in product_prices:
        assert MIN_PRICE <= price <= MAX_PRICE, \
            f"Ошибка: Цена {price} вне диапазона: от {MIN_PRICE} до {MAX_PRICE}!"
    print("Товар соответствует введенному ценовому диапазону.")
