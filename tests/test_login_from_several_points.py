import constant_data

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestLoginPage:
    def test_enter_from_main_page_login_ok(self, open_webdriver, close_webdriver):
        open_webdriver.get(constant_data.BASE_URL)

        open_webdriver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()
        # Добавь явное ожидание для загрузки страницы (проверяем появление надписи "Забыли пароль?")
        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/p[2]")))
        open_webdriver.find_element(By.XPATH, "//div[label[contains(text(),'Email')]]//input").send_keys(constant_data.LOGIN)
        open_webdriver.find_element(By.XPATH, "//div[label[contains(text(),'Пароль')]]//input").send_keys(constant_data.PASSWORD)
        open_webdriver.find_element(*Locators.REG_ENTER).click()
        WebDriverWait(open_webdriver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/button[text()='Оформить заказ']")))

        assert open_webdriver.find_element(By.XPATH, "//div/button[text()='Оформить заказ']").text == 'Оформить заказ'

        close_webdriver

