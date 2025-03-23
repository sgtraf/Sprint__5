import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistrationPage:

    def test_add_new_user_add_new_user_user_added(self, generate_random_email):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Найди поле "Имя" и заполни его
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys("rtrtrt")

        # Найди поле "Email" и заполни его
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").send_keys(generate_random_email)

        # Найди поле "Пароль" и заполни его
        driver.find_element(By.XPATH, ".//form/fieldset[3]/div/div/input").send_keys("12345678")

        # Найди кнопку "Войти" и кликни по ней
        driver.find_element(By.XPATH, ".//form/button").click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//body/div/div/main/div/form/button")))
        print(driver.find_element(By.CLASS_NAME, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa").text)

        assert driver.find_element(By.XPATH, "/html/body/div/div/main/div/h2").text == 'Вход'

        driver.quit()

    def test_input_incorrect_password_add_incorrect_password_passord_error(self,generate_random_email):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Найди поле "Имя" и заполни его
        driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys("Миша")

        # Найди поле "Email" и заполни его
        driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").send_keys(generate_random_email)

        # Найди поле "Пароль" и заполни его
        driver.find_element(By.XPATH, ".//form/fieldset[3]/div/div/input").send_keys("12345")

        # Найди кнопку "Войти" и кликни по ней
        driver.find_element(By.XPATH, ".//form/button").click()

        # Проверь, что появление сообщения 'Некорректный пароль'
        assert driver.find_element(By.XPATH, ".//form/fieldset[3]/div/p").text == 'Некорректный пароль'

        driver.quit()
