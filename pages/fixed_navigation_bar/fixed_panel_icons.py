import allure
from selenium.webdriver.common.by import By

from utils.expectation import Expectation

MENU_LOCATOR = (
    By.XPATH,
    "//button[contains(@class, 'btn-light') and .//span[contains(text(), 'menu')]]"
)
SHOP_LOCATOR = (By.CSS_SELECTOR, "a.navbar-brand")
SHOPPING_CART_LOCATOR = (
    By.XPATH,
    "//button[contains(@class, 'btn-light') and .//span[contains(text(), 'shopping_cart')]]"
)


class FixedPanelIcons(Expectation):

    @allure.step("Открыть меню")
    def open_menu(self):
        self.visibility_of_element_located(MENU_LOCATOR, "Меню").click()
        print("Нажата кнопка 'Меню'.")

    @allure.step("Нажать на 'Магазин'")
    def click_shop(self):
        self.visibility_of_element_located(SHOP_LOCATOR, "Магазин").click()
        print("Нажатие на надпись 'Магазин'.")

    @allure.step("Нажать на корзину")
    def click_shopping_cart(self):
        self.visibility_of_element_located(SHOPPING_CART_LOCATOR, "Корзина").click()
        print("Переход в продуктовую корзинку.")
