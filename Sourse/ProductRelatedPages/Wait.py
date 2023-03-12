from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class CustomFind():
    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_should_be_visible(self, by: By, value: str):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))
            return element
        except:
            print('error1: Some text end error description')
