import pytest


@pytest.fixture()
def before_run():
    print("Before Run")
    return True


def test_update(before_run):
    assert before_run == True
    print("Updating")