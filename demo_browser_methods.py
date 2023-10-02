import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoSeleniumLearning():
    def demo_browser_method(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://training.rcvacademy.com")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        time.sleep(2)
        driver.find_element("link text", "ALL COURSES").click()
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.minimize_window()
        time.sleep(10)
        driver.quit()




demoBrowser = DemoSeleniumLearning()
demoBrowser.demo_browser_method()