from selenium import webdriver
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge(
    service=Service("C:/Users/sarmil/PycharmProjects/AutomationFramework_1/drivers/msedgedriver.exe"))

driver.get("https://itsmycode.com/executable-path-has-been-deprecated/")

driver.close()
print("JEAAAAAAAAA")