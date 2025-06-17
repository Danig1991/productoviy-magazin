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
# CART_COUNTER_VALUE_LOCATOR = (By.CSS_SELECTOR, ".cart-counter")


class FixedPanelIcons(Expectation):

    # открыть меню
    def open_menu(self):
        self.visibility_of_element_located(MENU_LOCATOR, "Меню").click()
        print("Нажата кнопка \"Меню\".")

    # нажать на "Магазин"
    def click_shop(self):
        self.visibility_of_element_located(SHOP_LOCATOR, "Магазин").click()
        print("Нажатие на надпись \"Магазин\".")

    # нажать на корзину
    def click_shopping_cart(self):
        self.visibility_of_element_located(SHOPPING_CART_LOCATOR, "Корзина").click()
        print("Переход в продуктовую корзинку.")

    # # получить значение счетчика корзины
    # def get_cart_counter_value(self):
    #     cart_icon = self.visibility_of_element_located(CART_COUNTER_VALUE_LOCATOR, "Счетчик корзины")
    #     return int(cart_icon.text)
