import time

import constant_data

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestConstructor:
    def test_constructor_bulki_transfer_ok(self, open_webdriver, close_webdriver):
        #открываем главную страницу
        open_webdriver.get(constant_data.BASE_URL)
        # иммитируем переход на раздел Булки
        open_webdriver.find_element(By.XPATH, "//span[text()='Соусы']").click()
        open_webdriver.find_element(By.XPATH, "//span[text()='Булки']").click()
        # Проверь, что текущий class div равен 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        assert open_webdriver.find_element(By.XPATH, "//span[text()='Булки']/parent::div").get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        close_webdriver

    def test_constructor_sousi_transfer_ok(self, open_webdriver, close_webdriver):
        #открываем главную страницу
        open_webdriver.get(constant_data.BASE_URL)
        # иммитируем переход на раздел Булки
        open_webdriver.find_element(By.XPATH, "//span[text()='Соусы']").click()
        # Проверь, что текущий class div равен 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        assert open_webdriver.find_element(By.XPATH, "//span[text()='Соусы']/parent::div").get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        close_webdriver

    def test_constructor_nachinki_transfer_ok(self, open_webdriver, close_webdriver):
        #открываем главную страницу
        open_webdriver.get(constant_data.BASE_URL)
        # иммитируем переход на раздел Булки
        open_webdriver.find_element(By.XPATH, "//span[text()='Начинки']").click()
        # Проверь, что текущий class div равен 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        assert open_webdriver.find_element(By.XPATH, "//span[text()='Начинки']/parent::div").get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        close_webdriver