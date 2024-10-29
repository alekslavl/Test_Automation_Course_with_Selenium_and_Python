from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес       
        assert "login" in self.browser.current_url, "Incorrect url address"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form"

    def should_be_register_form(self):
        #  проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "No registration form on the page"
    
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        
        
        