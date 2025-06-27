import logging

import allure
from selenium.webdriver.common.by import By

from utils.action_with_element import ActionWithElement


class EditProductsPage(ActionWithElement):
    ADD_PRODUCT_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn-success")
    EDIT_PRODUCT_BUTTON_LOCATOR = (
        By.XPATH,
        "//*[contains(text(), 'Тестовый')]"
        "/ancestor::div[contains(@class, 'store-card')]"
        "//button[contains(@class, 'btn-outline-success')]"
    )
    DELETE_PRODUCT_BUTTON_LOCATOR = (
        By.XPATH,
        "//*[contains(text(), 'Тестовый')]"
        "/ancestor::div[contains(@class, 'store-card')]"
        "//button[contains(@class, 'btn-outline-danger')]"
    )

    @allure.step("Нажать кнопку 'Добавить товар'")
    def click_add_product_button(self):
        add_product_button = self.visibility_of_element_located(
            self.ADD_PRODUCT_BUTTON_LOCATOR,
            "Добавить товар"
        )
        self.click_button(add_product_button)
        logging.info("Нажатие кнопки 'Добавить товар'.")

    @allure.step("Нажать кнопку редактирования товара (иконка карандаша)")
    def click_edit_product_button(self):
        edit_product_button = self.visibility_of_element_located(
            self.EDIT_PRODUCT_BUTTON_LOCATOR,
            "Тестовый продукт (иконка карандаша)"
        )
        self.click_button(edit_product_button)
        logging.info("Редактирование тестового продукта (нажата иконка карандаша).")

    @allure.step("Удалить тестовый продукт (иконка корзины)")
    def remove_test_product(self):
        basket_icon = self.visibility_of_element_located(
            self.DELETE_PRODUCT_BUTTON_LOCATOR,
            "Тестовый продукт (иконка корзины)"
        )
        self.click_button(basket_icon)
        logging.info("Удаление тестового продукта (нажата иконка корзины).")
