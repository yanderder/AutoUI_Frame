import logging

import allure
from selenium.webdriver.common.by import By


def handle_black(func):

    logging.basicConfig(level=logging.INFO)

    def warpper(*args, **kwargs):
        from page.base_page import BasePage

        _blacklist = [
            (By.ID, "com.yunshen.autobike:id/base_banner_dimiss"),
        ]
        _countfind = 0
        _maxfind = 3
        instance: BasePage = args[0]
        try:
            logging.info("run "+func.__name__+"\n args: \n"+repr(args)+"\n"+repr(kwargs))
            element = func(*args, **kwargs)
            _countfind = 0
            # 隐式等待恢复原来的值
            instance._driver.implicitly_wait(10)

            return element

        except Exception as e:
            logging.error("element not found ,handle black list.")
            instance._driver.save_screenshot("temp.png")
            with open("temp.png","rb") as f:
                content=f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)


            instance._driver.implicitly_wait(2)
            if _countfind > _maxfind:
                raise e

            _countfind += 1

            for ele in _blacklist:

                elelist = instance._driver.find_elements(*ele)
                if len(elelist) > 0:

                    elelist[0].click()
                    return warpper(*args, **kwargs)
            raise e

    return warpper
