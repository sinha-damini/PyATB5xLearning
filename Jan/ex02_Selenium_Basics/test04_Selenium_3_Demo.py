C:\Users\HP\Downloads

from selenium import webdriver
import allure
import pytest

def test_vwo_sample_selenium_3():
    driver_path = '/Users/HP/Downloads/MicrosoftEdgeSetup'
    driver = webdriver.EdgeService(executable_path=driver_path)
    driver.get("https://app.vwo.com")