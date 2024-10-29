from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

'''def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()          # выполняем метод страницы — переходим на страницу логина
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()'''
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()         # 1. Гость открывает главную страницу
    main_page.go_to_basket() # 2. Переходит в корзину по кнопке в шапке сайта
    
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket() #3. Ожидаем, что в корзине нет товаров
    
    # Получаем сообщение, что корзина пустая
    empty_message = basket_page.get_empty_message()
    #basket_page.should_be_empty_basket_message()  #4. Ожидаем, что есть текст о том что корзина пуста 
    assert "empty" in empty_message, "Basket is not empty"

    

    