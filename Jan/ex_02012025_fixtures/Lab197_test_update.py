import pytest
import allure
import requests

def test_update_req_1(create_token, create_bookingid):
    print("Token ->", create_token)
    print("Booking ID -> ", create_bookingid)


def test_update_req_2(create_token, create_bookingid):
    print("Token ->", create_token)
    print("Booking ID -> ", create_bookingid)


def test_update_req_3(create_token, create_bookingid, read_csv_file_data):
    print("Token ->", create_token)
    print("Booking ID -> ", create_bookingid)

#pytest Jan/ex_02012025_fixtures/Lab197_test_update.py --alluredir=allure_result3
#after this allure_result3 folder is created

#at last run the command , allure serve allure_result3

