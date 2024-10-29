from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "There are products in the basket"
      
    def should_have_empty_message(self): 
        assert "empty" in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text, "Basket is not empty"  # Проверка наличия текста о пустой корзине
    