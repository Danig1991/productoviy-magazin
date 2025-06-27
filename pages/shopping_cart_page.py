import logging
import time

import allure
from selenium.webdriver.common.by import By

from utils.action_with_element import ActionWithElement


class ShoppingCartPage(ActionWithElement):
    TITLE_SHOPPING_CART_LOCATOR = (By.CSS_SELECTOR, "div.navbar-brand")
    EMPTY_CART_LOCATOR = (By.XPATH, "//*[contains(text(), 'в корзине пока пусто')]")
    BUTTON_PLACE_ORDER_LOCATOR = (By.CSS_SELECTOR, ".btn-success")
    TOTAL_SUM_LOCATOR = (By.XPATH, "//*[contains(text(), 'Итого')]")

    @allure.step("Получить заголовок 'Корзинка'")
    def get_title_shopping_cart(self):
        return self.visibility_of_element_located(self.TITLE_SHOPPING_CART_LOCATOR, "Корзинка").text

    @allure.step("Получить надпись 'в корзине пока пусто'")
    def get_empty_cart_message(self):
        return self.visibility_of_element_located(self.EMPTY_CART_LOCATOR, "Пустая корзинка").text

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

        for _ in range(clicks):
            self.click_button(selected_button)

    @allure.step("Уменьшить количество товара на указанное значение")
    def decrease_product_quantity(self, product_name, decrease_by):
        self._click_selected_button_repeatedly(product_name, "remove", decrease_by)
        logging.info(f"Количество '{product_name}' уменьшено на {decrease_by}.")

    # кнопка "Оформить заказ"
    def button_place_order(self):
        button_place_order = self.visibility_of_element_located(
            self.BUTTON_PLACE_ORDER_LOCATOR,
            "Оформить заказ"
        )
        return button_place_order

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_button_place_order(self):
        self.click_button(self.button_place_order())
        logging.info("Нажатие кнопки 'Оформить заказ'. "
                     "Переход на страницу 'Оформление заказа: Данные пользователя'")

    @allure.step("Получить значение счетчика продукта")
    def get_product_counter_value(self, product_name):
        time.sleep(1.5)
        counter_value = self.visibility_of_element_located(
            (
                By.XPATH,
                f"//*[contains(text(), '{product_name}')]"
                "/ancestor::div[contains(@class, 'store-card border')]"
                "//input[contains(@class, 'form-control shadow-none')]"

            ),
            f"Счетчик продукта '{product_name}'"
        )
        return int(counter_value.get_attribute("value"))

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
        total_sum_element = self.visibility_of_element_located(self.TOTAL_SUM_LOCATOR, "Итоговая сумма")
        total_sum = total_sum_element.text.split(":")[1].replace("₽", "").strip()

        return int(total_sum)
