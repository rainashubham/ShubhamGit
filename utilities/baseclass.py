import inspect
import logging

import openpyxl
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Baseclass:
    def getloggger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler("logs.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger


    def elementpresentcheck(self,text):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.LINK_TEXT, text)))

    def save_screenshot_test(self,filename):
        self.driver.get_screenshot_as_file(filename)


    def select_dropdown(self,locator,text):
        select = Select(locator)
        select.select_by_visible_text(text)
