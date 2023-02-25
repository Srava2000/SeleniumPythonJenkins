import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class MyTestCase(unittest.TestCase):
    def test01(self):
        filePath = "C:\\Users\\srava\\PycharmProjects\\SeleniumPythonProject\\drivers\\chromedriver.exe"

        url = "https://parabank.parasoft.com/parabank/index.htm"

        driver = webdriver.Chrome(filePath)

        time.sleep(1)

        driver.get(url)

        time.sleep(1)

        # Xpath
        loginButton = driver.find_element(By.XPATH, "//input[@value='Log In']")
        loginButton.click()

        # CSS Selector
        # loginButton = driver.find_element(By.CSS_SELECTOR, "input[value='Log In']")
        # loginButton.click()

        time.sleep(1)

        driver.quit()

if __name__ == '__main__':
    unittest.main()