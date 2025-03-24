import constant_data

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestTransferToCabinet:
    def test_transder_to_cabinet_transfer_ok(self, open_webdriver, close_webdriver, enter_to_site):
        #открываем главную страницу
        enter_to_site
        # нажимаем на кнопку Личный Кабинет на странице
        open_webdriver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "В этом разделе вы можете изменить свои персональные данные")
        WebDriverWait(open_webdriver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']")))

        # Проверь, что текущий url равен 'https://stellarburgers.nomoreparties.site/account/profile'
        assert open_webdriver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        close_webdriver

    def test_transder_to_constructor_from_lk_transfer_ok(self, open_webdriver, close_webdriver, enter_to_site):
        #открываем главную страницу
        enter_to_site
        # нажимаем на кнопку Личный Кабинет на странице
        open_webdriver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "В этом разделе вы можете изменить свои персональные данные")
        WebDriverWait(open_webdriver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']")))
        # нажимаем на кнопку Конструктор на странице
        open_webdriver.find_element(By.XPATH, "//p[text()='Конструктор']").click()

        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "В этом разделе вы можете изменить свои персональные данные")
        WebDriverWait(open_webdriver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//h1[text()='Соберите бургер']")))

        # Проверь, что текущий url равен 'https://stellarburgers.nomoreparties.site/account/profile'
        assert open_webdriver.find_element(By.XPATH, "//h1[text()='Соберите бургер']").text == 'Соберите бургер'

        close_webdriver