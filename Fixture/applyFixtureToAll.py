import pytest


@pytest.mark.usefixtures("setup")
class TestData:
    def test_Demo1(self):
        print("This is a Method")
    def test_Demo2(self):
        print("This is a Method")
    def test_Demo3(self):
        print("This is a Method")
    def test_Demo4(self):
        print("This is a Method")

#this way fixture will be availble to every method











