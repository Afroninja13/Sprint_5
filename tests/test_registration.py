from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from data import TestData
from helpers import random_char


class TestRegistration:
    """Тесты проверки регистрации"""

    def test_registration_with_valid_login_pass_positive_result(self, driver):
        """Проверка регистрации с валидными данными"""

        name = random_char()
        email = random_char()
        password = random_char()

        driver.get(TestData.REGISTRATION_URL)
        driver.find_element(*TestLocators.NAME_FORM).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_FORM).send_keys(email + '@ya.ru')
        driver.find_element(*TestLocators.PASSWORD_FORM).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_LOGIN))
        driver.find_element(*TestLocators.EMAIL_FORM).send_keys(email + '@ya.ru')
        driver.find_element(*TestLocators.PASSWORD_FORM).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGO_CREATE_BURGER))
        assert driver.find_element(*TestLocators.LOGO_CREATE_BURGER).is_displayed()

    def test_registration_with_invalid_password_return_error(self, driver):
        """Проверка ошибки валидации при не валидном значении пароля"""

        name = random_char()
        email = random_char()
        password = random_char()

        driver.get(TestData.REGISTRATION_URL)
        driver.find_element(*TestLocators.NAME_FORM).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_FORM).send_keys(email + '@ya.ru')
        driver.find_element(*TestLocators.PASSWORD_FORM).send_keys(password[:-1])
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        assert driver.find_element(*TestLocators.PASSWORD_ERROR_MESSAGE).is_displayed()
