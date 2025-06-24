import allure
from selenium.webdriver.common.by import By

from utils.expectation import Expectation

LOGIN_LOCATOR = (By.XPATH, "//input[@placeholder='Логин']")
PASSWORD_LOCATOR = (By.XPATH, "//input[@placeholder='Пароль']")
LOGIN_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn")
TITLE_AUTHORIZATION_LOCATOR = (By.CSS_SELECTOR, ".fs-2")


class AuthorizationPage(Expectation):

    @allure.step("Ввод логина.")
    def enter_login(self, login=None):
        if not login:
            print("Логин не введен!")
        else:
            self.visibility_of_element_located(LOGIN_LOCATOR, "Логин").send_keys(login)
            print(f"Введен логин: {login}")

    @allure.step("Ввод пароля")
    def enter_password(self, password=None):
        if not password:
            print("Пароль не введен!")
        else:
            self.visibility_of_element_located(PASSWORD_LOCATOR, "Пароль").send_keys(password)
            print(f"Введен пароль: {password}")

    @allure.step("Нажать кнопку 'Войти'")
    def click_the_login_button(self):
        self.visibility_of_element_located(LOGIN_BUTTON_LOCATOR, "Войти").click()
        print("Нажата кнопка 'Ввод'.")

    @allure.step("Получить заголовок 'Авторизация'")
    def title_authorization(self):
        return self.visibility_of_element_located(TITLE_AUTHORIZATION_LOCATOR, "Авторизация").text
