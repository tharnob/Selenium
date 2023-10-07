import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoMultipleWindows():
    def locate_windows(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        # driver.maximize_window()
        parent_handle = driver.current_window_handle
        print(parent_handle)
        time.sleep(5)
        driver.find_element(By.XPATH, "//img[@alt='Flat 12% OFF (upto Rs. 1,500)']").click()
        time.sleep(5)
        print("WORKED!")

        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//a[@id='twtr_yttkd']").click()
                time.sleep(4)
                driver.close()
                time.sleep(2)
                break

        driver.switch_to.window(parent_handle)
        time.sleep(4)
        driver.find_element(By.XPATH, "//img[@alt='Flat 12% OFF (upto Rs. 1,500)']").click()
        time.sleep(5)

demoMultipleWindows = DemoMultipleWindows()
demoMultipleWindows.locate_windows()