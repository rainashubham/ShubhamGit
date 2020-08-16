from selenium.webdriver.common.by import By

from pages.confirmationpage import ConfirmationPage


class CheckoutPage:

    productslist = (By.XPATH,"//div[@class='card h-100']")
    productname = (By.CSS_SELECTOR, ".card-title a")
    productselect = (By.XPATH,"//div[@class='card h-100']/div/button")
    checkclickbutton = (By.CSS_SELECTOR,"a.btn-primary")
    confirmcheckbutton = (By.XPATH,"//button[@class='btn btn-success']")

    def __init__(self,driver):
        self.driver = driver

    def getproductslist(self):
        return self.driver.find_elements(*CheckoutPage.productslist)

    def getproductname(self):
        return self.driver.find_elements(*CheckoutPage.productname)

    def selectproduct(self):
        return self.driver.find_elements(*CheckoutPage.productselect)

    def checkoutclick(self):
        return self.driver.find_element(*CheckoutPage.checkclickbutton)

    def confirmcheck(self):
        self.driver.find_element(*CheckoutPage.confirmcheckbutton).click()
        Confirmation = ConfirmationPage(self.driver)
        return Confirmation

