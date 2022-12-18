import pytest
# -----------Install pytest Order
# pip3 install pytest-ordering

@pytest.mark.run(order=2)
def test_method1():
    print(" I am method 1")
@pytest.mark.run(order=3)
def test_method2():
    print(" I am method 2")
@pytest.mark.run(order=1)
def test_method3():
    print(" I am method 3")

"""
test_runOrder.py::test_method3  I am method 3
PASSED
test_runOrder.py::test_method1  I am method 1
PASSED
test_runOrder.py::test_method2  I am method 2
PASSED
"""