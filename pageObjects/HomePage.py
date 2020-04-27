from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    name = (By.NAME, "name")

    email = (By.CSS_SELECTOR, "input[name='email']")

    password = (By.CSS_SELECTOR, "#exampleInputPassword1")

    checkBox = (By.CSS_SELECTOR, "#exampleCheck1")

    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")

    status = (By.CSS_SELECTOR, "#inlineRadio1")

    submit = (By.XPATH, "//input[@value='Submit']")

    def shopItem(self):

        self.driver.find_element(*HomePage.shop).click()

        checkout = CheckOutPage(self.driver)

        return checkout

    def getName(self):

        return self.driver.find_element(*HomePage.name)

    def getEmail(self):

        return self.driver.find_element(*HomePage.email)

    def getPassword(self):

        return self.driver.find_element(*HomePage.password)

    def getStatus(self):

        return self.driver.find_element(*HomePage.status)

    def getCheckBox(self):

        return self.driver.find_element(*HomePage.checkBox)

    def getGender(self):

        return self.driver.find_element(*HomePage.gender)

    def getSubmit(self):

        return self.driver.find_element(*HomePage.submit)