import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EgdeService


class WebDriverWrapper:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        browser_name = "edge"

        if browser_name == "edge":
            # srv = EgdeService(executable_path=r"C:\Mine\Software\msedgedriver.exe")
            # self.driver = webdriver.Edge(service=srv)
            self.driver = webdriver.Edge()
        elif browser_name == "ff":
            self.driver = webdriver.Firefox()
        else:
            # srv = ChromeService(executable_path=C:\Mine\Software\chromedriver.exe)
            # self.driver = webdriver.Chrome(srv)
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()
