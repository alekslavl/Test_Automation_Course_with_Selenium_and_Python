import pytest
from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import time
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
    
@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Открываем страницу регистрации
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        
        # Генерируем email и регистрируем нового пользователя
        email = str(time.time()) + "@fakemail.org"
        password = "TestPassword123"
        page.register_new_user(email, password)
        
        # Проверяем, что пользователь залогинен
        base_page = BasePage(browser, browser.current_url)
        base_page.should_be_authorized_user()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                         # открываем страницу
    
        # Получаем название и цену товара
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        
        # Добавляем товар в корзину
        page.add_to_basket()
        
        # Получаем код
        page.solve_quiz_and_get_code()
    
        # Проверяем результаты с использованием методов класса
        page.verify_success_message(product_name, product_price)
    
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                         # открываем страницу
    
        # Получаем сообщение об успешном добавлении товара
        page.should_not_be_success_message()
           
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                         # открываем страницу
    
        # Получаем название и цену товара
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        
        # Добавляем товар в корзину
        page.add_to_basket()
        
        # Получаем код
        page.solve_quiz_and_get_code()
    
        # Проверяем результаты с использованием методов класса
        page.verify_success_message(product_name, product_price)

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/" 
    product_page = ProductPage(browser, link)
    product_page.open()                                      #1. Гость открывает страницу товара
    
    product_page.go_to_basket()                              #2. Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)
    
    basket_page.should_not_be_products_in_basket()           #3. Ожидаем, что в корзине нет товаров
        
    basket_page.should_have_empty_message()                  #4. Ожидаем, что есть текст о том что корзина пуста

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail # Заранее помечаем, что тест упадет
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    
    # Добавляем товар в корзину
    page.add_to_basket()
    
    # Получаем сообщение об успешном добавлении товара
    page.should_not_be_success_message()
    
@pytest.mark.xfail #Заранее помечаем, что тест упадет
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    
    # Добавляем товар в корзину
    page.add_to_basket()
    
    #Проверяем, что сообщение об успешном добавлении товара исчезло
    page.success_message_should_disappear()

#Гость может перейти на страницу логина со страницы Х
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    

    

    

    
    
    

    