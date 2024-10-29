from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, ".basket-items")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")            # Селектор для поля email
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")   # Селектор для поля пароля
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")  # Селектор для кнопки регистрации
    
class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    CART_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE =(By.CSS_SELECTOR, ".alertinner strong")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")