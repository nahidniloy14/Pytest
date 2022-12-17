import pytest


def test_Bank():
    print("Dhaka Bank Limited")


@pytest.mark.skip
#this method wil be skipped in the test
def test_CreditCardInfo():
    a = 100000
    b = 0.4
    balance = a * b
    print("Account Balance", +balance)
