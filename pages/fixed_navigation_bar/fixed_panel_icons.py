import logging

import allure
from selenium.webdriver.common.by import By

from utils.action_with_element import ActionWithElement


class FixedPanelIcons(ActionWithElement):
    MENU_LOCATOR = (
        By.XPATH,
        "//button[contains(@class, 'btn-light') and .//span[contains(text(), 'menu')]]"
    )
    SHOP_LOCATOR = (By.CSS_SELECTOR, "a.navbar-brand")
    SHOPPING_CART_LOCATOR = (
        By.XPATH,
        "//button[contains(@class, 'btn-light') and .//span[contains(text(), 'shopping_cart')]]"
    )

    @allure.step("Открыть меню")
    def open_menu(self):
        menu_button = self.visibility_of_element_located(self.MENU_LOCATOR, "Меню")
        self.click_button(menu_button)
        logging.info("Нажатие кнопки 'Меню'.")

    @allure.step("Нажать на 'Магазин'")
    def click_shop(self):
        shop_button = self.visibility_of_element_located(self.SHOP_LOCATOR, "Магазин")
        self.click_button(shop_button)
        logging.info("Нажатие на надпись 'Магазин'.")

    @allure.step("Нажать на корзину")
    def click_shopping_cart(self):
        shopping_cart_button = self.visibility_of_element_located(self.SHOPPING_CART_LOCATOR, "Корзина")
        self.click_button(shopping_cart_button)
        logging.info("Переход в продуктовую корзинку.")
