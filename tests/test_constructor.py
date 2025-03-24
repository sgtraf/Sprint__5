import time

import constant_data

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestConstructor:
    def test_constructor_bulki_transfer_ok(self, open_webdriver, close_webdriver):
        #открываем главную страницу
        #enter_to_site
        open_webdriver.get(constant_data.BASE_URL)
        # нажимаем на кнопку Личный Кабинет на странице
        open_webdriver.find_element(By.XPATH, "//span[text()='Соусы']").click()

        open_webdriver.find_element(By.XPATH, "//span[text()='Булки']").click()
        #time.sleep(5)
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "В этом разделе вы можете изменить свои персональные данные")
        #WebDriverWait(open_webdriver, 3).until(
         #   expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']")))

        # Проверь, что текущий class div равен 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        assert open_webdriver.find_element(By.XPATH, "//span[text()='Булки']/parent::div").get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

        close_webdriver