import logging

import allure
from selenium.webdriver.common.by import By

from utils.action_with_element import ActionWithElement


class Menu(ActionWithElement):
    EDIT_PRODUCTS_LOCATOR = (By.XPATH, "//a[@class='nav-link' and text()='Редактировать товары']")
    SHOP_IN_MENU_LOCATOR = (By.XPATH, "//a[contains(@class, 'nav-link') and text()='Магазин']")
    SHOPPING_CART_IN_MENU_LOCATOR = (By.XPATH, "//a[@class='nav-link' and text()='Корзинка']")
    EXIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn-danger")

    # "Редактировать товары" в меню
    def edit_products_in_menu(self):
        return self.visibility_of_element_located(self.EDIT_PRODUCTS_LOCATOR, "Редактировать товары")

    @allure.step("Нажать 'Редактировать товары' в меню")
    def click_edit_products_in_menu(self):
        self.click_button(self.edit_products_in_menu())
        logging.info("В меню выбран пункт 'Редактировать товары'.")

    # "Магазин" в меню
    def shop_in_menu(self):
        return self.visibility_of_element_located(self.SHOP_IN_MENU_LOCATOR, "Магазин")

    @allure.step("Нажать 'Магазин' в меню")
    def click_shop_in_menu(self):
        self.click_button(self.shop_in_menu())
        logging.info("В меню выбран пункт 'Магазин'.")

    # "Корзинка" в меню
    def shopping_cart_in_menu(self):
        return self.visibility_of_element_located(self.SHOPPING_CART_IN_MENU_LOCATOR, "Корзинка")

    @allure.step("Нажать 'Корзинка' в меню")
    def click_shopping_cart_in_menu(self):
        self.click_button(self.shopping_cart_in_menu())
        logging.info("В меню выбран пункт 'Корзинка'.")

    # кнопка "Выход" в меню
    def exit_button_in_menu(self):
        return self.visibility_of_element_located(self.EXIT_BUTTON_LOCATOR, "Выход")

    @allure.step("Нажать кнопку 'Выход'")
    def click_exit_button_in_menu(self):
        self.click_button(self.exit_button_in_menu())
        logging.info("Нажатие кнопки 'Выход' в меню.")
