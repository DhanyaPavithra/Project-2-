# TCPim01:

# importing data and locator details from files
from Data import data
from Locator import locators

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# importing exceptions
from selenium.common.exceptions import NoSuchElementException

# importing explicit waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResetPassword:

    def __init__(self):
        # initializing the driver:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """
        to boot the webpage with the url

        """
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()

    def quit(self):
        """
        to quit the webpage

        """
        self.driver.quit()

    def forgetPw(self):
        """
        function to test the forget password link in the login page
        """

        try:
            # boot the webpage
            self.boot()
            # Using explicit wait, locate and click the forget password link:
            WebDriverWait(self.driver,timeout=25).until(EC.element_to_be_clickable((By.XPATH, locators.WebLocators().forgetPwLocator))).click()
            # Using explicit wait, locate and enter username details:
            WebDriverWait(self.driver,timeout=25).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().frgtPwUserNameLocator))).send_keys(data.WebData().forgetUsername)
            # Using explicit wait, locate and click the Reset Password option:
            WebDriverWait(self.driver,timeout=25).until(EC.element_to_be_clickable((By.XPATH, locators.WebLocators().resetPwLocator))).click()

            print("Reset Password Link sent successfully ")

        except NoSuchElementException as e:
            print(e)

        finally:
            self.driver.quit()


obj = ResetPassword()
obj.forgetPw()

