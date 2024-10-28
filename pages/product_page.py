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
    

    