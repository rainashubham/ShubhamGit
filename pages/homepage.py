from selenium.webdriver.common.by import By

from pages.checkoutpage import CheckoutPage


class HomePage:
    shop = (By.XPATH,"//a[text()='Shop']")
    name = (By.NAME,"name")
    email = (By.XPATH,"//input[@name='email']")
    password = (By.ID,"exampleInputPassword1")
    checkbox_click = (By.XPATH,"//div[@class='form-check']/input[@class='form-check-input']")
    submit_click = (By.XPATH,"//input[contains(@class,'btn-success')]")
    text_assertion = (By.XPATH,"//div[contains(@class,'alert-success')]")
    dropdown = (By.ID,"exampleFormControlSelect1")

    def __init__(self,driver):
        self.driver = driver

    def home_shop(self):
        self.driver.find_element(*HomePage.shop).click()
        Checkoutpage = CheckoutPage(self.driver)
        return Checkoutpage

    def enter_name(self):
        return self.driver.find_element(*HomePage.name)


    def enter_email(self):
        return self.driver.find_element(*HomePage.email)


    def enter_password(self):
        return self.driver.find_element(*HomePage.password)


    def click_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox_click)


    def submit_click_button(self):
        return self.driver.find_element(*HomePage.submit_click)


    def assert_text(self):
        return self.driver.find_element(*HomePage.text_assertion)


    def dropdown_select(self):
        return self.driver.find_element(*HomePage.dropdown)