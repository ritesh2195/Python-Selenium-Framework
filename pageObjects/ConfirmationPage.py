from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self,driver):

        self.driver = driver

    location = (By.ID, "country")

    india = (By.LINK_TEXT, "India")

    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    purchase = (By.CSS_SELECTOR, "input[value='Purchase']")

    alertText = (By.CLASS_NAME, "alert-success")

    def setLocation(self):

        return self.driver.find_element(*ConfirmationPage.location)

    def clickLocation(self):
        return self.driver.find_element(*ConfirmationPage.india)

    def clickCheckBox(self):

        return self.driver.find_element(*ConfirmationPage.checkBox)

    def getPurchase(self):

        return self.driver.find_element(*ConfirmationPage.purchase)

    def getAlertText(self):
        return self.driver.find_element(*ConfirmationPage.alertText)