"""
POST Request (Requests) - API Automation
- URL - [﻿restful-booker.herokuapp.com/auth
- Method - POST
- Headers -> Content-Type : application/json
- Payload - dict
- Auth  -> NA
- QP/PP -> NA
```
{
    "username" : "admin",
    "password" : "password123"
}
```

POST Response  - API Automation
- Verify the Status Code.
- token
- Time
```
{
    "token": "f36141fc455829b"
}
```
"""

import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"
headers = { "Content-Type" : "application/json" }

@allure.title("TC01 - Create Token")
@allure.description("Verify that a token is created with valid username and password.")
@pytest.mark.smoke
def test_create_token():
    path_post = "/auth"
    full_url = base_url + path_post
    json_payload = {
        "username" : "admin",
        "password" : "password123"
    }

    response_data = requests.post(url = full_url, headers= headers, json = json_payload)
    print(response_data)
    response_data_json = response_data.json()
    token = response_data_json["token"]
    assert  response_data.status_code == 200
    print(token)
    assert type(token) == str
    assert len(token) > 0

#pytest -m "smoke" C:/Users/HP/PycharmProjects/PyATB5xLearning/Dec/ex_31122024_PyTest_requests_Module/test_Lab192_Pytest_Create_Token_POST.py --alluredir=allure_result2
#after this allure_result2 folder is created

#at last run the command , allure serve allure_result2
