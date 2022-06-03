#name should start with test
import pytest
#Pycharm
@pytest.mark.testcase1
def test_message():
    print("hello")


@pytest.mark.testcase2
@pytest.mark.xfail  #mark but not report
def test_doNotTestMe():
    print("hello")
#
# # cmd
# # -k will work as a regular expression -k merthodname will run the test
# # -s prints the logs
# # -v for more info (metadata)
# # directory>py.test filename -v -s
# # -m test marked python file

#html report
#C:\Users\lm\PycharmProjects\SeleniumLearningSession\Pytest{Udemy}>py.test --html=report.html
def test_failed1():
    msg="Hello"
    assert msg == "hi","string unmatched"

def test_addition():
    a=4
    b=6
    assert a+2 == 6,"addition not matched"

def test_crossBrowser(crossBrowser):
     print(crossBrowser[0])
