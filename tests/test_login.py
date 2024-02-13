from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from locators import TestLocators
from data import TestData


class TestLogin:
    """Тесты проверки аутентификации"""

    def test_login_from_main_page_positive_result(self, driver):
        """Проверка логина при переходе из главной страницы"""

        driver.get(TestData.MAIN_URL)
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAINPAGE).click()
        driver.find_element(*TestLocators.EMAIL_LOGIN_FORM).send_keys(TestData.CREATED_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_LOGIN_FORM).send_keys(TestData.CREATED_PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_CREATE_ORDER))
        assert driver.find_element(*TestLocators.BUTTON_CREATE_ORDER).is_displayed()

    def test_login_from_personal_account_positive_result(self, driver):
        """Проверка логина при переходе из личного кабинета"""

        driver.get(TestData.MAIN_URL)
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL_LOGIN_FORM).send_keys(TestData.CREATED_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_LOGIN_FORM).send_keys(TestData.CREATED_PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_CREATE_ORDER))
        assert driver.find_element(*TestLocators.BUTTON_CREATE_ORDER).is_displayed()

    def test_login_from_registration_page_positive_result(self, driver):
        """Проверка логина при переходе со страницы регистрации"""

        driver.get(TestData.REGISTRATION_URL)
        driver.find_element(*TestLocators.BUTTON_LOGIN_REGPAGE).click()
        driver.find_element(*TestLocators.EMAIL_LOGIN_FORM).send_keys(TestData.CREATED_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_LOGIN_FORM).send_keys(TestData.CREATED_PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_CREATE_ORDER))
        assert driver.find_element(*TestLocators.BUTTON_CREATE_ORDER).is_displayed()

    def test_login_from_forgot_password_page_positive_result(self, driver):
        """Проверка логина при переходе со страницы восстановления пароля"""

        driver.get(TestData.FORGOT_PASS_URL)
        driver.find_element(*TestLocators.BUTTON_LOGIN_FORGOT_PAGE).click()
        driver.find_element(*TestLocators.EMAIL_LOGIN_FORM).send_keys(TestData.CREATED_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_LOGIN_FORM).send_keys(TestData.CREATED_PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_CREATE_ORDER))
        assert driver.find_element(*TestLocators.BUTTON_CREATE_ORDER).is_displayed()