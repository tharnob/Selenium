import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoImplicitWait:
    def demo_implicit_wait(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/")
        driver.find_element(By.ID, "username").send_keys("tharnob")
        driver.find_element(By.ID, "password").send_keys("tharnob")





implicitWait = DemoImplicitWait()
implicitWait.demo_implicit_wait()