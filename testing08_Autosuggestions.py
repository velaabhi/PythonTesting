
import time
from re import search

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import  Select

#for auto-suggestions
class Demo():

    def CheckAutoSuggestions1(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        departFrom = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        departFrom.click()
        time.sleep(4)
        departFrom.send_keys("New Delhi")       #we are entering entire value and then clicking Enter
        time.sleep(4)
        departFrom.send_keys(Keys.ENTER)
        time.sleep(4)

        going_to = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        going_to.click()
        time.sleep(4)
        going_to.send_keys("New")
        time.sleep(4)
        searchResults = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        for results in searchResults:
            if "New Zealand" in results.text:
                results.click()
                time.sleep(4)
                break
        time.sleep(4)

        selectCalender = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
        selectCalender.click()
        driver.find_element(By.CSS_SELECTOR,"td[id='03/10/2024']").click()


find = Demo()
find.CheckAutoSuggestions1()

print("Search completed. Press Ctrl+C to close the browser window.")
input("Press Enter to continue...")