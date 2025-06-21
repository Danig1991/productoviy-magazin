from faker import Faker


# конфигурации

class Url:
    # базовый URL
    BASE_URL = "http://91.197.96.80/"


class AuthConfig:
    # учетная запись покупателя
    SHOPPER_LOGIN = "покупатель4"
    SHOPPER_PASSWORD = "покупатель4"

    # учетная запись администратора ADMIN
    ADMIN_LOGIN = "admin"
    ADMIN_PASSWORD = "admin"


class ProductData:
    # значения для нового продукта
    NAME = "Тестовый Пирожок Вишневый"
    DESCRIPTION = "Обжаренный во фритюре пирожок со сладкой начинкой из вишни 80 г"
    CATEGORY = "Пирожок"
    PRICE = 65
    NEW_PRICE = 70
    IMAGE_URL = "https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/521573545-pirogok-vishnevyj-600x600.webp"


class ProductConfig:
    # данные для действия с продуктом
    PRODUCT_NAME = "Бургер с курицей"
    QUANTITY_1 = 1
    QUANTITY_2 = 2
    QUANTITY_3 = 3
    QUANTITY_105 = 105
    QUANTITY_505 = 505


class FilterConfig:
    # значения для выпадающего меню
    SORT_BY_PRICE_LOW_TO_HIGH = "Цена: Сначала подешевле"
    SORT_BY_PRICE_HIGH_TO_LOW = "Цена: Сначала подороже"
    SORT_BY_NAME_A_TO_Z = "Наименование: от A до Я"
    SORT_BY_NAME_Z_TO_A = "Наименование: от Я до А"

    # значения для фильтра: категории
    BURGER = "Бургер"
    PIE = "Пирожок"
    ROLL = "Ролл"
    SANDWICH = "Сэндвич"

    # значения для фильтра: цена
    MIN_PRICE = 100
    MAX_PRICE = 150


class UserData:
    faker = Faker("ru_Ru")

    # имя
    def get_first_name(self):
        return self.faker.first_name_male()

    # фамилия
    def get_last_name(self):
        return self.faker.last_name_male()

    # отчество
    def get_middle_name(self):
        return self.faker.middle_name_male()

    # адрес доставки
    def get_address(self):
        return self.faker.street_address()

    # номер карты
    def get_card_number(self):
        return (f"{self.faker.random_number(digits=4, fix_len=True)} "
                f"{self.faker.random_number(digits=4, fix_len=True)} "
                f"{self.faker.random_number(digits=4, fix_len=True)} "
                f"{self.faker.random_number(digits=4, fix_len=True)}")

    # нечисловой номер карты
    def get_non_numeric_card_number(self):
        return (f"{self.faker.password(length=4, digits=False, upper_case=False)} "
                f"{self.faker.password(length=4, digits=False, upper_case=False)} "
                f"{self.faker.password(length=4, digits=False, upper_case=False)} "
                f"{self.faker.password(length=4, digits=False, upper_case=False)}")
