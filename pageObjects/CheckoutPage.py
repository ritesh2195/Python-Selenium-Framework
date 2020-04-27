from selenium.webdriver.common.by import By

from pageObjects.ConfirmationPage import ConfirmationPage


class CheckOutPage:

    def __init__(self, driver):

        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")

    cardFooter = (By.CSS_SELECTOR, ".card-footer button")

    buttonCheckout = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    finalCheckout = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):

        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):

        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def clickCheckout(self):

        return self.driver.find_element(*CheckOutPage.buttonCheckout)

    def getFinalCheckout(self):

        self.driver.find_element(*CheckOutPage.finalCheckout).click()

        confirm = ConfirmationPage(self.driver)

        return confirm