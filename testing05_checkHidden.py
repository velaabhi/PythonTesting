
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#    is_displayed() - its used to check if an element appears on the screen or not - returns bool

class Demo():

    #in this case that element is there its only getting hidden (value as "none") in the style tag of DOM when its hidden
    def checkEnabledEle1(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")

        #check element appears after clicking a button
        elementAppears = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        time.sleep(5)
        print("element appears  ? ", elementAppears)

        #check element when button is not clicked
        driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        elementAppears = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        time.sleep(5)
        print("element appears  ? ", elementAppears)



    #in this case that element is there its only getting hidden (value as "none") in the style tag of DOM when its hidden
    def checkEnabledEle2(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.yatra.com/hotels")


        # check element appears after clicking a button
        driver.find_element(By.XPATH,"//i[@class='icon icon-angle-right arrowpassengerBox']").click() #to display the part
        driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        elementAppears = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        time.sleep(5)
        print("element appears  ? ", elementAppears)


        # check element when button is not clicked
        driver.find_element(By.XPATH,"//i[@class='icon icon-angle-right arrowpassengerBox']").click() #to hide the part
        elementAppears = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed() #since ele is not found - we get no such element found exception
        time.sleep(5)
        print("element appears  ? ", elementAppears)




find = Demo()
#find.checkEnabledEle1()
find.checkEnabledEle2()
print("Search completed. Press Ctrl+C to close the browser window.")
input("Press Enter to continue...")


