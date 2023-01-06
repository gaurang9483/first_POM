import pytest
from config.config import TestData
from pages.home_page import HomePage
from pages.login_page import LoginPage
import XLutilities
import time


# @pytest.mark.usefixtures("init_driver")
class TestLogin:
    """
   def test_valid_login(self):
        global login_page
        login_page = LoginPage(self.driver)
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        #home_page = HomePage(self.driver)
        assert HomePage.get_logged_in_success_message() == "Login Successfully"

   """


    def test_invalid_login(self, init_driver):
        global login_page
        login_page = LoginPage(self.driver)
        row = XLutilities.getrowcount(TestData.PATHXL, 'login')
        for r in range(2, row + 1):
            username = XLutilities.readfile(TestData.PATHXL, 'login', r, 1)
            password = XLutilities.readfile(TestData.PATHXL, 'login', r, 2)
            login_page.login(username, password)
            if login_page.driver.title == "Login: Mercury Tours":
                print("test is pass")
                XLutilities.writefile(TestData.PATHXL, 'login', r, 3, "PASS")
            else:
                print("test failed")
                XLutilities.writefile(TestData.PATHXL, 'login', r, 3, "FAIL")
        time.sleep(5)

    def test_title(self, init_driver):
        global login_page
        login_page = LoginPage(self.driver)
        title = login_page.driver.title
        print(title)
        assert title == "Login: Mercury Tours"
