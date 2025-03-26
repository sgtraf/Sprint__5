import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import constant_data
from locators import Locators

@pytest.fixture
#вход по существующему логину
def enter_to_site(open_close_webdriver):
    # открываем главную страницу
    open_webdriver = open_close_webdriver
    open_webdriver.get(constant_data.BASE_URL)
    # нажимаем на кнопку Войти на главной странице
    open_webdriver.find_element(*Locators.BT_ENTER).click()

    # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Забыли пароль?")
    WebDriverWait(open_webdriver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.TEXT_FORGGOT_PASS_LP)))
    # Заполняем поля своим логином и паролем
    open_webdriver.find_element(*Locators.INPUT_EMAIL).send_keys(
        constant_data.LOGIN)
    open_webdriver.find_element(*Locators.INPUT_PASSW).send_keys(
        constant_data.PASSWORD)
    open_webdriver.find_element(*Locators.REG_ENTER).click()
    return open_webdriver

@pytest.fixture
#открывает и закрывает вебдрайвер
def open_close_webdriver():
    wd_webdriver = webdriver.Chrome()
    yield wd_webdriver
    wd_webdriver.quit()

