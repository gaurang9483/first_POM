from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(by))
        element.click()

    def send_keys(self, by, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(by))
        element.send_keys(text)

    def get_element_text(self, by):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(by))
        return element.text

    def get_page_title(self, title):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(title))
        return self.driver.title

    def wait_and_get_page_title(self, title):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_is(title))
        return self.driver.title
