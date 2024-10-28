import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class Demo():
    def screen_capture(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        time.sleep(2)
        driver.get("https://secure.yatra.com/social/common/yatra/register")
        time.sleep(2)
        continue_btn = driver.find_element(By.XPATH, "//*[@id='login-continue-btn']")
        continue_btn.screenshot(".\\test.png")      #captures the img of element
        continue_btn.click()
        time.sleep(2)
        driver.get_screenshot_as_file(".\\error.png")      #captures complete screen
        driver.save_screenshot(".\\error2.png")
        print("msg is ",driver.get_issue_message())



find = Demo()
find.screen_capture()

print("Search completed. Press Ctrl+C to close the browser window.")
input("Press Enter to continue...")