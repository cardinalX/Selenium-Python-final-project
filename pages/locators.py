from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

    INPUT_LOGIN_USERNAME = (By.ID, "id_login-username")
    INPUT_LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name=login_submit]")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")
