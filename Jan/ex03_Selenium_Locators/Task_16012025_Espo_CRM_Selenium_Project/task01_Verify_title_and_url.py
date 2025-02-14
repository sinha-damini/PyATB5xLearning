import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@allure.title("Espo CRM Login Page.")
@allure.description("TC01-Positive Case-Verify that title and URL is appearing correctly.")
@pytest.mark.positiveespologinpage
def test_load_espo_crm():
    chrome_options  = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://demo.us.espocrm.com/")
    print(driver.title)


    assert driver.title == "EspoCRM Demo"
    assert driver.current_url == "https://demo.us.espocrm.com/"

    time.sleep(5)
    driver.quit()

# pytest -s Jan/ex03_Selenium_Locators/Task_16012025_Espo_CRM_Selenium_Project/task01_Verify_title_and_url.py --alluredir=./allure-results
# allure serve allure-results