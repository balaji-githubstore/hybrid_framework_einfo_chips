from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.webdriver_listener import WebDriverWrapper


class TestAddEmployee(WebDriverWrapper):
    def test_add_valid_employee(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
        self.driver.find_element(By.NAME, "firstName").send_keys("John")
        self.driver.find_element(By.NAME, "middleName").send_keys("J")
        self.driver.find_element(By.NAME, "lastName").send_keys("wick")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        actual_profile_header = self.driver.find_element(By.XPATH, "//h6[contains(normalize-space(),'John')]").text
        # actual_profile_header = self.driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 --strong']").text
        actual_first_name = self.driver.find_element(By.NAME, "firstName").get_attribute("value")

        assert_that("John wick").is_equal_to(actual_profile_header)
        assert_that("John").is_equal_to(actual_first_name)
