import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by: By, value: str):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))

        except:
            print(f"Error 1:Element({by}, {value}) not visible")

        return element

    def git_title(self):
        return self.driver.title

    def element_should_be_visible(self, by: By, value: str):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))
            return True
        except:
            return False

    def send_keys(self, element, text):
        element.clear()
        element.send_keys(text)

    def wait_until_element_will_be_visibility(self, by: By, value: str):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))
            return element
        except:
            print('error1: Some text end error description')

    def screenshot(self):
        pass

    def press_an_hold(self, element, timeout =5):
        action = ActionChains(self.driver)
        action.click_and_hold(element)
        action.perform()
        time.sleep(5)
        action.release()

    def mouse_move(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()




