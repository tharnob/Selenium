import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.alert import Alert
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






class DemoIframe:
    def demo_frame(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        # Switch with Iframe locator
        # By XPATH
        # driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))

        # By ID
        # driver.switch_to.frame("iframeResult")

        # By Name

        driver.switch_to.frame("iframeResult")

        # Switch with index
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH, "//a[normalize-space()='Log in']").click()
        time.sleep(24)



class DemoJsPopup:
    def demo_js_alerts(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.switch_to.frame("iframeResult")

        time.sleep(5)

        print("Worked!")

        # Accept Alert

        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)

        print("Worked! AGAIN!")

        # Dismiss Alert
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        # driver.switch_to.alert.dismiss()
        Alert(driver).dismiss()
        time.sleep(2)

        # Send text in alert

        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.send_keys("Tafsir Haque Arnob")
        driver.switch_to.alert.accept()
        time.sleep(2)


# ACTION CHAIN CLASS IS USED FOR MOUSE HOVER

class DemoMouseHover:
    def demo_mouse_hover(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        moreButton = driver.find_element(By.XPATH, "//span[@class='more-arr']")

        myAccountLink = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")

        aChains = ActionChains(driver)
        aChains.move_to_element(myAccountLink).perform()
        time.sleep(4)

        aChains.move_to_element(moreButton).perform()
        time.sleep(4)
        driver.find_element(By.XPATH, "//span[normalize-space()='Xplore']").click()
        time.sleep(4)





class DemoRightDoubleClick:
    def demo_right_doubleClick(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()

        # RIGHT CLICK

        # aChains = ActionChains(driver)
        # elem1 = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        # copyElem = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']")
        # aChains.context_click(elem1).perform()
        # time.sleep(4)
        # copyElem.click()
        # time.sleep(4)

        # DOUBLE CLICK

        # driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        # driver.maximize_window()

        aChains1 = ActionChains(driver)
        elem2 = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")

        aChains1.double_click(elem2).perform()
        time.sleep(4)




class DemoSliders:
    def demo_sliders(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://codepen.io/jackiejohnston/pen/NNrpjQ")
        driver.switch_to.frame("result")
        elem1 = driver.find_element(By.CLASS_NAME, "noUi-handle-lower")
        elem2 = driver.find_element(By.CLASS_NAME, "noUi-handle-upper")


        # MULTIPLE WAYS -> FIRST WAY
        # time.sleep(4)
        # ActionChains(driver).drag_and_drop_by_offset(elem1, 60, 0).perform()
        # time.sleep(4)

        # IF FIRST NOT WORKS -> SECOND WAY

        # time.sleep(4)
        # ActionChains(driver).click_and_hold(elem1).pause(1).move_by_offset(50, 0).release().perform()
        # time.sleep(4)

        # IF THIS DON'T WORK TOO -> THIRD WAY (FOR SYNCHRONIZATION ISSUES)

        time.sleep(4)
        ActionChains(driver).move_to_element(elem1).pause(1).click_and_hold(elem1).move_by_offset(80, 0).release().perform()
        time.sleep(4)

        ActionChains(driver).drag_and_drop_by_offset(elem2, -60, 0).perform()
        time.sleep(4)






sliders = DemoSliders()
sliders.demo_sliders()






# rightDoubleClick = DemoRightDoubleClick()
# rightDoubleClick.demo_right_doubleClick()


# mouseHover = DemoMouseHover()
# mouseHover.demo_mouse_hover()


# jsAlerts = DemoJsPopup()
# jsAlerts.demo_js_alerts()


# demoFrame = DemoIframe()
# demoFrame.demo_frame()


# demoMultipleWindows = DemoMultipleWindows()
# demoMultipleWindows.locate_windows()