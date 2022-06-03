import pytest
@pytest.mark.testcase1
def test_failed2():
    msg="Hello"
    assert msg == "hi","string unmatched"

@pytest.mark.skip #will skip this test
def test_skipped():
   print("I am skipped")
