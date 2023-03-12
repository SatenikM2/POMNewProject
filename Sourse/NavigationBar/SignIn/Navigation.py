from selenium.webdriver.common.by import By
from Sourse.Base.BasPage import BasePage


class NavigationBarLocator():
    SearchFieldELemenetLocator = (By.ID, "twotabsearchtextbox")
    searchButtonlOcator = (By.ID, "nav-search-submit-button")
    clickCartButtonLocator = (By.ID, "nav-cart-text-container")
    cartProductsCountLocator = (By.ID, "nav-cart-count")
    homePageLocator = (By.XPATH, "//a[@class='nav-logo-link nav-progressive-attribute']")
    buttonInnerLocator = (By.XPATH, "(//span[@class='a-button-text a-declarative'])[1]")





class NavigationBar(NavigationBarLocator, BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_search_field(self, text):
        searchFieldElement = self.driver.find_element(*(self.SearchFieldELemenetLocator))
        searchFieldElement.clear()
        searchFieldElement.send_keys(text)


    def click_to_search_button(self):
        searchButtonElement = self.driver.find_element(*(self.searchButtonlOcator))
        searchButtonElement.click()


    def click_to_cart_button(self):
        clickCartButton = self.driver.find_element(*(self.clickCartButtonLocator))
        clickCartButton.click()

    def get_cart_products_count(self):
        element = self.driver.find_element(*(self.cartProductsCountLocator))
        return int(element.text)

    def click_to_button_iner(self):
        clickiner = self.driver.find_element(*(self.buttonInnerLocator))
        clickiner.click()

    def click_to_second_button_iner(self):
        clickiner = self.driver.find_element(*(self.secondButtonInnerLocator))
        clickiner.click()


    def go_to_home_page(self):
        homePage = self.driver.find_element(*(self.homePageLocator))
        homePage.click()

