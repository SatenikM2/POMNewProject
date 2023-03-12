import time

from selenium import webdriver
import unittest
from Sourse.NavigationBar.SignIn.SignInPage import SignInPage
from Sourse.NavigationBar.SignIn.Navigation import NavigationBar
from Sourse.NavigationBar.SignIn.CartPage import Cart


class MyNewTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        self.signInPageObject = SignInPage(self.driver)
        self.navigationBarObject = NavigationBar(self.driver)
        self.cartObject = Cart(self.driver)


    def test_delete_first_product(self):
        self.signInPageObject.fill_Login_Field("SatMartirosyan0@gmail.com")
        self.signInPageObject.click_to_continue_button()
        time.sleep(5)
        self.signInPageObject.fill_password_field("Sat454649")
        self.signInPageObject.click_to_sign_in_button()
        time.sleep(3)
        self.navigationBarObject.click_to_cart_button()
        self.cartObject.validate_cart_page()
        time.sleep(2)
        self.navigationBarObject.click_to_button_iner()
        time.sleep(4)
        self.cartObject.change_quantity_product()
        time.sleep(3)
        self.navigationBarObject.go_to_home_page()
        time.sleep(3)








    def tearDown(self) -> None:
        self.driver.close()