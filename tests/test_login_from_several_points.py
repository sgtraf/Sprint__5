import constant_data

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
import time

class TestLoginPage:
    def test_enter_from_main_page_login_ok(self, open_webdriver, close_webdriver):
        #открываем главную страницу
        open_webdriver.get(constant_data.BASE_URL)
        #нажимаем на кнопку Войти на главной странице
        open_webdriver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Забыли пароль?")
        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/p[2]")))
        #Заполняем поля своим логином и паролем
        open_webdriver.find_element(By.XPATH, "//div[label[contains(text(),'Email')]]//input").send_keys(constant_data.LOGIN)
        open_webdriver.find_element(By.XPATH, "//div[label[contains(text(),'Пароль')]]//input").send_keys(constant_data.PASSWORD)
        open_webdriver.find_element(*Locators.REG_ENTER).click()

        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Оформить заказ" на кнопке)

        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/button[text()='Оформить заказ']")))

        assert open_webdriver.find_element(By.XPATH, "//div/button[text()='Оформить заказ']").text == 'Оформить заказ'

        close_webdriver

    def test_enter_from_cabinet_login_ok(self, open_webdriver, close_webdriver):
        #открываем главную страницу
        open_webdriver.get(constant_data.BASE_URL)
        #нажимаем на кнопку Личный Кабинет на странице
        open_webdriver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Забыли пароль?")
        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/p[2]")))
        #Заполняем поля своим логином и паролем
        open_webdriver.find_element(By.XPATH, "//div[label[contains(text(),'Email')]]//input").send_keys(constant_data.LOGIN)
        open_webdriver.find_element(By.XPATH, "//div[label[contains(text(),'Пароль')]]//input").send_keys(constant_data.PASSWORD)
        open_webdriver.find_element(*Locators.REG_ENTER).click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Оформить заказ" на кнопке)

        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/button[text()='Оформить заказ']")))

        assert open_webdriver.find_element(By.XPATH, "//div/button[text()='Оформить заказ']").text == 'Оформить заказ'

        close_webdriver

    def test_enter_throw_buton_reg_page_login_ok(self, open_webdriver, close_webdriver):
        #открываем главную страницу
        open_webdriver.get(constant_data.BASE_URL+constant_data.REGISTER)
        #нажимаем на кнопку Войти на странице
        open_webdriver.find_element(By.XPATH, "//a[text()='Войти']").click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Забыли пароль?")
        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/p[2]")))
        #Заполняем поля своим логином и паролем
        open_webdriver.find_element(By.XPATH, "//div[label[contains(text(),'Email')]]//input").send_keys(constant_data.LOGIN)
        open_webdriver.find_element(By.XPATH, "//div[label[contains(text(),'Пароль')]]//input").send_keys(constant_data.PASSWORD)
        open_webdriver.find_element(*Locators.REG_ENTER).click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Оформить заказ" на кнопке)

        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/button[text()='Оформить заказ']")))

        assert open_webdriver.find_element(By.XPATH, "//div/button[text()='Оформить заказ']").text == 'Оформить заказ'

        close_webdriver

    def test_enter_throw_buton_forgot_password_login_ok(self, open_webdriver, close_webdriver):
        #открываем главную страницу
        open_webdriver.get(constant_data.BASE_URL+constant_data.FORGOT_PASSWORD_URL)
        #нажимаем на кнопку Войти на странице
        open_webdriver.find_element(By.XPATH, "//a[text()='Войти']").click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Забыли пароль?")
        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/p[2]")))
        #Заполняем поля своим логином и паролем
        open_webdriver.find_element(By.XPATH, "//div[label[contains(text(),'Email')]]//input").send_keys(constant_data.LOGIN)
        open_webdriver.find_element(By.XPATH, "//div[label[contains(text(),'Пароль')]]//input").send_keys(constant_data.PASSWORD)
        open_webdriver.find_element(*Locators.REG_ENTER).click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Оформить заказ" на кнопке)

        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/button[text()='Оформить заказ']")))

        assert open_webdriver.find_element(By.XPATH, "//div/button[text()='Оформить заказ']").text == 'Оформить заказ'

        close_webdriver