import inspect
import logging

import pytest
@pytest.mark.usefixtures("dataLoad")
class BaseClass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)  # method to log everything#__name__ prints name
        fileHandler = logging.FileHandler('../logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s ")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # accept filehandler object #logger format and file
        logger.setLevel(logging.DEBUG)
        return logger
