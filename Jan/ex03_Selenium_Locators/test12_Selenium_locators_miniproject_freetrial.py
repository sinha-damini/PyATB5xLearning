import allure
import  pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
import os

@allure.title("VWO Login Testcase")
@allure.description("TC02 - VWO Login FreeTrial check.")
@pytest.mark.vwofreetrialcheck
def test_app_vwo_login_freetrial_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))

    # <a
    # href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo"
    # >Start a free trial<
    # /a>

    # Here we can use class, link text or partial_text

    anchor_tag_element = driver.find_element(By.CSS_SELECTOR, ".text-link")
    anchor_tag_element.click()

    # anchor_tag_element = driver.find_element(By.LINK_TEXT, "Start a free trial")
    # anchor_tag_element.click()

    # anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Start a free")
    # anchor_tag_element.click()

    # anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "a ")
    # anchor_tag_element.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    time.sleep(5)
    driver.quit()  # close everything.


# pytest -s Jan/ex03_Selenium_Locators/test12_Selenium_locators_miniproject_freetrial.py --alluredir=./allure-results