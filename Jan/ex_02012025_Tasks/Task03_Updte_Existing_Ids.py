# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and
# Verify using GET by id.


import pytest
import requests

base_url = "https://restful-booker.herokuapp.com"


def get_token():
    path_post = "/auth"
    full_url = base_url + path_post
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username" : "admin",
        "password" : "password123"
    }

    response_data = requests.post(url = full_url, headers= headers, json = json_payload)
    response_data_json = response_data.json()
    token = response_data_json["token"]
    assert  response_data.status_code == 200
    return token


def get_request_positive():
    booking_path = "/booking"
    url_get = base_url + booking_path
    response_data = requests.get(url=url_get)
    response_data_json = response_data.json()
    print(response_data_json)
    print ("We will update : ", response_data_json[0]["bookingid"])
    # assert response_data.status_code == 200
    return (response_data_json[0]["bookingid"])


def put_reuest():
    token = get_token()
    booking_id_upd = get_request_positive()

    print(token)
    print(booking_id_upd)

    base_path = "/booking/" + str(booking_id_upd)
    full_url_put = base_url + base_path
    cookie = "token=" + token

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": cookie

    }

    json_payload = {
        "firstname": "Damini", #Updating First Name.
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2020-12-01" #Updating Checkout Date.
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=full_url_put, headers = headers, json=json_payload)
    print("Updating the First Name & Deposit Paid of Booking with Id : ", booking_id_upd)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Damini"
    assert response.json()["bookingdates"]["checkout"] == "2020-12-01"
    print(response.json()["firstname"])
    print(response.json()["bookingdates"]["checkout"])
    return booking_id_upd

def test_get_request():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    booking_id_get = put_reuest()
    GET_URL = base_url + str(booking_id_get)
    response_data = requests.get(url = GET_URL)
    response_data_json = response_data.json()
    assert response_data.status_code == 200
    assert response_data.json()["firstname"] == "Damini"
    assert response_data.json()["bookingdates"]["checkout"] == "2020-12-01"
    print("We are getting updated value of First Name & Checkout Date for " + str(booking_id_get))
