from selenium import webdriver
import allure
import pytest

@allure.title("Verify that the title 'CURA Healthcare Service' is there in the page.")
def test_demo_cura():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURA Healthcare Service" in driver.page_source:
        print("Text Found!!, Test Case Passed!")
    else:
        print("Text not found on the page")
        pytest.fail("Text not found on the page") #failing the test case deliberately.

# Python Interpreter is closing the browser.