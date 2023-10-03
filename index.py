import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



class DemoByClass():
    def locate_by_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CLASS_NAME, "email-login-box").send_keys("rcv@academy.com")
        time.sleep(4)



class DemoGetText():

    def getTheText(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        text = driver.find_element(By.XPATH, "//body/div[@class='theme-snipe']/div[@id='themeSnipe']/section[@class='wrapper']/div[@class='right_data']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]/div[1]").text

        text1 = driver.find_element(By.XPATH, "//h1[contains(text(),'Book Flights, Hotels, Trains, Buses, Cruise and Ho')]").text



        print(text)
        print(text1)
        time.sleep(2)





# getText = DemoGetText()
# getText.getTheText()



# findById = DemoByClass()
# findById.locate_by_demo()



