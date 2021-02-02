import inspect
import json
import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from page.wrapper import handle_black


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver
    _params = dict()


    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @handle_black
    def find(self, loctor, value: str=None):

        element:WebElement

        if isinstance(loctor, tuple):
            element = self._driver.find_element(*loctor)

        else:
            element = self._driver.find_element(loctor, value)

        return element



    def steps(self, path):
        with open(path) as f:
            name=inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]
            raw=json.dumps(steps)
        for key,value in self._params.items():
            raw=raw.replace(f"${{{key}}}",value)

        steps=json.loads(raw)


        for step in steps:
            if "action" in step:
                if step["action"] == "click":
                    self.find(step["by"], step["locator"]).click()
                elif step["action"] == "sendkeys":
                    self.find(step["by"], step["locator"]).send_keys(step["keys"])
                else:
                    logging.warning("定位有误")


