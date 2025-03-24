from selenium.webdriver.common.by import By

class Locators:
    #Страница регистрации
    REG_NAME = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default']")
    REG_EMAIL = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default']/input[@class='text input__textfield text_type_main-default']")
    REG_PASSWORD = (By.XPATH, ".//input[@type='password']")
    REG_ENTER = (By.XPATH, ".//form/button")
    POPUP_INCORRECT_PASSWORD = (By.XPATH, ".//form/fieldset[3]/div/p")

    #надпись "Забыли пароль?" на странице входа
    ENTER_FORGET_PASSWORD = (By.XPATH, "/html/body/div/div/main/div/h2")
