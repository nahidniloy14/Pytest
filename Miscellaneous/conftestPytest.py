# when fixture is required by multiple files,it will work as a common ground for all
import pytest


@pytest.fixture()
# @pytest.fixture(scope="class")#will prevent executing yeild for every function and rather it will execute once at the end
def setup():
    print(" i will execute first")
    yield
    print(" i will execute last")


@pytest.fixture()
def dataLoad():
    print("User Profile date is created")
    return ["Nahid Hassan ", "Niloy", "26"]


@pytest.fixture(params=["chrome", "firefox", "IE"])
def crossBrowser(request):  # when we have fixture with some values
    return request.param
# @pytest.fixture(params=[("chrome","Nahid","Hassan"),("firefox","Niloy"),"IE"])
# #("chrome","Niloy") 1st run #firefox 2nd run and "IE" 3rd
# def crossBrowser(request):  # when we have fixture with some values
#     return request.param