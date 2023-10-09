import time
from selenium import webdriver
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

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




class DemoExplicitWait:
    def demo_explicit_wait(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        time.sleep(2)
        going_to.send_keys("New")

        time.sleep(2)

        search_result = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='viewport']//div[1]//li"))).find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")
        # time.sleep(2)
        # search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")



        print(search_result)
        print(len(search_result))

        time.sleep(2)

        for result in search_result:
            print(result.text)
            print(result)
            print("||||||||||||")
            if "New York (JFK)" in result.text:
                result.click()
                break

        # Not a recommended way to select a calendar date
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        # origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        # origin.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@id='07/12/2023']"))).click()
        # driver.find_element(By.XPATH, "//td[@id='07/12/2023']").click()
        time.sleep(4)


# DID NOT WORK !!!!!!!!!!!
# DID NOT WORK !!!!!!!!!!!
# DID NOT WORK !!!!!!!!!!!
# DID NOT WORK !!!!!!!!!!!
# DID NOT WORK !!!!!!!!!!!
# DID NOT WORK !!!!!!!!!!!
# DID NOT WORK !!!!!!!!!!!
# DID NOT WORK !!!!!!!!!!!
# DID NOT WORK !!!!!!!!!!!
# DID NOT WORK !!!!!!!!!!!
# DID NOT WORK !!!!!!!!!!!



class DemoFluentWait:
    def demo_fluent_wait(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        wait = WebDriverWait(driver, 10, 1, ignored_exceptions=[ElementClickInterceptedException])
        # , ignored_exceptions= []
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        time.sleep(2)
        going_to.send_keys("New")

        time.sleep(2)

        search_result = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='viewport']//div[1]//li"))).find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")
        # time.sleep(2)
        # search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")



        print(search_result)
        print(len(search_result))

        time.sleep(2)

        for result in search_result:
            print(result.text)
            print(result)
            print("||||||||||||")
            if "New York (JFK)" in result.text:
                result.click()
                break

        # Not a recommended way to select a calendar date
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        #.click()
        # origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        # origin.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@id='07/12/2023']"))).click()

        # driver.find_element(By.XPATH, "//td[@id='07/12/2023']").click()
        time.sleep(4)






fluentWait = DemoFluentWait()
fluentWait.demo_fluent_wait()


# explicitWait = DemoExplicitWait()
# explicitWait.demo_explicit_wait()


# implicitWait = DemoImplicitWait()
# implicitWait.demo_implicit_wait()