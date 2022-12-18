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

"""
test_demo1.py::test_method1 Starting Execution
 i will execute first
 I am method 1
PASSED i will execute last

test_demo1.py::test_method2  i will execute first
 I am method 2
PASSED i will execute last
Stoping Execution

test_demo2.py::test_method3 Starting Execution
 i will execute first
 I am method 3
PASSED i will execute last
Stoping Execution
"""

