from playwright.sync_api import Page
import config
from pages.base_page import BasePage
from pages.project_page import ProjectPage


class MainCheqPage(ProjectPage):
    EMAIL = '[placeholder="mymail@mail.com"]'
    PASSWORD_FOR_LOGIN = '//*[@id="input-4"]'
    LOGIN = '//*[@id="cheq-pro"]//div[2]//span[3]'

    def log_in_to_account(self):
        self.page.goto(config.url.CHEQPRO)
        self.page.locator(self.EMAIL).click()
        self.page.locator(self.EMAIL).fill("iamratnikov@yandex.by")
        self.page.locator(self.PASSWORD_FOR_LOGIN).click()
        self.page.locator(self.PASSWORD_FOR_LOGIN).fill("golova26")
        self.page.locator(self.LOGIN).click()
