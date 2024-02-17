from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from locators import TestLocators
from data import TestData


class TestPersonalAccount:
    """Тесты страницы личного кабинета"""

    def test_authorized_user_go_to_account_page_positive_result(self, driver):
        """Проверка перехода в личный кабинет авторизованным юзером"""

        driver.get(TestData.MAIN_URL)
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAINPAGE).click()
        driver.find_element(*TestLocators.EMAIL_FORM).send_keys(TestData.CREATED_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_FORM).send_keys(TestData.CREATED_PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.ACCOUNT_PROFILE_TAB))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_unauthorized_user_go_to_account_page_redirect_login_page(self, driver):
        """Проверка перехода в личный кабинет неавторизованным юзером"""

        driver.get(TestData.MAIN_URL)
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        assert driver.find_element(*TestLocators.LOGO_LOGIN_PAGE).is_displayed()

    def test_go_to_constructor_from_personal_account_positive_result(self, driver):
        """Проверка перехода из личного кабинета в конструктор"""

        driver.get(TestData.LOGIN_URL)
        driver.find_element(*TestLocators.EMAIL_FORM).send_keys(TestData.CREATED_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_FORM).send_keys(TestData.CREATED_PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.ACCOUNT_PROFILE_TAB))
        driver.find_element(*TestLocators.HEADER_CONSTRUCTOR_TAB).click()
        assert driver.find_element(*TestLocators.LOGO_CREATE_BURGER).is_displayed()

    def test_go_to_main_page_from_personal_account_page(self, driver):
        """Проверка перехода из личного кабинета на главную страницу """

        driver.get(TestData.LOGIN_URL)
        driver.find_element(*TestLocators.EMAIL_FORM).send_keys(TestData.CREATED_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_FORM).send_keys(TestData.CREATED_PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.ACCOUNT_PROFILE_TAB))
        driver.find_element(*TestLocators.HEADER_MAIN_TAB).click()
        assert driver.find_element(*TestLocators.LOGO_CREATE_BURGER).is_displayed()

    def test_exit_from_account_positive_result(self, driver):
        """Проверка разлогина из личного кабинета"""

        driver.get(TestData.LOGIN_URL)
        driver.find_element(*TestLocators.EMAIL_FORM).send_keys(TestData.CREATED_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_FORM).send_keys(TestData.CREATED_PASSWORD)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.ACCOUNT_PROFILE_TAB))
        driver.find_element(*TestLocators.ACCOUNT_EXIT_TAB).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGO_LOGIN_PAGE))
        assert driver.find_element(*TestLocators.LOGO_LOGIN_PAGE).is_displayed()
