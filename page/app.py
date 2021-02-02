from time import sleep

import yaml
from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):

    _package = "com.yunshen.autobike"
    _activity = "com.yunshen.autobike.NewSplashActivity"

    def start(self):
        if self._driver is None :
            des_caps = dict()
            des_caps["platformName"] = "android"
            des_caps["deviceName"] = yaml.safe_load(open("../page/configuration.yaml"))["caps"]["deviceName"]
            des_caps["appPackage"] = self._package
            des_caps["appActivity"] = self._activity
            des_caps["noReset"] = False
            des_caps["platformVersion"] = "11"
            des_caps["autoGrantPermissions"]= True
            # des_caps = {
            #     "platformName": "android",
            #     "platformVersion": "11",
            #     "browserName": "Chrome",
            #     # "udid":"xxxx",设备唯一标识
            #     #  "noReset": "true", 不要停止应用程序，不要清除应用程序数据，也不要卸载APK。（默认：测试后停止并清除应用数据。不要卸载apk）
            #     "noReset": True,
            #     # "fullReset":"true" 在会话开始之前和测试之后停止应用程序，清除应用程序数据并卸载apk
            #     "deviceName": "998ec161",
            #     "chromedriverExecutable": "D:\soft_tools\Python\Python38\chromedriver.exe",
            #     # "autoGrantPermissions":"true" 权限自动赋予
            #     "autoGrantPermissions": True,
            #     # "dontStopAppOnReset":"true" 在使用adb启动应用程序之前，不要停止被测应用程序的进程。
            # }
            # print("aa")
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        else:
            self._driver.launch_app()
        # self._driver.find_element_by_id("base_dialog_ty").click()
        # self._driver.implicitly_wait(10)
        sleep(10)


        return self

    def main(self)-> Main:
        sleep(10)
        self._driver.save_screenshot("main.png")
        return Main(self._driver)
