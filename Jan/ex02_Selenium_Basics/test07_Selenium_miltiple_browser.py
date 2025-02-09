from selenium import webdriver
import allure
import pytest
import time

@allure.title("Verify that the url of katalon is  as expected.")
def test_katalon_chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"


def test_katalon_edge():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"


def test_katalon_firefox():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"


# To run everything parallely.
# pip install pytest-xdist
# pytest -n auto -s Jan/ex02_Selenium_Basics/test07_Selenium_miltiple_browser.py