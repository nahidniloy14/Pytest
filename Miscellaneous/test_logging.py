import inspect
import logging
def test_logging():
    # loggerName=inspect.stack()[1][3]
    logger=logging.getLogger(__name__) #method to log everything#__name__ prints name
    fileHandler=logging.FileHandler('../Reports/logfile.log')
    formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s ")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler) #accept filehandler object #logger format and file
    logger.setLevel(logging.INFO)
    # logger.debug("debug executed")
    # logger.info("Information: ")
    # logger.warning("Warnings: ")
    # logger.error("a major error has occured")
    # logger.critical("Critical Issue")
