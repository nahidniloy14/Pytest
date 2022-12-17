# reusable stuffs should go into the fixture
import pytest


@pytest.fixture()
def setup():
    print("I am header")
    yield  # will wait until the header gets printed and then after it will to start working with the footer
    print("I am footer")


def test_FixtureDemo(setup):
    print("I am the body")
