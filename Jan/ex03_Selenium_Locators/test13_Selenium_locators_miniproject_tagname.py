import allure
import  pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
import os

@allure.title("VWO Login Testcase")
@allure.description("TC03 - Positive TC - Exploring Tag Names.")
@pytest.mark.vwofreetrialchecktagname
def test_app_vwo_login_tagname_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))

    all_links_page = driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links_page))
    for i in range(len(all_links_page)):
        element = driver.find_elements(By.TAG_NAME, "a")[i]
        print(element.text)
        if "Start a free trial" in element.text:
            element.click()

    time.sleep(5)
    driver.quit()  # close everything.


# pytest -s Jan/ex03_Selenium_Locators/test13_Selenium_locators_miniproject_tagname.py --alluredir=./allure-results