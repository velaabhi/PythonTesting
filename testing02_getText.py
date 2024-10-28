import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class DemoFindElement():
    def gettext(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://secure.yatra.com")
        Actualtext = driver.find_element(By.XPATH, "//p[contains(text(),'On Yatra.com, you can tailor your trip from end-to')]").text
        time.sleep(5)
        print(Actualtext)

find = DemoFindElement()
find.gettext()

print("Search completed. Press Ctrl+C to close the browser window.")
input("Press Enter to continue...")