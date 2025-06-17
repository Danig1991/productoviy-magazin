# Данные пользователя
from faker import Faker

faker = Faker("ru_Ru")

# имя
FIRST_NAME = faker.first_name_male()
# фамилия
LAST_NAME = faker.last_name_male()
# отчество
MIDDLE_NAME = faker.middle_name_male()
# адрес доставки
ADDRESS = faker.street_address()
# номер карты
CARD_NUMBER = (f"{faker.random_number(digits=4, fix_len=True)} "
               f"{faker.random_number(digits=4, fix_len=True)} "
               f"{faker.random_number(digits=4, fix_len=True)} "
               f"{faker.random_number(digits=4, fix_len=True)}")
# нечисловой номер карты
NON_NUMERIC_CARD_NUMBER = (f"{faker.password(length=4, digits=False, upper_case=False)} "
                           f"{faker.password(length=4, digits=False, upper_case=False)} "
                           f"{faker.password(length=4, digits=False, upper_case=False)} "
                           f"{faker.password(length=4, digits=False, upper_case=False)}")
