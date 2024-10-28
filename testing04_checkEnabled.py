
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#    is_enabled() - its used to check if a button is enabled or not - returns bool

class Demo():
    def checkEnabledEle(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://training.openspan.com/login")

        # when username and password is blank
        buttonEnabled = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        time.sleep(5)
        print("Sign in button is enabled or not ? ",buttonEnabled)

        # when username and password is filled
        driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys("arvii")
        driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys("arv@123")
        buttonEnabled = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        time.sleep(5)
        print("After filling Username and Password Sign in button is enabled or not ? ", buttonEnabled)


find = Demo()
find.checkEnabledEle()

print("Search completed. Press Ctrl+C to close the browser window.")
input("Press Enter to continue...")