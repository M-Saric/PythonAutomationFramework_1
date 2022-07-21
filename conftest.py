import pytest
from selenium.webdriver.edge.service import Service
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--govno", action="store", default="chrome", help="Type in browser name")


@pytest.fixture(scope="class")  # moze da bude i fucntion onda krece posle svake fje
# ili class ako se pravi class, session radi kao setup i teardown u unit testu
def test_setup(request):

    browser = request.config.getoption("--govno")
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(
            "C:/Users/sarmil/PycharmProjects/AutomationFramework_1/drivers/chromedriver.exe"))
    elif browser == "edge":
        driver = webdriver.Edge(service=Service(
            "C:/Users/sarmil/PycharmProjects/AutomationFramework_1/drivers/msedgedriver.exe"))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=Service(
            "C:/Users/sarmil/PycharmProjects/AutomationFramework_1/drivers/geckodriver.exe"))

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed!")
