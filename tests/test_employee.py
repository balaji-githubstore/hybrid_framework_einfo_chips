import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.webdriver_listener import WebDriverWrapper


class TestAddEmployee(WebDriverWrapper):
    def test_add_valid_employee(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH,"//span[normalize-space()='PIM']").click()
        self.driver.find_element(By.LINK_TEXT,"Add Employee").click()
        # enter first name as John
        self.driver.find_element(By.NAME, "firstName").send_keys("John")
        self.driver.find_element(By.NAME, "middleName").send_keys("J")
        self.driver.find_element(By.NAME, "lastName").send_keys("wick")
        time.sleep(5)
        # self.driver.find_element(By.XPATH, "//label[normalize-space()='Employee Id']/following::input").clear()

        action=webdriver.ActionChains(self.driver)
        ele=self.driver.find_element(By.XPATH, "//label[normalize-space()='Employee Id']/following::input")
        action.click(ele).key_down(webdriver.Keys.CONTROL)\
            .send_keys("a").key_up(webdriver.Keys.CONTROL)\
            .send_keys(webdriver.Keys.DELETE).perform()

        self.driver.find_element(By.XPATH,"//label[normalize-space()='Employee Id']/following::input").send_keys("988")
        time.sleep(5)
        # enter middle name as J
        # enter lastname as wick
        # click on save
        # Assert the profile header as John Wick
        # Assert the Firstname textbox should contain value as John
