import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class DemoFindElement():
    def getAttribute(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://secure.yatra.com")
        Actualtext = driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        time.sleep(5)
        print(Actualtext)

find = DemoFindElement()
find.getAttribute()

print("Search completed. Press Ctrl+C to close the browser window.")
input("Press Enter to continue...")