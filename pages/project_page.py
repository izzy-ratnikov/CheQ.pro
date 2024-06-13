from playwright.sync_api import Page
import config
from pages.base_page import BasePage


class ProjectPage(BasePage):
    BUTTON_OPEN_CREATE_PROJECT = '//*[@id="cheq-pro"]//div[1]//div/i'
    # INPUT_PROJECT_NAME = '//*[@id="input-16"]'
    CREATE_PROJECT = '//body/div[2]//button[1]/span'
    OPEN_PROJECT = '.open-button'

    def press_button_create_project(self):
        self.page.locator(self.BUTTON_OPEN_CREATE_PROJECT).click()

    # def input_project_name(self):
    #     self.page.locator(self.INPUT_PROJECT_NAME).click()
    #     self.page.locator(self.INPUT_PROJECT_NAME).fill(BasePage.generate_random_string())

    def create_project(self):
        self.page.locator(self.CREATE_PROJECT).click()

    def open_project(self):
        self.page.locator(self.OPEN_PROJECT).click()
