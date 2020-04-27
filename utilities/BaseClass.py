import inspect
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import logging

@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        file = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file.setFormatter(formatter)
        fileHandler = logger.addHandler(file)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresense(self, text):

        wait = WebDriverWait(self.driver, 20)

        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))
