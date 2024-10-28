
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import  Select

#for dropdown there are 2 implementations - 1. Dropdown by using select class, 2. By using list and unordered list
#select tags can again have 2 implementations - 1.single select, 2.multiple select
#3 methods to select - 1.by Index, 2.by Value, 3.by Visible text

class Demo():

    def checkDropdownSingleSelect(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.salesforce.com/in/form/sem/salesforce-crm/?d=7013y000002hbRLAAY&nc=7013y000000a9thAAA&utm_source=google&utm_medium=paid_search&utm_campaign=apac_in_alllobcon&utm_content=brand-en-multi-product-search_salesforce-crm_7013y000002hbrlaay_7013y000002hbRLAAY&utm_term=Salesforce&ef_id=Cj0KCQjwrp-3BhDgARIsAEWJ6SzSPqYInDF7C0FGTfLjwuZbu9OcEFWtBCtrFG94RvOFIxVPVyA01J0aApV0EALw_wcB:G:s&s_kwcid=AL!4720!3!676565784220!e!!g!!salesforce&&ev_sid=3&ev_ln=salesforce&ev_lx=kwd-94920873&ev_crx=676565784220&ev_mt=e&ev_n=g&ev_ltx=&ev_pl=&ev_pos=&ev_dvc=c&ev_dvm=&ev_phy=9062114&ev_loc=&ev_cx=16895847353&ev_ax=137218384684&ev_efid=Cj0KCQjwrp-3BhDgARIsAEWJ6SzSPqYInDF7C0FGTfLjwuZbu9OcEFWtBCtrFG94RvOFIxVPVyA01J0aApV0EALw_wcB:G:s&url=!https://clickserve.dartsearch.net/link/click%3flid=43700074078535017&ds_s_kwgid=58700008151233901&gad_source=1&gclid=Cj0KCQjwrp-3BhDgARIsAEWJ6SzSPqYInDF7C0FGTfLjwuZbu9OcEFWtBCtrFG94RvOFIxVPVyA01J0aApV0EALw_wcB&gclsrc=aw.ds")

        dropdownEle =  driver.find_element(By.NAME,"UserTitle")

        dd = Select(dropdownEle)

        dd.select_by_index(1)  # we didnt take 0 index cz its been disabled by the frontend for placeholder "Job title"
        time.sleep(3)

        dd.select_by_value("Customer_Service_Manager_AP")
        time.sleep(3)

        dd.select_by_visible_text("IT Manager")
        time.sleep(3)

    def checkDropdownMultiSelect(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.salesforce.com/in/form/sem/salesforce-crm/?d=7013y000002hbRLAAY&nc=7013y000000a9thAAA&utm_source=google&utm_medium=paid_search&utm_campaign=apac_in_alllobcon&utm_content=brand-en-multi-product-search_salesforce-crm_7013y000002hbrlaay_7013y000002hbRLAAY&utm_term=Salesforce&ef_id=Cj0KCQjwrp-3BhDgARIsAEWJ6SzSPqYInDF7C0FGTfLjwuZbu9OcEFWtBCtrFG94RvOFIxVPVyA01J0aApV0EALw_wcB:G:s&s_kwcid=AL!4720!3!676565784220!e!!g!!salesforce&&ev_sid=3&ev_ln=salesforce&ev_lx=kwd-94920873&ev_crx=676565784220&ev_mt=e&ev_n=g&ev_ltx=&ev_pl=&ev_pos=&ev_dvc=c&ev_dvm=&ev_phy=9062114&ev_loc=&ev_cx=16895847353&ev_ax=137218384684&ev_efid=Cj0KCQjwrp-3BhDgARIsAEWJ6SzSPqYInDF7C0FGTfLjwuZbu9OcEFWtBCtrFG94RvOFIxVPVyA01J0aApV0EALw_wcB:G:s&url=!https://clickserve.dartsearch.net/link/click%3flid=43700074078535017&ds_s_kwgid=58700008151233901&gad_source=1&gclid=Cj0KCQjwrp-3BhDgARIsAEWJ6SzSPqYInDF7C0FGTfLjwuZbu9OcEFWtBCtrFG94RvOFIxVPVyA01J0aApV0EALw_wcB&gclsrc=aw.ds")

        dropdownEle =  driver.find_element(By.NAME,"UserTitle")

        dd = Select(dropdownEle)

        dd.select_by_index(1)  # we didnt take 0 index cz its been disabled by the frontend for placeholder "Job title"
        time.sleep(3)

        dd.select_by_value("Customer_Service_Manager_AP")
        time.sleep(3)

        dd.select_by_visible_text("IT Manager")
        time.sleep(3)


find = Demo()
#find.checkDropdownSingleSelect()
find.checkDropdownMultiSelect()

print("Search completed. Press Ctrl+C to close the browser window.")
input("Press Enter to continue...")