import pytest


from TestData.testdata_homepage import getdata_homepage
from pages.homepage import HomePage
from utilities.baseclass import Baseclass


class Test_HomePage(Baseclass):
    def test_formsubission(self,home_test_data):
        log = self.getloggger()
        # Entering name using Name locator
        home = HomePage(self.driver)
        home.enter_name().send_keys(home_test_data["firstname"])

        log.info(home_test_data["firstname"])

        # Entering email using xpath
        home.enter_email().send_keys(home_test_data["email"])

        log.info(home_test_data["email"])
        # Entering password  using ID
        home.enter_password().send_keys(home_test_data["password"])
        log.info(home_test_data["password"])
        # Chcecking checkbox using big relative xpath
        home.click_checkbox().click()

        # Selecting dropdown
        # Create Select Class object
        self.select_dropdown(home.dropdown_select(),"Female")

        # clicking on submit button using contains
        home.submit_click_button().click()

        # getting the text and printing it
        print(home.assert_text().text)

        log.info(home.assert_text().text)

        self.save_screenshot_test("screnshot_homepage.png")

        self.driver.refresh()

    @pytest.fixture(params=getdata_homepage.excel_utility("testcase3"))
    def home_test_data(self,request):
        return request.param

