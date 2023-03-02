from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from assertpy import assert_that
from selenium.webdriver.common.by import By


class TestLoginUI:
    def test_title(self):
        serv_driver = Service(executable_path=r"C:\Users\JiDi\Downloads\chromedriver_win32 (5)\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_driver)
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        actual_title = driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        serv_driver = Service(executable_path=r"C:\Users\JiDi\Downloads\chromedriver_win32 (5)\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_driver)
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        actual_header = driver.find_element(By.XPATH, "//h5").text
        assert_that("Login").is_equal_to(actual_header)
