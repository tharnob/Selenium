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

class DemoGetAttributeValue():

    def demo_getValue(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        attr_value = driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("class")

        print(attr_value)
        time.sleep(2)




class DemoHiddenElements():

    def demo_is_displayed(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()

        elem1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem1)


    def demo_is_displayed_yatra(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/hotels")
        driver.find_element(By.XPATH, "//i[@class='icon icon-angle-right arrowpassengerBox']").click()

        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        elem = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()

        time.sleep(2)
        print(elem)

        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]").click()


        try:
            elem1 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()

        except:
            print("No such Element!")

        else:
            print(elem1)
        time.sleep(2)





class CheckBoxes():
    def demo_checkBox(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.ironspider.ca/forms/checkradio.htm")
        driver.find_element(By.XPATH, "//input[@value='red']").click()
        driver.find_element(By.XPATH, "//input[@value='blue']").click()
        var1 = driver.find_element(By.XPATH, "//input[@value='blue']").is_selected()
        var2 = driver.find_element(By.XPATH, "//input[@value='yellow']").is_selected()
        driver.maximize_window()
        print(var1)
        print(var2)
        time.sleep(2)


checkbox = CheckBoxes()
checkbox.demo_checkBox()




# demoDisplayed = DemoHiddenElements()
# demoDisplayed.demo_is_displayed()
# demoDisplayed.demo_is_displayed_yatra()


# demoState = DemoElementState()
# demoState.demo_enable_disable()


# getAttrValue = DemoGetAttributeValue()
# getAttrValue.demo_getValue()


# getText = DemoGetText()
# getText.getTheText()



# findById = DemoByClass()
# findById.locate_by_demo()



