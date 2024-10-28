
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class Demo():

    def checkCheckbox(self):  # for this tag will be "input" and type will be "checkbox" and then use "is_selected"
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.amazon.in/s?k=music&crid=1M1P9JGAKCUAS&sprefix=music%2Caps%2C224&ref=nb_sb_noss_2")
        driver.find_element(By.LINK_TEXT,"pTron").click()
        time.sleep(8)
        checkboxSelected = driver.find_element(By.LINK_TEXT, "pTron").is_selected()
        print("Check-box is selected ",checkboxSelected)

    def checkRadioBtn(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://training.openspan.com/login")




find = Demo()
find.checkCheckbox()

print("Search completed. Press Ctrl+C to close the browser window.")
input("Press Enter to continue...")