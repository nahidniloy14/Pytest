import pytest
# @pytest.fixture()
# def setup():
#     print(" i will execute first")
#     yield
#     print(" i will execute last")
# fixture will execute before we reach our test cases
# reuseable stuffs should go into the fixture
def test_fixture(setup):
    print(" i will execute steps in this method ")

