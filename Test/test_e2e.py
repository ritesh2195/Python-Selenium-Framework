import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmationPage import ConfirmationPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# pytest.mark.usefixtures("setup")


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()

        homePage = HomePage(self.driver)

        checkoutPage = homePage.shopItem()

        log.info("click on shop link")

        # checkoutPage = CheckOutPage(self.driver)

        cards = checkoutPage.getCardTitle()

        i = -1

        for card in cards:
            i = i + 1
            cardText = card.text

            log.info(card.text)

            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        checkoutPage.clickCheckout().click()

        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        confirmPage = checkoutPage.getFinalCheckout()

        # confirmPage = ConfirmationPage(self.driver)

        confirmPage.setLocation().send_keys("ind")

        log.info("entering country name")

        # self.driver.find_element_by_id("country").send_keys("ind")

        self.verifyLinkPresense("India")

        # wait = WebDriverWait(self.driver, 20)

        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        confirmPage.clickLocation().click()

        # self.driver.find_element_by_link_text("India").click()

        confirmPage.clickCheckBox().click()

        log.info("clicked on checkbox")

        # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

        confirmPage.getPurchase().click()

        log.info("clicked on purchase button")

        # self.driver.find_element_by_css_selector("input[value='Purchase']").click()

        confirmation = confirmPage.getAlertText()

        # confirmation = self.driver.find_element_by_class_name("alert-success").text

        print(confirmation)
