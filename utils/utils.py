#CONSTANTS
import inspect
import allure
import moment


URL = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"


def whoami():
    return inspect.stack()[1][3]

def allureScreenshot():
    allure.attach(self.driver.get_screenshot_as_png(),
                name=utils.whoami() + moment.now().strftime("%d-%m-%Y_%H:%M:%S"),
                attachment_type=allure.attachment_type.PNG)

