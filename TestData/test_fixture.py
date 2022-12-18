# fixture will execute before we reach our test cases ,all the reuseable stuffs should go into the fixture
import pytest


@pytest.fixture()
def setup():
    print(" i will execute first")
    yield
    print(" i will execute last")

def test_fixture(setup):
    print(" i will execute steps in this method ")

""""
i will execute first
i will execute steps in this method
PASSED i will execute last
"""
