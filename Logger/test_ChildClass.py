import pytest
from pytest.Logger.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class EditProfile(BaseClass):
    def test_editProfile(self, dataLoad):
        log = self.getlogger()
        log.info(dataLoad[0])
