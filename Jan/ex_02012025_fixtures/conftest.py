import pytest
import requests
from dotenv import load_dotenv
import os



@pytest.fixture()
def create_token():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username, password)
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username" : "admin",
        "password" : "password123"
    }
    response_data = requests.post(url = url, headers= headers, json = json_payload)
    response_data_json = response_data.json()
    token = response_data_json["token"]
    print(token)
    return token

@pytest.fixture()
def create_bookingid():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
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

    response_data = requests.post(url = url, headers = headers, json = payload)
    print(type(url))
    print(type(headers))
    print(type(payload))

    response_data_json = response_data.json()
    bookingid = response_data_json["bookingid"]
    print(bookingid)
    return bookingid

@pytest.fixture
def read_csv_file_data():
    pass


@pytest.fixture
def read_mysql_file_database():
    pass


@pytest.fixture
def read_url_testdata_excel():
    pass


@pytest.fixture
def launch_browser():
    print("Launching a Browser!! Chrome")
    return "chrome"


@pytest.fixture
def close_browser():
    print("Closing a Browser!! Chrome")
    return "Closed"