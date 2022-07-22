from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.chrome.service import Service
import pytest
from pages.Login_page import LoginPage
from pages.HomePage import HomePage
from utils import utils
import allure
import moment

@pytest.mark.usefixtures("test_setup")
class TestLogin:
    # @pytest.fixture(scope="session")  #moze da bude i function onda krece posle svake fje ili class ako se pravi class
    # def test_setup(self):
    #     global driver
    #     driver = webdriver.Edge(service=Service(
    #         "C:/Users/sarmil/PycharmProjects/AutomationFramework_1/drivers/msedgedriver.exe"))
    #     driver.maximize_window()
    #     yield
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed!")

    def test_login(self):
        self.driver.get(utils.URL)

        LoginPage(self.driver).enter_username(utils.USERNAME)
        LoginPage(self.driver).enter_pw(utils.PASSWORD)
        self.driver.implicitly_wait(2)
        LoginPage(self.driver).click_login()

    def test_logout(self):
        try:
            HomePage(self.driver).click_welcome()
            self.driver.implicitly_wait(2)
            HomePage(self.driver).click_logout()
            assert self.driver.title == "OrangeHRM"
        except AssertionError:
            print("There was an exception")
            print(AssertionError)
            # scrname = "screenshot" + moment.now().strftime("%d-%m-%Y_%H:%M:%S")

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=utils.whoami() + moment.now().strftime("%d-%m-%Y_%H:%M:%S"),
                attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_(
                "C:/Users/sarmil/PycharmProjects/AutomationFramework_1/screenshots" + utils.whoami() + moment.now().strftime("%d-%m-%Y_%H:%M:%S") + ".png")
            raise
        except:
            print("There was an exception")
            raise
