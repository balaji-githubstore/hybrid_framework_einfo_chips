from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from assertpy import assert_that



class TestLoginUI:
    def test_title(self):
        serv_driver = Service(executable_path=r"C:\Users\JiDi\Downloads\chromedriver_win32 (5)\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_driver)
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        actual_title = driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)
