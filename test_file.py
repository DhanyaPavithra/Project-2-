# Importing Data and Locator details from respective files:
from Data import data
from Locator import locators

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# importing keys
from selenium.webdriver.common.keys import Keys
# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pytest

class Test:

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.quit()

    @ pytest.mark.html
    def test_TCPim01(self,boot):
        self.driver.get(data.WebData().url)
        # Using explicit wait, locate and click the forget password link:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locators.WebLocators().forgetPwLocator))).click()
        # Using explicit wait, locate and enter username details:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().frgtPwUserNameLocator))).send_keys(data.WebData().forgetUsername)
        # Using explicit wait, locate and click the Reset Password option:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locators.WebLocators().resetPwLocator))).click()

        assert self.driver.current_url == data.WebData().pwsentURL

    @pytest.mark.html
    def test_TCPim02(self,boot):
        self.driver.get(data.WebData().url)
        # Login page credentials:
        # Using explicit wait, locate and enter username details:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().usernameLocator))).send_keys(data.WebData().username)
        # Using explicit wait, locate and enter password details:
        WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().passwordLocator))).send_keys(data.WebData().password)
        # Using explicit wait, locate and click the login button:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locators.WebLocators().loginBtnLocator))).click()

        # Admin module:
        WebDriverWait(self.driver, timeout=25).until(EC.element_to_be_clickable((By.XPATH, locators.WebLocators().adminModuleLocator))).click()
        # locators.WebLocators().clickBtn(self.driver,locators.WebLocators().adminModuleLocator)
        details = WebDriverWait(self.driver,timeout=25).until(EC.visibility_of_element_located((By.CLASS_NAME, locators.WebLocators().adminHeaderLocator))).text

        assert self.driver.title == data.WebData().title
        print(f"SUCCESS! The title of the page is {self.driver.title}")
        assert details == data.WebData().adminHeaders

    @pytest.mark.html
    def test_TCPim03(self, boot):
        self.driver.get(data.WebData().url)
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
        menuOptions = WebDriverWait(self.driver, timeout=25).until(EC.visibility_of_element_located((By.CLASS_NAME, locators.WebLocators().PimModuleMenuLocator))).text

        assert menuOptions == data.WebData().adminMenu




