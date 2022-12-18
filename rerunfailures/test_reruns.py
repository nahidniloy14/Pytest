import pytest

var1=1
var2=5

def test_one():
    assert var1 == var2
"""

#using command : pytest --reruns 4 --reruns-delay 2 test_rerunDelay.py
test_demo.py R                                                                                                                                            [100%]R [100%]R [100%]R [100%]F [100%]
                                                                                                                                          [100%]R [100%]R [100%]R [100%]F [100%]
[100%]R [100%]R [100%]F [100%]

"""
