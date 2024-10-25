import pytest
from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import time

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
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
    
    
    

    