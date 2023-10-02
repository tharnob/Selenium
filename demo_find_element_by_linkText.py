import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class DemoFindElementByCss():
    def locate_by_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        time.sleep(3)
        element = driver.find_element("partial link text", "Holida")
        # driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.fullscreen_window()
        driver.find_element("xpath", "//button[normalize-space()='Ok,I Agree']").click()
        element.click()
        time.sleep(4)


findById = DemoFindElementByCss()
findById.locate_by_demo()