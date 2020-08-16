from selenium.webdriver.common.by import By


class ConfirmationPage:
    labeltext = (By.XPATH,"//label[@for='country']")
    countryfield = (By.CSS_SELECTOR,"input[id='country']")
    selectcountryitem = (By.XPATH,"//div[@class='suggestions']//a[text()='India']")
    confirmcheckbox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    submitclick = (By.CSS_SELECTOR,"input[type='submit']")
    successtext = (By.CSS_SELECTOR,"div.alert-dismissible")

    def __init__(self,driver):
        self.driver = driver

    def getlabel(self):
        return self.driver.find_element(*ConfirmationPage.labeltext)

    def entercountry(self):
        return self.driver.find_element(*ConfirmationPage.countryfield)

    def selectcountry(self):
        return self.driver.find_element(*ConfirmationPage.selectcountryitem)

    def selectconfirmcheckbox(self):
        return self.driver.find_element(*ConfirmationPage.confirmcheckbox)

    def submitclickbutton(self):
        return self.driver.find_element(*ConfirmationPage.submitclick)

    def successconfirmation(self):
        return self.driver.find_element(*ConfirmationPage.successtext)
