import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Modals_MakeMyTrip")
@allure.description("Verify Modals in Make_My_Trip")
def test_modals_makemytrip():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")


    WebDriverWait(driver=driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Enter Mobile Number']")))

    modal = driver.find_element(By.XPATH, "//input[@placeholder='Enter Mobile Number']")
    modal.send_keys("9876543210")

    continue_button = driver.find_element(By.XPATH, "//span[normalize-space()='Continue']")
    continue_button.click()

    time.sleep(5)



