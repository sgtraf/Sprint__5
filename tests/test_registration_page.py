import helper
import constant_data

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestRegistrationPage:

    def test_add_new_user_add_new_user_user_added(self, open_webdriver, close_webdriver):

        open_webdriver.get(constant_data.BASE_URL+constant_data.REGISTER)

        # Найди поле "Имя" и заполни его
        open_webdriver.find_element(*Locators.REG_NAME).send_keys(constant_data.NAME)

        # Найди поле "Email" и заполни его
        open_webdriver.find_element(*Locators.REG_EMAIL).send_keys(
            helper.generate_random_email())

        # Найди поле "Пароль" и заполни его
        open_webdriver.find_element(*Locators.REG_PASSWORD).send_keys(constant_data.PASSWORD_7)

        # Найди кнопку "Войти" и кликни по ней
        open_webdriver.find_element(*Locators.REG_ENTER).click()

        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Забыли пароль?")
        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/p[2]")))

        assert open_webdriver.find_element(*Locators.ENTER_FORGET_PASSWORD).text == 'Вход'
        close_webdriver

    def test_input_incorrect_password_add_incorrect_password_passord_error(self, open_webdriver, close_webdriver):

        open_webdriver.get(constant_data.BASE_URL+constant_data.REGISTER)

        # Найди поле "Имя" и заполни его
        open_webdriver.find_element(*Locators.REG_NAME).send_keys(constant_data.NAME)

        # Найди поле "Email" и заполни его
        open_webdriver.find_element(*Locators.REG_EMAIL).send_keys(
            helper.generate_random_email())

        # Найди поле "Пароль" и заполни его
        open_webdriver.find_element(*Locators.REG_PASSWORD).send_keys(constant_data.PASSWORD_5)

        # Найди кнопку "Войти" и кликни по ней
        open_webdriver.find_element(*Locators.REG_ENTER).click()

        # Проверь, что появление сообщения 'Некорректный пароль'
        assert open_webdriver.find_element(*Locators.POPUP_INCORRECT_PASSWORD).text == 'Некорректный пароль'

        close_webdriver
