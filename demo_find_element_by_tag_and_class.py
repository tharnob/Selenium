import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class DemoFindElementByCss():
    def locate_by_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        #driver.find_element("tag name", "input").send_keys("test@test.com")
        driver.find_element("class name", "email-login-box").send_keys("test@test.com")
        time.sleep(4)


findById = DemoFindElementByCss()
findById.locate_by_demo()