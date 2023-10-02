import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoFindElementByCss():
    def locate_by_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/")
        lista = driver.find_elements(By.TAG_NAME, "a")
        print(len(lista))
        for i in lista:
            print(i.text)
        time.sleep(4)


findById = DemoFindElementByCss()
findById.locate_by_demo()