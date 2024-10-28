import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class DemoFindElement():
    def locate_by_xpath(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/register")
        driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys("8149979901")
        time.sleep(5)

find = DemoFindElement()
find.locate_by_xpath()

print("Search completed. Press Ctrl+C to close the browser window.")
input("Press Enter to continue...")