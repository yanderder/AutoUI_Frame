import allure

from page.base_page import BasePage


class SearchPage(BasePage):
    def search(self,address):
        self._params["address"] = address
        self.steps("../page/search.yaml")
        self._driver.save_screenshot("search.png")
        with open("search.png", "rb") as f:
            content = f.read()
        allure.attach(content, attachment_type=allure.attachment_type.PNG)