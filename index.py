import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager




class DemoFindElementByID():
    def locate_by_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element("id", "login-input").send_keys("test@test.com")
        time.sleep(4)


findById = DemoFindElementByID()
findById.locate_by_demo()



