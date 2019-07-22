from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        actual_url = self.browser.current_url
        assert "login" in actual_url, "url is not correct"

    def should_be_login_form(self):
        try:
            self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"
        except NoSuchElementException:
            assert False
        assert True

    def should_be_register_form(self):
        try:
            self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"
        except NoSuchElementException:
            assert False
        assert True

