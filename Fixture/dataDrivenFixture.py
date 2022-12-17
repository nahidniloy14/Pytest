import pytest


@pytest.mark.usefixtures("dataLoad")

def test_profile(dataLoad):
    print(dataLoad)


# if we want to return data we should pass fixture name also
