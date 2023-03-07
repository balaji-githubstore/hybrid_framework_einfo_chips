import pytest


class TestAddEmployee:
    def test_add_valid_employee(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        # click on PIM menu
        # click on Add Employee
        # enter first name as John
        # enter middle name as J
        # enter lastname as wick
        # click on save
        # Assert the profile header as John Wick
        # Assert the Firstname textbox should contain value as John
