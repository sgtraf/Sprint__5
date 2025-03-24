import pytest
from selenium import webdriver


@pytest.fixture
#открывает вебдрайвер
def open_webdriver():
    open_webdriver = webdriver.Chrome()
    return open_webdriver

@pytest.fixture
#открывает вебдрайвер
def close_webdriver(open_webdriver):
    open_webdriver.quit
