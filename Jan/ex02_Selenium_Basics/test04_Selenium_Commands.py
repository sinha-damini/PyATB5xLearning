from selenium import webdriver
import allure
import  pytest

@allure.title("Verify that the title of vwo.com is as expected.")
def test_vwo_sample():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"


# pytest -s JAN/ex02_Selenium_Basics/test04_Selenium_Commands.py --alluredir=./allure-results
# allure serve allure-results