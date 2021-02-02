from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.search_page import SearchPage


class Main(BasePage):
    def goto_search(self):
        self.steps("../page/main.yaml")

        return SearchPage(self._driver)


