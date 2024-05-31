from playwright.sync_api import Page
import config
from pages.base_page import BasePage
from pages.project_page import ProjectPage


class MainCheqPage(ProjectPage):
    REGISTRATION_BUTTON = '.registration-btn'
    EMAIL = '[placeholder="mymail@mail.com"]'
    NICKNAME = '[placeholder="Nickname"]'
    PASSWORD_1 = '//*[@id="cheq-pro"]//form/div[3]/div[1]'
    PASSWORD_2 = '//*[@id="input-92"]'
    CONFIRM_PASSWORD = '//*[@id="cheq-pro"]//form/div[4]'
    BUTTON_CREATE_ACCOUNT = '//*[@id="cheq-pro"]//div[2]//span[3]'
    PASSWORD_FOR_LOGIN = '//*[@id="input-4"]'
    LOGIN = '//*[@id="cheq-pro"]//div[2]//span[3]'

    def open_cheq_pro(self) -> None:
        self.page.goto(config.url.CHEQPRO)

    def press_button_registration(self):
        self.page.locator(self.REGISTRATION_BUTTON).click()

    def enter_email(self):
        self.page.locator(self.EMAIL).click()
        self.page.locator(self.EMAIL).fill("iamratnikov@yandex.by")

    def enter_nickname(self):
        self.page.locator(self.NICKNAME).click()
        self.page.locator(self.NICKNAME).fill("Golova")

    def same_password(self):
        password = BasePage.generate_random_password()
        self.page.locator(self.PASSWORD_1).click()
        self.page.locator(self.PASSWORD_2).fill(password)
        # self.page.locator(self.CONFIRM_PASSWORD).click()
        # self.page.locator(self.CONFIRM_PASSWORD).fill(password)

    def press_button_create_account(self):
        self.page.locator(self.BUTTON_CREATE_ACCOUNT).click()

    def enter_password_for_login(self):
        self.page.locator(self.PASSWORD_FOR_LOGIN).click()
        self.page.locator(self.PASSWORD_FOR_LOGIN).fill("golova26")

    def press_button_login(self):
        self.page.locator(self.LOGIN).click()

    # def input_project_name(self):
    #     self.page.locator(self.INPUT_PROJECT_NAME).click()
    #     self.page.locator(self.INPUT_PROJECT_NAME).fill(BasePage.generate_random_string())
