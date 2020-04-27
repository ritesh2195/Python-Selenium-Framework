import time

from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import pytest


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)

        homepage.getName().send_keys(getData["firstName"])

        # self.driver.find_element_by_name("name").send_keys("ritesh")

        homepage.getEmail().send_keys(getData["lastName"])

        homepage.getPassword().send_keys("dceeevwgmail.com")

        homepage.getCheckBox().click()

        select = Select(homepage.getGender())

        select.select_by_visible_text(getData["gender"])

        homepage.getStatus().click()

        homepage.getSubmit().click()

        time.sleep(5)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param