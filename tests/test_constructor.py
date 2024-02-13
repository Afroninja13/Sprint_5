from conftest import driver
from locators import TestLocators
from data import TestData


class TestConstructor:
    """Тесты переключения вкладок конструктора"""

    def test_chose_roll_menu_tab_displayed_rolls(self, driver):
        """Проверка переключения на вкладку Булки"""

        driver.get(TestData.MAIN_URL)
        if not driver.find_element(*TestLocators.ROLL_BUTTON_DIV).get_attribute('class').__contains__('current'):
            driver.find_element(*TestLocators.ROLL_BUTTON).click()
        assert driver.find_element(*TestLocators.ROLL_BUTTON_DIV).get_attribute('class').__contains__('current')

    def test_chose_sauses_menu_tab_displayed_sauses(self, driver):
        """Проверка переключения на вкладку Соусы"""

        driver.get(TestData.MAIN_URL)
        if not driver.find_element(*TestLocators.SAUSES_BUTTON_DIV).get_attribute('class').__contains__('current'):
            driver.find_element(*TestLocators.SAUSES_BUTTON).click()
        assert driver.find_element(*TestLocators.SAUSES_BUTTON_DIV).get_attribute('class').__contains__('current')

    def test_chose_fillings_menu_tab_displayed_fillings(self, driver):
        """Проверка переключения на вкладку Начинки"""

        driver.get(TestData.MAIN_URL)
        if not driver.find_element(*TestLocators.FILLINGS_BUTTON_DIV).get_attribute('class').__contains__('current'):
            driver.find_element(*TestLocators.FILLINGS_BUTTON).click()
        assert driver.find_element(*TestLocators.FILLINGS_BUTTON_DIV).get_attribute('class').__contains__('current')
