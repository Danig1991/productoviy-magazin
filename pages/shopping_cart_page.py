import time

import allure
from selenium.webdriver.common.by import By

from utils.expectation import Expectation

TITLE_SHOPPING_CART_LOCATOR = (By.CSS_SELECTOR, "div.navbar-brand")
EMPTY_CART_LOCATOR = (By.XPATH, "//*[contains(text(), 'в корзине пока пусто')]")
BUTTON_PLACE_ORDER_LOCATOR = (By.CSS_SELECTOR, ".btn-success")
TOTAL_SUM_LOCATOR = (By.XPATH, "//*[contains(text(), 'Итого')]")


class ShoppingCartPage(Expectation):

    @allure.step("Получить заголовок 'Корзинка'")
    def get_title_shopping_cart(self):
        return self.visibility_of_element_located(TITLE_SHOPPING_CART_LOCATOR, "Корзинка").text

    @allure.step("Получить надпись 'в корзине пока пусто'")
    def get_empty_cart_message(self):
        return self.visibility_of_element_located(EMPTY_CART_LOCATOR, "Пустая корзинка").text

    # Нажать выбранную кнопку несколько раз
    def _click_selected_button_repeatedly(self, product_name, action, clicks):
        selected_button = self.visibility_of_element_located(
            (
                By.XPATH,
                f"//*[contains(text(), '{product_name}')]"
                "/ancestor::div[contains(@class, 'store-card border')]"
                f"//span[text()='{action}']"
                "/ancestor::button"
            ),
            f"Кнопка {'+' if action == 'add' else '-'} для '{product_name}'"
        )

        self.move_to_element(selected_button)

        for _ in range(clicks):
            selected_button.click()
            time.sleep(0.15)

    @allure.step("Уменьшить количество товара на указанное значение")
    def decrease_product_quantity(self, product_name, decrease_by):
        self._click_selected_button_repeatedly(product_name, "remove", decrease_by)
        print(f"Количество '{product_name}' уменьшено на {decrease_by}.")

    # кнопка "Оформить заказ"
    def button_place_order(self):
        button_place_order = self.visibility_of_element_located(BUTTON_PLACE_ORDER_LOCATOR, "Оформить заказ")
        self.move_to_element(button_place_order)
        return button_place_order

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_button_place_order(self):
        self.button_place_order().click()
        print("На странице \"Корзинка\" нажата кнопка \"Оформить заказ\".")

    @allure.step("Получить значение счетчика продукта")
    def get_product_counter_value(self, product_name):
        time.sleep(2)
        counter_value = self.visibility_of_element_located(
            (
                By.XPATH,
                f"//*[contains(text(), '{product_name}')]"
                "/ancestor::div[contains(@class, 'store-card border')]"
                "//input[contains(@class, 'form-control shadow-none')]"

            ),
            f"Счетчик продукта '{product_name}'"
        ).get_attribute("value")
        return int(counter_value)

    @allure.step("Получить цену продукта")
    def get_product_price(self, product_name):
        product_price = self.visibility_of_element_located(
            (
                By.XPATH,
                f"//*[contains(text(), '{product_name}')]"
                "/ancestor::div[contains(@class, 'store-card border')]"
                "//div[contains(@class, 'fs-5')]"
            ),
            f"Цена продукта '{product_name}'"
        ).text
        return int(product_price[:-5])

    @allure.step("Получить итоговую сумму")
    def get_total_sum(self):
        total_sum_element = self.visibility_of_element_located(TOTAL_SUM_LOCATOR, "Итоговая сумма")
        self.move_to_element(total_sum_element)
        total_sum = total_sum_element.text.split(":")[1].replace("₽", "").strip()

        return int(total_sum)
