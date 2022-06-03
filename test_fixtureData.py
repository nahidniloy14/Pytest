import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2():
    def test_editProfile(self,dataLoad): #if we have to return dataLoad
        print(dataLoad)
        print(dataLoad[1])
# @pytest.mark.usefixtures("dataLoad")
# class EditProfile(BaseClass):
#     def test_editprofile(self, dataLoad):
#         log = self.getlogger()
#         log.info(dataLoad[0])
