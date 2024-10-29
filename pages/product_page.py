from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        button.click()
    
    def get_success_message(self):
        # Получаем сообщение об успешном добавлении товара в корзину
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
    
    def get_product_name(self):
        # Получаем название товара
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text 
        
    def get_cart_price_message(self):
        # Получаем сообщение о стоимости корзины 
        return self.browser.find_element(*ProductPageLocators.CART_PRICE_MESSAGE).text
    
    def get_product_price(self):
        # Получаем цену товара
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_name_in_success_message(self):
        # Получаем название товара
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text

    def should_not_be_success_message(self):
        #Сообщения об успешном добвалении не должно быть
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"    
    
    def success_message_should_disappear(self):
        #Сообщение об успешном добавлении должно исчезнуть
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message not disapper, but should be"

    def should_not_be_product_in_basket(self):
        #В корзине не должно быть товара
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_BASKET), \
            "Product in basket, but should not be"

    def verify_success_message(self, product_name, product_price):
        success_message = self.get_success_message()
        cart_price_message = self.get_cart_price_message()
        product_name_in_success_message = self.get_product_name_in_success_message()

        assert "has been added to your basket." in success_message, \
            "Success message is incorrect"
        assert product_name == product_name_in_success_message, \
            "Product name in success message is incorrect"
        assert product_price in cart_price_message, \
            "Cart price message is incorrect"        
    

    