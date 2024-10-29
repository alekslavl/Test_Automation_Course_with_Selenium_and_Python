import pytest
from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import time
from .pages.basket_page import BasketPage

'''@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link}"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    
    # Получаем название и цену товара
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    # Добавляем товар в корзину
    page.add_to_basket()
    # Получаем код
    page.solve_quiz_and_get_code()
    
    # Получаем сообщение об успешном добавлении товара и сообщение о стоимости корзины
    success_message = page.get_success_message()
    cart_price_message = page.get_cart_price_message()
    product_name_in_success_message = page.get_product_name_in_success_message()
    
    time.sleep(1)
    
    # Проверяем результаты
    assert "has been added to your basket." in success_message #The shellcoder's handbook has been added to your basket.
    assert product_name == product_name_in_success_message
    assert product_price in cart_price_message
    
@pytest.mark.xfail # Заранее помечаем, что тест упадет
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    
    # Добавляем товар в корзину
    page.add_to_basket()
    
    # Получаем сообщение об успешном добавлении товара
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    
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
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()'''
    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/" 
    product_page = ProductPage(browser, link)
    product_page.open()                                     #1. Гость открывает страницу товара
    
    # Добавляем товар в корзину
    #product_page.add_to_basket()
    
    product_page.go_to_basket()                             #2. Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()           #3. Ожидаем, что в корзине нет товаров
    # Получаем сообщение, что корзина пустая
    empty_message = product_page.get_empty_message() 
    assert "empty" in empty_message, "Basket is not empty"  #4. Ожидаем, что есть текст о том что корзина пуста
    
    
    

    