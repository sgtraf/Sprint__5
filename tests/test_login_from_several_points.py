import constant_data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestLoginFrom:
    def test_enter_from_main_page_login_ok(self, open_close_webdriver):
        #открываем главную страницу
        #открываем вебдрайвер через фикстуру
        open_webdriver = open_close_webdriver
        open_webdriver.get(constant_data.BASE_URL)
        #нажимаем на кнопку Войти на главной странице
        open_webdriver.find_element(*Locators.BT_ENTER).click()

        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Забыли пароль?")
        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.TEXT_FORGGOT_PASS_LP)))
        #Заполняем поля своим логином и паролем
        open_webdriver.find_element(*Locators.INPUT_EMAIL).send_keys(constant_data.LOGIN)
        open_webdriver.find_element(*Locators.INPUT_PASSW).send_keys(constant_data.PASSWORD)
        open_webdriver.find_element(*Locators.REG_ENTER).click()

        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Оформить заказ" на кнопке)

        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.TAKE_ORDER_TEXT)))

        assert open_webdriver.find_element(By.XPATH, Locators.TAKE_ORDER_TEXT).text == 'Оформить заказ'

    def test_enter_from_cabinet_login_ok(self, open_close_webdriver):
        #открываем главную страницу
        #открываем вебдрайвер через фикстуру
        open_webdriver = open_close_webdriver
        open_webdriver.get(constant_data.BASE_URL)
        #нажимаем на кнопку Личный Кабинет на странице
        open_webdriver.find_element(*Locators.LK_TEXT).click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Забыли пароль?")
        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.TEXT_FORGGOT_PASS_LP)))
        #Заполняем поля своим логином и паролем
        open_webdriver.find_element(*Locators.INPUT_EMAIL).send_keys(constant_data.LOGIN)
        open_webdriver.find_element(*Locators.INPUT_PASSW).send_keys(constant_data.PASSWORD)
        open_webdriver.find_element(*Locators.REG_ENTER).click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Оформить заказ" на кнопке)

        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.TAKE_ORDER_TEXT)))

        assert open_webdriver.find_element(By.XPATH, Locators.TAKE_ORDER_TEXT).text == 'Оформить заказ'

    def test_enter_throw_buton_reg_page_login_ok(self, open_close_webdriver):
        #открываем страницу регистрации
        #открываем вебдрайвер через фикстуру
        open_webdriver = open_close_webdriver
        open_webdriver.get(constant_data.BASE_URL+constant_data.REGISTER)
        #нажимаем на кнопку Войти на странице
        open_webdriver.find_element(*Locators.BT_ENTER_REG).click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Забыли пароль?")
        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.TEXT_FORGGOT_PASS_LP)))
        #Заполняем поля своим логином и паролем
        open_webdriver.find_element(*Locators.INPUT_EMAIL).send_keys(constant_data.LOGIN)
        open_webdriver.find_element(*Locators.INPUT_PASSW).send_keys(constant_data.PASSWORD)
        open_webdriver.find_element(*Locators.REG_ENTER).click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Оформить заказ" на кнопке)

        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.TAKE_ORDER_TEXT)))

        assert open_webdriver.find_element(By.XPATH, Locators.TAKE_ORDER_TEXT).text == 'Оформить заказ'

    def test_enter_throw_buton_forgot_password_login_ok(self, open_close_webdriver):
        #открываем главную страницу
        #открываем вебдрайвер через фикстуру
        open_webdriver = open_close_webdriver
        open_webdriver.get(constant_data.BASE_URL+constant_data.FORGOT_PASSWORD_URL)
        #нажимаем на кнопку Войти на странице
        open_webdriver.find_element(*Locators.BT_ENTER_FP).click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Забыли пароль?")
        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.TEXT_FORGGOT_PASS_LP)))
        #Заполняем поля своим логином и паролем
        open_webdriver.find_element(*Locators.INPUT_EMAIL).send_keys(constant_data.LOGIN)
        open_webdriver.find_element(*Locators.INPUT_PASSW).send_keys(constant_data.PASSWORD)
        open_webdriver.find_element(*Locators.REG_ENTER).click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Оформить заказ" на кнопке)

        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.TAKE_ORDER_TEXT)))

        assert open_webdriver.find_element(By.XPATH, Locators.TAKE_ORDER_TEXT).text == 'Оформить заказ'
