from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_id = "txtUsername"
        self.password_id = "txtPassword"
        self.login_id = "btnLogin"

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def enter_pw(self, pw):
        self.driver.find_element(By.ID, self.password_id).send_keys(pw)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_id).click()



