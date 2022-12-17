import inspect
import logging
def test_logging():
    loggerName=inspect.stack()[1][3]
    logger=logging.getLogger(__name__) #method to log everything#__name__ prints name
    fileHandler=logging.FileHandler('../logfile.log')
    formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s ")
    #2022/12/17 12.40.16 :ERROR: <test case name>:Fatal error in submetting credit card
    #s will think it as a string
    fileHandler.setFormatter(formatter)#give foramt knowledge to filehandler
    logger.addHandler(fileHandler) #accept filehandler object #logger format and file

    #----------use according to requirements-----------
    logger.setLevel(logging.INFO)
    logger.debug("debug executed")
    logger.info("Information: ")
    logger.warning("Warnings: ")
    logger.error("a major error has occured")
    logger.critical("Critical Issue")

    #logs level set:
    # debug---------print all
    # info--------print all excluding debug
    # warning
    # error
    # critical
    #will open a file named logfile.log
