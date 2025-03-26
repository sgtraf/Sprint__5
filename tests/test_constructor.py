import constant_data
from locators import Locators

class TestConstructor:
    def test_constructor_bulki_transfer_ok(self, open_close_webdriver):
        #открываем главную страницу
        #открываем вебдрайвер через фикстуру
        open_webdriver = open_close_webdriver
        open_webdriver.get(constant_data.BASE_URL)
        # иммитируем переход на раздел Булки
        open_webdriver.find_element(*Locators.SOUSE).click()
        open_webdriver.find_element(*Locators.BULKI).click()
        # Проверь, что текущий class родительского локатора div равен 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        assert open_webdriver.find_element(*Locators.PARENT_BULKI).get_attribute('class') == constant_data.CLASS_DIV
        #закрываем вебдрайвер через фикстуру
        open_close_webdriver

    def test_constructor_sousi_transfer_ok(self, open_close_webdriver):
        #открываем главную страницу
        #открываем вебдрайвер через фикстуру
        open_webdriver = open_close_webdriver
        open_webdriver.get(constant_data.BASE_URL)
        # иммитируем переход на раздел Соусы
        open_webdriver.find_element(*Locators.SOUSE).click()
        # Проверь, что текущий class div равен 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        assert open_webdriver.find_element(*Locators.PARENT_SOUSE).get_attribute('class') == constant_data.CLASS_DIV
        #закрываем вебдрайвер через фикстуру
        open_close_webdriver

    def test_constructor_nachinki_transfer_ok(self, open_close_webdriver):
        #открываем главную страницу
        #открываем вебдрайвер через фикстуру
        open_webdriver = open_close_webdriver
        open_webdriver.get(constant_data.BASE_URL)
        # иммитируем переход на раздел Начинки
        open_webdriver.find_element(*Locators.NACHINKI).click()
        # Проверь, что текущий class div равен 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        assert open_webdriver.find_element(*Locators.PARENT_NACHINKI).get_attribute('class') == constant_data.CLASS_DIV
        #закрываем вебдрайвер через фикстуру
        open_close_webdriver