import pytest
import allure

@allure.title("Verify that create booking, with valid data is working")
@allure.description("This Testcase check for the positive create booking")
@pytest.mark.positive
def test_create_booking_positive():
    print("test1")
    assert 1-1 == 2

@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase check for the negative  create booking")

@pytest.mark.negative
def test_create_booking_negative_1():
    print("test2")
    assert 1 + 1 == 2


@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase check for the negative  create booking")
@pytest.mark.negative
def test_create_booking_negative_2():
    print("test2")
    assert 1 + 1 == 2


#pip install allure-pytest
#pytest --alluredir=allure_result
#allure serve allure_result


#Dec/ex_28122024_PyTest/test_Lab188_Pytest_Learning_Allure.py --alluredir=allure_result
#after this allure_result folder is created

#at last run the command , allure serve allure_result
