from selenium.webdriver.support.events import AbstractEventListener

class EventListeners(AbstractEventListener):
    def before_navigate_to(self, url: str, driver) -> None:
        print(f"before_navigate_to{url}")

    def after_navigate_to(self, url: str, driver) -> None:
        print(f"after_navigate_to %s" % url)

    def before_navigate_back(self, driver) -> None:
        print(" before_navigate_back")

    def after_navigate_back(self, driver) -> None:
        print("after_navigate_back")

    def before_navigate_forward(self, driver) -> None:
        print("before_navigate_forward")

    def before_find(self, by, value, driver) -> None:
        pass

    def after_find(self, by, value, driver) -> None:
        pass

    def before_click(self, element, driver) -> None:
        pass

    def after_click(self, element, driver) -> None:
        pass

    def before_change_value_of(self, element, driver) -> None:
        print(f"before_change_value_of {element}")
        print(f"Text is: <{element.get_attribute('value')}>")

    def after_change_value_of(self, element, driver) -> None:
        print(f"after_change_value_of  {element}")
        print(f"Text is: <{element.get_attribute('value')}>")

    def before_execute_script(self, script, driver) -> None:
        pass

    def after_execute_script(self, script, driver) -> None:
        pass

    def before_close(self, driver) -> None:
        pass

    def after_close(self, driver) -> None:
        pass

    def before_quit(self, driver) -> None:
        pass

    def after_quit(self, driver) -> None:
        pass

    def on_exception(self, exception, driver) -> None:
        pass