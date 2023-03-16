from selenium.webdriver.common.by import By


class LoginPage:

    @staticmethod
    def enter_username(driver, username):
        driver.find_element(By.NAME, "username").send_keys(username)

    @staticmethod
    def enter_password(driver,password):
        driver.find_element(By.NAME, "password").send_keys(password)