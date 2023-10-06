import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


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
        text = driver.find_element(By.XPATH,
                                   "//body/div[@class='theme-snipe']/div[@id='themeSnipe']/section[@class='wrapper']/div[@class='right_data']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]/div[1]").text

        text1 = driver.find_element(By.XPATH,
                                    "//h1[contains(text(),'Book Flights, Hotels, Trains, Buses, Cruise and Ho')]").text

        print(text)
        print(text1)
        time.sleep(2)


class DemoGetAttributeValue():

    def demo_getValue(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        attr_value = driver.find_element(By.XPATH,
                                         "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute(
            "class")

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

        driver.find_element(By.XPATH,
                            "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        elem = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()

        time.sleep(2)
        print(elem)

        driver.find_element(By.XPATH,
                            "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]").click()

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


class DemoRadio:
    def demo_radio_button(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.ironspider.ca/forms/checkradio.htm")
        time.sleep(2)
        var1 = driver.find_element(By.XPATH,
                                   "//form[contains(text(),'Your current web browser is:')]//input[2]").is_selected()
        driver.find_element(By.XPATH, "//form[contains(text(),'Your current web browser is:')]//input[2]").click()
        var2 = driver.find_element(By.XPATH,
                                   "//form[contains(text(),'Your current web browser is:')]//input[2]").is_selected()

        print(var1, var2)
        time.sleep(4)



class DemoDropdown:
    def demo_dropdown(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.salesforce.com/au/form/signup/freetrial-sales/")
        dropdown = driver.find_element(By.NAME, "UserTitle")
        dd = Select(dropdown)
        time.sleep(2)
        dd.select_by_index(1)
        time.sleep(2)
        dd.select_by_value("CxO_General_Manager_ANZ")
        time.sleep(2)
        dd.select_by_visible_text("Marketing / PR Manager")
        time.sleep(4)


# To run the below code, I took a multidropdown code from w3 school and then run it on vscode on my local machine


# SOURCE CODE:

# <!DOCTYPE html>
# <html>
# <body>
#
# <h1>The select multiple attribute</h1>
#
# <p>The multiple attribute specifies that multiple options can be selected at once:</p>
#
# <form action="/action_page.php">
#   <label for="cars">Choose a car:</label>
#   <select name="cars" id="cars" multiple>
#     <option value="volvo">Volvo</option>
#     <option value="saab">Saab</option>
#     <option value="opel">Opel</option>
#     <option value="audi">Audi</option>
#   </select>
#   <br><br>
#   <input type="submit" value="Submit">
# </form>
#
# <p>Hold down the Ctrl (windows) or Command (Mac) button to select multiple options.</p>
#
# </body>
# </html>

class DemoDropDownMultiSelect:
    def demo_dropdown_multiSelect(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("http://127.0.0.1:5500/index.html")
        multiDropdown = driver.find_element(By.NAME, "cars")
        dd_multi = Select(multiDropdown)

        time.sleep(2)
        dd_multi.select_by_index(0)
        time.sleep(2)
        dd_multi.select_by_value("saab")
        time.sleep(2)
        dd_multi.select_by_visible_text("Audi")
        time.sleep(2)
        dd_multi.deselect_by_visible_text("Saab")
        time.sleep(2)
        dd_multi.deselect_by_value("audi")
        time.sleep(4)



class DemoAutoSuggest:
    def demo_auto_suggest(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(2)

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        time.sleep(2)
        going_to.send_keys("New")
        time.sleep(2)
        search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")
        time.sleep(2)
        print(search_result)
        print(len(search_result))
        time.sleep(2)
        for result in search_result:
            print(result.text)
            print(result)
            print("||||||||||||")
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(4)
                break



        
        
d_auto = DemoAutoSuggest()
d_auto.demo_auto_suggest()






# multiSelect = DemoDropDownMultiSelect()
# multiSelect.demo_dropdown_multiSelect()


# ddDemo = DemoDropdown()
# ddDemo.demo_dropdown()


# radioDemo = DemoRadio()
# radioDemo.demo_radio_button()

# checkbox = CheckBoxes()
# checkbox.demo_checkBox()


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
