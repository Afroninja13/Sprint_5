from selenium.webdriver.common.by import By


class TestLocators:
    NAME_FORM = By.XPATH, '//label[contains(text(), "Имя")]/following-sibling::input[@name="name"]'  # Поле Name в форме регистрации
    EMAIL_FORM = By.XPATH, '//label[contains(text(), "Email")]/following-sibling::input[@name="name"]'  # Поле Email в форме регистрации
    PASSWORD_FORM = By.XPATH, '//label[contains(text(), "Пароль")]/following-sibling::input[@name="Пароль"]'  # Поле Password в форме регистрации
    BUTTON_REGISTRATION = By.XPATH, './/button[text()="Зарегистрироваться"]'  # Кнопка регистрации
    PASSWORD_ERROR_MESSAGE = By.XPATH, './/p[@class="input__error text_type_main-default"]'  # Сообщение ошибки валидации пароля

    LOGO_LOGIN_PAGE = By.XPATH, './/h2[text()="Вход"]'  # Логотип страницы логина
    BUTTON_LOGIN_MAINPAGE = By.XPATH, './/button[text()="Войти в аккаунт"]'  # Кнопка авторизации на главной странице
    BUTTON_LOGIN = By.XPATH, './/button[text()="Войти"]'  # Кнопка авторизации на странице авторизации
    BUTTON_CREATE_ORDER = By.XPATH, './/button[text()="Оформить заказ"]'  # Кнопка оформления заказа на главной странице
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, './/p[text()="Личный Кабинет"]'  # Кнопка перехода в личный кабинет
    BUTTON_LOGIN_REGPAGE = By.XPATH, './/a[text()="Войти"]'  # Кнопка авторизации на странице регистрации
    BUTTON_LOGIN_FORGOT_PAGE = By.XPATH, './/a[text()="Войти"]'  # Кнопка авторизации на странице восстановления пароля

    LOGO_CREATE_BURGER = By.XPATH, './/h1[text()="Соберите бургер"]'  # Логотип на главной странице
    ACCOUNT_PROFILE_TAB = By.XPATH, './/a[text()="Профиль"]'  # Вкладка Профиль в личном кабинете
    ACCOUNT_EXIT_TAB = By.XPATH, './/button[text()="Выход"]'  # Вкладка разлогина в личном кабинете

    HEADER_CONSTRUCTOR_TAB = By.XPATH, './/p[text()="Конструктор"]'  # Кнопка Конструктор в шапке сайта
    HEADER_MAIN_TAB = By.XPATH, '//div[contains(@class, "AppHeader_header__logo")]'  # Кнопка главной страницы в шапке сайта

    ROLL_BUTTON = By.XPATH, '//span[text()="Булки"]'  # Вкладка Булки в конструкторе
    ROLL_BUTTON_DIV = By.XPATH, '//span[text()="Булки"]//parent::div'  # Локатор для определения выбранной вкладки Булки
    SAUSES_BUTTON = By.XPATH, '//span[text()="Соусы"]'  # Вкладка Соусы в конструкторе
    SAUSES_BUTTON_DIV = By.XPATH, '//span[text()="Соусы"]//parent::div'  # Локатор для определения выбранной вкладки Соусы
    FILLINGS_BUTTON = By.XPATH, '//span[text()="Начинки"]'  # Вкладка Начинки в конструкторе
    FILLINGS_BUTTON_DIV = By.XPATH, '//span[text()="Начинки"]//parent::div' # Локатор для определения выбранной вкладки Начинки