from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# действие
class ActionWithElement:

    def __init__(self, driver):
        self._driver = driver

    # видимость элемента
    def visibility_of_element_located(self, locator, element):
        return WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(locator),
            message=f"Не найден искомый элемент \"{element}\"!"
        )

    # видимость всех элементов
    def visibility_of_all_elements_located(self, locator, element):
        return WebDriverWait(self._driver, 10).until(
            EC.visibility_of_all_elements_located(locator),
            message=f"Не найден искомый элемент \"{element}\"!"
        )

    # поиск элемента без ожидания
    def find_element(self, type_locator, value_locator):
        return self._driver.find_element(type_locator, value_locator)

    # поиск элементов без ожидания
    def find_elements(self, type_locator, value_locator):
        return self._driver.find_elements(type_locator, value_locator)

    # перейти к элементу
    def move_to_element(self, necessary_element):
        return ActionChains(self._driver).move_to_element(necessary_element).perform()

    # нажать кнопку
    def click_button(self, button):
        self.move_to_element(button)
        button.click()
