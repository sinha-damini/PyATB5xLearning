import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@allure.title("Espo CRM Logging In.")
@allure.description("TC02-Positive Case-Verify able to login successfully.")
@pytest.mark.positiveespologin
def test_load_espo_crm_login():
    chrome_options  = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)

    # <<button
    # type="submit"
    # class="btn btn-primary btn-s-wide"
    # id="btn-login">
    # Login
    # </button>


    login_web_element = driver.find_element(By.ID, "btn-login")
    login_web_element.click()
    time.sleep(3)
    assert driver.current_url == "https://demo.us.espocrm.com/?l=en_US"


    time.sleep(5)
    driver.quit()

# pytest -s Jan/ex03_Selenium_Locators/Task_16012025_Espo_CRM_Selenium_Project/task02_Verify_Login.py --alluredir=./allure-results
# allure serve allure-results

