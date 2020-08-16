from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.checkoutpage import CheckoutPage
from pages.confirmationpage import ConfirmationPage
from pages.homepage import HomePage
from utilities.baseclass import Baseclass


class Test_E2E(Baseclass):
    def test_demo(self):
        log = self.getloggger()
        Home = HomePage(self.driver)
        Checkout = Home.home_shop()
        log.info("Entering checkout shop")
        cards = Checkout.getproductname()

        i = -1

        for card in cards:
            i = i + 1
            cardtxt = card.text
            log.info(cardtxt)
            print(cardtxt)
            if cardtxt == "Blackberry":
                Checkout.selectproduct()[i].click()


        Checkout.checkoutclick().click()

        self.save_screenshot_test("screenshot.png")

        Confirmation = Checkout.confirmcheck()

        labeltext = Confirmation.getlabel().text

        assert "delivery location." in labeltext

        Confirmation.entercountry().send_keys("Ind")

        self.elementpresentcheck("India")

        Confirmation.selectcountry().click()

        Confirmation.selectconfirmcheckbox().click()

        Confirmation.submitclickbutton().click()

        finalsuccess = Confirmation.successconfirmation().text

        assert self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']/input").is_selected()

        assert "Success!" in finalsuccess

        log.info(f"Message received: {finalsuccess}")

        self.save_screenshot_test("screenshot1.png")

