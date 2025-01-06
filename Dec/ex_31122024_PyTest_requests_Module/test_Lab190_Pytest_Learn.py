import pytest
import allure
import requests


@allure.title("TC#1 - Verify that 2-2 is equal to 0")
@allure.description("This is a BASIC Math Test")
@pytest.mark.smoke
def test_basic_math():
    assert 2-2 == 0

@allure.title("TC#2 - Verify that 3-3 is equal to 0")
@allure.description("This isn't a smoke Testcase which check that 3-3 is equal to 0")
@pytest.mark.regression
def test_sub1():
    assert 3 - 3 == 0


@allure.title("TC#3 - verify that 1-1 is equal to 0")
@allure.description("This is a smoke Testcase which check that 1-1 is equal to 0")
@pytest.mark.smoke
def test_sub2():

    assert 1 - 1 == 0

@pytest.mark.skip(reason="Not working,Skip it")
def test_sub3():
    assert 0 - 0 != 0

#pytest -m "smoke" C:/Users/HP/PycharmProjects/PyATB5xLearning/Dec/ex_31122024_PyTest_requests_Module/test_Lab190_Pytest_Learn.py