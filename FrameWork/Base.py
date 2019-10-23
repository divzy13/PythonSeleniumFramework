import selenium
from selenium import webdriver
from Data.config import Settings
from selenium.webdriver.common.by import By


# EXE_PATH = r'C:\Users\divya.raveendran\PycharmProjects\PythonSeleniumFramework\Drivers\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=EXE_PATH)
# driver.get('https://www.google.com/')


class BaseApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = BaseApp()
            return cls.instance

    def __init__(self):
        if str(Settings["Browser"]).lower() is "chrome":
            # EXE_PATH = r'C:\Users\divya.raveendran\PycharmProjects\PythonSeleniumFramework\Drivers\chromedriver.exe'
            # self.driver = webdriver.Chrome(executable_path=EXE_PATH)
            self.driver = webdriver.Chrome(Settings["Path"])

        else:
            print('Wrong browser selection')

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(Settings["URL"])


BaseApp = BaseApp.get_instance()
