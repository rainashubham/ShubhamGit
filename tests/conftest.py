import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver

    browsername = request.config.getoption("browser_name")

    if browsername == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\pcw\\Desktop\\chromedriver.exe")
    elif browsername == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\pcw\\Desktop\\geckodriver.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
