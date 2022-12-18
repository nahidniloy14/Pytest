# fixture will execute before we reach our test cases ,all the reuseable stuffs should go into the fixture
import pytest


@pytest.yield_fixture(scope='module')
def statement():
    print("Starting Execution")
    yield
    print("Stoping Execution")


@pytest.yield_fixture()
def setup():
    print(" i will execute first")
    yield
    print(" i will execute last")


def test_method1(setup,statement):
    print(" I am method 1")
def test_method2(setup,statement):
    print(" I am method 2")
def test_method3(setup,statement):
    print(" I am method 3")
"""
test_classfixture.py::test_method1 Starting Execution
 i will execute first
PASSED                                [ 33%] I am method 1
 i will execute last

test_classfixture.py::test_method2  i will execute first
PASSED                                [ 66%] I am method 2
 i will execute last

test_classfixture.py::test_method3  i will execute first
PASSED                                [100%] I am method 3
 i will execute last
Stoping Execution
"""