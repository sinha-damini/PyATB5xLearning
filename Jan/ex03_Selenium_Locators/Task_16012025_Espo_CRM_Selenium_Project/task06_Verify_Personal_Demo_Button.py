import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("EspoCRM Personal Demo.")
@allure.description("TC04-Positive Case-Verify that personal demo button is working fine.")
@pytest.mark.positiveespopersonaldemo
def test_load_espo_crm_personal_demo():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)

    personal_demo_web_element = driver.find_element(By.PARTIAL_LINK_TEXT, "personal demo")
    personal_demo_web_element.click()

    time.sleep(3)
    expected_url = "https://www.espocrm.com/cloud-registration/?plan=demo"
    assert driver.current_url == expected_url

    time.sleep(5)
    driver.quit()

# pytest -s Jan/ex03_Selenium_Locators/Task_16012025_Espo_CRM_Selenium_Project/task06_Verify_Personal_Demo_Button.py --alluredir=./allure-results
# allure serve allure-results

