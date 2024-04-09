# TCPim03:

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



class TCPim_03:

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

    def admin(self):
        """
        funtion to login to the portal and move to admin module, locate and validate the menu options.
        """
        try:
            # boot the webpage
            self.boot()
            # Login page credentials:
            # Using explicit wait, locate and enter username details:
            WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().usernameLocator))).send_keys(data.WebData().username)
            # Using explicit wait, locate and enter password details:
            WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().passwordLocator))).send_keys(data.WebData().password)
            # Using explicit wait, locate and click the login button:
            WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locators.WebLocators().loginBtnLocator))).click()

            # Admin module:
            # Using explicit wait, locate and click the admin module option:
            WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locators.WebLocators().adminModuleLocator))).click()
            # Using explicit wait, locate the menu options:
            menuOptions= WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.CLASS_NAME, locators.WebLocators().PimModuleMenuLocator))).text
            print(f"The admin page menu has : {menuOptions}")

        except NoSuchElementException as e:
            print(e)

        finally:
            self.driver.quit()


obj = TCPim_03()
obj.admin()