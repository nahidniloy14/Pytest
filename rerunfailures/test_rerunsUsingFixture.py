import pytest

var1=1
var2=5
@pytest.mark.flaky(reruns=5)
def test_one():
    assert var1 == var2

"""
test_demo.py::test_one RERUN
test_demo.py::test_one RERUN
test_demo.py::test_one RERUN
test_demo.py::test_one RERUN
test_demo.py::test_one RERUN
test_demo.py::test_one FAILED


#using command
test_demo.py R                                                                                                                                            [100%]R [100%]R [100%]R [100%]F [100%]
                                                                                                                                          [100%]R [100%]R [100%]R [100%]F [100%]
[100%]R [100%]R [100%]F [100%]

"""
