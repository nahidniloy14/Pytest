import pytest


def test_Bank():
    print("Dhaka Bank Limited")


@pytest.mark.xfail
#this method wil run but it will not report any bugs regarding this test method
def test_CreditCardInfo():
    a = 100000
    b = 0.4
    balance = a * b
    print("Account Balance", +balance)
