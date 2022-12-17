import pytest


def greet():
    print("Hello World")
@pytest.mark.smoke
def GreetCreditCardOwner():
    print("Customer")
