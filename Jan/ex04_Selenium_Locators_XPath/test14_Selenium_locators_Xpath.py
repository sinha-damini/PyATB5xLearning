
import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@allure.title("Practicing XPath.")
@allure.description("TC1 - Exploring XPath")
def test_xpath_chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_app_btn = driver.find_element(By.XPATH, "//a[contains(text(),'Make')]")
    make_app_btn.click()

    # text() -> Exact Match

    # Partial Text() - contains()
    # //a[contains(text(),'Make Appointment')]
    # //a[contains(text(),'Appointment')]
    # //a[contains(text(),'Make')]
    # //a[contains(text(),'Ma')]
    # //a[contains(text(),'App')] - This may fail if there 1 or more a tag with App.
    # <a rel="https:/google.com"/>

    # //a[starts-with(text(),'Make')]

    time.sleep(5)
    driver.quit()  # close everything.

# pytest -s Jan/ex04_Selenium_Locators_XPath/test14_Selenium_locators_Xpath.py --alluredir=./allure-results
# allure serve allure-results