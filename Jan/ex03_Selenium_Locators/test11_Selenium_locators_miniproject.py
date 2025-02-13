import allure
import  pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
import os

@allure.title("VWO Login Negative Testcase")
@allure.description("TC01 - Negative TC - VWO Login with invalid credentials.")
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))

    # 1. Find the email and enter the wrong username or email

    # <input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # data-gtm-form-interact-field-id="0"
    # >
    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys(os.getenv("INVALID_USERNAME"))

    # <input
    # type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # >

    password_web_element = driver.find_element(By.NAME, "password")
    password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))



    # <button
    # type="submit"
    # id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica">

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    # Wait for sometime
    time.sleep(3)

    # <div
    # class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">
    # Your email, password, IP address or location did not match
    # </div>

    # error_message_web_element = driver.find_element(By.ID, "js-notification-box-msg")
    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)

    assert error_message_web_element.text == os.getenv("error_message_expected")

    time.sleep(5)
    driver.quit()  # close everything.