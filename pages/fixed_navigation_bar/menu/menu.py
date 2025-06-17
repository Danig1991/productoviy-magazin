from selenium.webdriver.common.by import By

from utils.expectation import Expectation

EDIT_PRODUCTS_LOCATOR = (By.XPATH, "//a[@class='nav-link' and text()='Редактировать товары']")
SHOP_IN_MENU_LOCATOR = (By.XPATH, "//a[contains(@class, 'nav-link') and text()='Магазин']")
SHOPPING_CART_IN_MENU_LOCATOR = (By.XPATH, "//a[@class='nav-link' and text()='Корзинка']")
EXIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn-danger")


class Menu(Expectation):

    # "Редактировать товары" в меню
    def edit_products_in_menu(self):
        return self.visibility_of_element_located(EDIT_PRODUCTS_LOCATOR, "Редактировать товары")

    # нажать "Редактировать товары" в меню
    def click_edit_products_in_menu(self):
        self.edit_products_in_menu().click()
        print("В меню выбран пункт \"Редактировать товары\".")

    # "Магазин" в меню
    def shop_in_menu(self):
        return self.visibility_of_element_located(SHOP_IN_MENU_LOCATOR, "Магазин")

    # нажать "Магазин" в меню
    def click_shop_in_menu(self):
        self.shop_in_menu().click()
        print("В меню выбран пункт \"Магазин\".")

    # "Корзинка" в меню
    def shopping_cart_in_menu(self):
        return self.visibility_of_element_located(SHOPPING_CART_IN_MENU_LOCATOR, "Корзинка")

    # нажать "Корзинка" в меню
    def click_shopping_cart_in_menu(self):
        self.shopping_cart_in_menu().click()
        print("В меню выбран пункт \"Корзинка\".")

    # кнопка "Выход" в меню
    def exit_button_in_menu(self):
        return self.visibility_of_element_located(EXIT_BUTTON_LOCATOR, "Выход")

    # нажать кнопку "Выход"
    def click_exit_button_in_menu(self):
        self.exit_button_in_menu().click()
        print("Нажата кнопка \"Выход\" в меню.")
