from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.welcome_id = "welcome"
        self.logout_linktxt = "Logout"

    def click_welcome(self):
        self.driver.find_element(By.ID, self.welcome_id).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_linktxt).click()
