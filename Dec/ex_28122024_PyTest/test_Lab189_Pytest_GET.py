"""
GET Request Automation?

1. URL -> [﻿restful-booker.herokuapp.com/booking/1](https://restful-booker.herokuapp.com/booking/1)
2. Auth -> NA
3. Payload -> NA
4. Content - Type - Application JSON - NA
5. Query Param -> NA
6. Path Param. - 1 -> [﻿booking/1](https://restful-booker.herokuapp.com/booking/1)


GET Response Automation

- `Body -> Verify - Assert. , # Keys, Values`
- `Status Code -> Verify`
- Time
- Headers
- **JSON Schema**


"""


import pytest
import allure
import requests

@allure.title("Verify the GET Request of Restful Booker")
@allure.description("This Testcase check Booking 1 and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    url_get = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url_get)
    assert response_data.status_code == 200

@allure.title("Verify the GET Request of Restful Booker with invalid ID")
@allure.description("This Testcase check Booking -1 and verify the response")
@pytest.mark.positive
def test_get_request_negative():
    url_get = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url_get)
    assert response_data.status_code != 200
    # assert response_data.status_code == 404



#pip install requests


#pytest Dec/ex_28122024_PyTest/test_Lab189_Pytest_GET.py --alluredir=allure_results

#To see the result, pytest Dec/ex_28122024_PyTest/test_Lab189_Pytest_GET.py --alluredir=allure_results -s
#after this allure_result folders is created

#at last run the command , allure serve allure_results