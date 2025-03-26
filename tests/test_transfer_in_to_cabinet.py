import constant_data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestTransferToCabinet:
    def test_transfer_to_cabinet_transfer_ok(self, open_close_webdriver, enter_to_site):
        #открываем главную страницу и залогиниваемся через фикстуру, присваеваем переменной ссылку на объект webdraiver
        open_webdriver = enter_to_site
        # нажимаем на кнопку Личный Кабинет на странице
        open_webdriver.find_element(*Locators.BUTTON_LK_MP).click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "В этом разделе вы можете изменить свои персональные данные")
        WebDriverWait(open_webdriver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TEXT_LK)))

        # Проверь, что текущий url равен 'https://stellarburgers.nomoreparties.site/account/profile'
        assert open_webdriver.current_url == constant_data.PROFILE_URL
        #закрываем вебдрайвер через фикстуру
        open_close_webdriver

    def test_transfer_to_constructor_from_lk_transfer_ok(self, open_close_webdriver, enter_to_site):
        #открываем главную страницу и залогиниваемся через фикстуру, присваеваем переменной ссылку на объект webdraiver
        open_webdriver = enter_to_site
        # нажимаем на кнопку Личный Кабинет на странице
        open_webdriver.find_element(*Locators.BUTTON_LK_MP).click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "В этом разделе вы можете изменить свои персональные данные")
        WebDriverWait(open_webdriver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TEXT_LK)))
        # нажимаем на кнопку Конструктор на странице
        open_webdriver.find_element(*Locators.BUTTON_CONSTRUKTOR).click()

        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Соберите бургер")
        WebDriverWait(open_webdriver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Locators.TEXT_COMPLETE_BURGER)))

        # Проверь, что на странице есть текст 'Соберите бургер'
        assert open_webdriver.find_element(By.XPATH, Locators.TEXT_COMPLETE_BURGER).text == 'Соберите бургер'
        #закрываем вебдрайвер через фикстуру
        open_close_webdriver

    def test_transfer_to_constructor_from_logo_transfer_ok(self, open_close_webdriver, enter_to_site):
        #открываем главную страницу и залогиниваемся через фикстуру, присваеваем переменной ссылку на объект webdraiver
        open_webdriver = enter_to_site
        # нажимаем на кнопку Личный Кабинет на странице
        open_webdriver.find_element(*Locators.BUTTON_LK_MP).click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "В этом разделе вы можете изменить свои персональные данные")
        WebDriverWait(open_webdriver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TEXT_LK)))
        # нажимаем на Логотип на странице
        open_webdriver.find_element(*Locators.LOGO).click()

        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Соберите бургер")
        WebDriverWait(open_webdriver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Locators.TEXT_COMPLETE_BURGER)))

        # Проверь, что на странице есть текст 'Соберите бургер'
        assert open_webdriver.find_element(By.XPATH, Locators.TEXT_COMPLETE_BURGER).text == 'Соберите бургер'
        #закрываем вебдрайвер через фикстуру
        open_close_webdriver

    def test_logout_from_lk_logout_ok(self, open_close_webdriver, enter_to_site):
        #открываем главную страницу и залогиниваемся через фикстуру, присваеваем переменной ссылку на объект webdraiver
        open_webdriver = enter_to_site
        # нажимаем на кнопку Личный Кабинет на странице
        open_webdriver.find_element(*Locators.BUTTON_LK_MP).click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "В этом разделе вы можете изменить свои персональные данные")
        WebDriverWait(open_webdriver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.TEXT_LK)))
        # нажимаем на кнопку Выход на странице
        open_webdriver.find_element(*Locators.BUTTON_EXIT).click()

        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Вход")
        WebDriverWait(open_webdriver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Locators.LABEL_ENTER)))

        # Проверь, что на странице есть текст 'Вход'
        assert open_webdriver.find_element(By.XPATH, Locators.LABEL_ENTER).text == 'Вход'
        #закрываем вебдрайвер через фикстуру
        open_close_webdriver