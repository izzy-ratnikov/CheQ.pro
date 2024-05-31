from pages.base_page import BasePage
from playwright.sync_api import Page
import config


class RepositoryPage(BasePage):
    CREATE_SUITE = '//*[@id="cheq-pro"]//div[2]//div[2]/button[2]'
    CREATE_ANOTHER_SUITE = '.add-btn.suite'
    NAME_SUITE = '[placeholder="New Suite"]'
    DESCRIPTION = '//*[@id="description"]'
    PRECONDITIONS = '//*[@id="description"]'
    SAVE_SUITE = '.primary-btn'
    EXIT = '//*[@id="cheq-pro"]/div[1]/i'

    def create_suite(self):
        self.page.locator(self.CREATE_SUITE).click()

    def enter_name_suite(self):
        self.page.locator(self.NAME_SUITE).click()
        self.page.locator(self.NAME_SUITE).fill(BasePage.generate_random_string())

    def enter_description(self):
        description = self.page.locator(self.DESCRIPTION).nth(0)
        description.click()
        description.fill(BasePage.generate_random_string())

    def enter_preconditions(self):
        preconditions = self.page.locator(self.DESCRIPTION).nth(1)
        preconditions.click()
        preconditions.fill(BasePage.generate_random_string())

    def save_suite(self):
        self.page.locator(self.SAVE_SUITE).click()

    def log_out_of_account(self):
        self.page.locator(self.EXIT).click()

    def create_another_suite(self):
        self.page.locator(self.CREATE_ANOTHER_SUITE).click()
