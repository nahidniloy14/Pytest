import pytest
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_failed2(self):
        msg = "Hello"
        assert msg == "hi", "string unmatched"

    def test_skipped(self):
        print("I am skipped")
