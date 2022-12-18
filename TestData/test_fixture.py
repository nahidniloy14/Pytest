import pytest


@pytest.fixture()
def greet():
    print("Good Morning")


def test_employee(greet):
    print("How you doin?")


def test_HR(greet):
    print("How are you,Sir?")


def test_staff(greet):
    print("whatss up??")

"""
test_fixture2.py::test_employee Good Morning
PASSED                                   [ 33%]How you doin?

test_fixture2.py::test_HR Good Morning
PASSED                                         [ 66%]How are you,Sir?

test_fixture2.py::test_staff Good Morning
PASSED                                      [100%]whatss up??
"""