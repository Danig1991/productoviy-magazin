import allure
from selenium.webdriver.common.by import By

from utils.expectation import Expectation

NAME_LOCATOR = (By.XPATH, "//input[@placeholder='Наименование']")
DESCRIPTION_LOCATOR = (By.XPATH, "//input[@placeholder='Описание']")
CATEGORY_LOCATOR = (By.XPATH, "//input[@placeholder='Ожидаемая категория']")
PRICE_LOCATOR = (By.XPATH, "//input[@placeholder='Цена']")
IMAGE_URL_LOCATOR = (By.XPATH, "//input[@placeholder='Image Source']")
BUTTON_BACK_TO_PRODUCTS_LOCATOR = (By.XPATH, "//button[contains(text(), 'Обратно к товарам')]")
BUTTON_CREATE_PRODUCT_LOCATOR = (By.XPATH, "//button[contains(text(), 'Создать товар')]")


class AddProductPage(Expectation):

    @allure.step("Добавить наименование")
    def add_name(self, name):
        self.visibility_of_element_located(NAME_LOCATOR, "Наименование").send_keys(name)
        print(f"Добавлено наименование '{name}'")

    @allure.step("Добавить описание")
    def add_description(self, description):
        self.visibility_of_element_located(DESCRIPTION_LOCATOR, "Описание").send_keys(description)
        print(f"Добавлено описание '{description}'")

    @allure.step("Добавить категорию")
    def add_category(self, category):
        self.visibility_of_element_located(CATEGORY_LOCATOR, "Ожидаемая категория").send_keys(category)
        print(f"Добавлена ожидаемая категория '{category}'")

    @allure.step("Добавить цену")
    def add_price(self, price):
        self.visibility_of_element_located(PRICE_LOCATOR, "Цена").send_keys(price)
        print(f"Добавлена цена '{price}'р.")

    @allure.step("Добавить URL картинки")
    def add_image_url(self, image_url):
        self.visibility_of_element_located(IMAGE_URL_LOCATOR, "URL картинки").send_keys(image_url)
        print(f"Добавлено URL картинки '{image_url}'")

    @allure.step("Нажать кнопку 'Обратно к товарам'")
    def click_button_back_to_products(self):
        button_back_to_products = self.visibility_of_element_located(
            BUTTON_BACK_TO_PRODUCTS_LOCATOR,
            "Обратно к товарам"
        )
        self.move_to_element(button_back_to_products)
        button_back_to_products.click()
        print("Нажата кнопка 'Обратно к товарам'.")

    # кнопка "Создать товар"
    def button_create_product(self):
        button_create_product = self.visibility_of_element_located(
            BUTTON_CREATE_PRODUCT_LOCATOR,
            "Создать товар"
        )
        self.move_to_element(button_create_product)
        return button_create_product

    @allure.step("Нажать кнопку 'Создать товар'")
    def click_button_create_product(self):
        self.button_create_product().click()
        print("Нажата кнопка 'Создать товар'.")
