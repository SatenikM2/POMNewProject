from Sourse.Base.BasPage import BasePage
from Sourse.NavigationBar.SignIn.Navigation import NavigationBar
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartLocator():
    delFistProductLocator = (By.XPATH, "(//input[@data-action='delete'])[1]")
    shoppinglistTableLocator = (By.ID, "sc-active-cart")
    buttonInnerLocator = (By.XPATH, "(//span[@class='a-button-text a-declarative'])[1]")
    quantityProductLocator = (By.ID, "quantity_7")
    chooseFirstProductLocator = (By.XPATH, "(//img[@class='sc-product-image'])[1]")




class Cart(CartLocator, BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.navBarObject = NavigationBar(self.driver)


    def delete_first_product(self):
        delFirstProduct = self.driver.find_element(*(self.delFistProductLocator))
        delFirstProduct.click()


    def delete_all_products(self):
        while self.navBarObject.get_cart_products_count() > 0:
            self.delete_first_product()
            time.sleep(3)

    def choose_product_first(self):
        chooseProduct = self.driver.find_element(*(self.chooseFirstProductLocator))
        chooseProduct.click()


    def change_quantity_product(self):
        quantityProduct = self.driver.find_element(*(self.quantityProductLocator))
        quantityProduct.click()


    def validate_cart_page(self):
        assert self.element_should_be_visible(*(self.shoppinglistTableLocator)) == True




