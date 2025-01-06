"""
POST Request (Requests) - API Automation
- URL - [﻿restful-booker.herokuapp.com/booking](https://restful-booker.herokuapp.com/booking)
- Method - POST
- Headers -> Content-Type : application/json
- Payload - dict
- Auth  -> NA
- QP/PP -> NA
```
{
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : true,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
```

POST Response  - API Automation
- Verify the Status Code.
- Booking id > 0
- Firstname, Lastname
- Time
```
{
    "bookingid": 3691,
    "booking": {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": true,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
}
```
"""


import pytest
import allure
import requests


@allure.title("TC#1 - Create booking CRUD Positive")
@allure.description("Verify the create Booking!")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path_post = "/booking"
    # base_path_put = "/booking/1" #Id is also reuired for PUT request.

    full_url = base_url + base_path_post
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url = full_url, headers = headers, json = payload)

    response_data_json = response_data.json()
    bookingId = response_data_json["bookingid"]
    firstName = response_data_json["booking"]["firstname"]
    lastName = response_data_json["booking"]["lastname"]
    totalPrice = response_data_json["booking"]["totalprice"]
    depositPaid = response_data_json["booking"]["depositpaid"]
    checkIn = response_data_json["booking"]["bookingdates"]["checkin"]
    checkOut = response_data_json["booking"]["bookingdates"]["checkout"]
    additionalNeeds = response_data_json["booking"]["additionalneeds"]
    time = response_data.elapsed.total_seconds()

    print(bookingId)
    assert bookingId is not None
    assert bookingId > 0
    assert type(bookingId) == int
    assert firstName == "Jim"
    assert type(firstName) == str
    assert lastName == "Brown"
    # assert lastName == null
    # assert lastName == "Sinha"
    assert totalPrice == 111
    assert depositPaid == True
    assert checkIn == "2018-01-01"
    assert checkOut == "2019-01-01"
    assert additionalNeeds == "Breakfast"
    assert time < 3

@allure.title("TC#2 - Create Booking CRUD Negative")
@allure.description("Verify that invalid payload Booking is not created!")
@pytest.mark.crud
def test_create_booking_negative_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    assert response.status_code == 500
    assert response.text == "Internal Server Error"

#pytest Dec/ex_31122024_PyTest_requests_Module/test_Lab191_Pytest_POST.py