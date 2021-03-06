"""
3.5 PyTest - маркировка
Для маркировки теста нужно написать декоратор вида @pytest.mark.mark_name, где mark_name - произвольная строка.

"""
# Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:
# pytest -s -v -m smoke test_fixture8.py


# Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду:
# pytest -s -v -m "not smoke" test_fixture8.py


# Запустим smoke и regression-тесты:
# pytest -s -v -m "smoke or regression" test_fixture8.py


# Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И:
# pytest -s -v -m "smoke and win10" test_fixture81.py


# Итак, чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip



import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = WebDriver('/home/hor/ChromeDriver/chromedriver')
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    @pytest.mark.win10
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

