import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("EspoCRM Advanced Pack.")
@allure.description("TC03-Positive Case-Verify that advanced pack button is working fine.")
@pytest.mark.positiveespoadvancedpack
def test_load_espo_crm_advanced_pack():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)

    advance_pack_web_element = driver.find_element(By.LINK_TEXT, "Advanced Pack")
    advance_pack_web_element.click()

    time.sleep(3)

    main_window = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != main_window:
            driver.switch_to.window(window_handle)
            break

    time.sleep(3)
    expected_url = "https://www.espocrm.com/extensions/advanced-pack/"
    assert driver.current_url == expected_url

    time.sleep(5)
    driver.quit()

# pytest -s Jan/ex03_Selenium_Locators/Task_16012025_Espo_CRM_Selenium_Project/task03_Verify_Advance_Pack_Button.py --alluredir=./allure-results
# allure serve allure-results
