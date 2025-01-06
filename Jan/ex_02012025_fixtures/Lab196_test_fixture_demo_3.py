import pytest


@pytest.fixture()
def create_token():
    return "abc"


@pytest.fixture()
def create_booking_id():
    return 123



def test_update_req(create_token, create_booking_id):
    print("Token : ", create_token)
    print("Booking ID : ", create_booking_id)