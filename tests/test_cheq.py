import time
from playwright.sync_api import expect
import pytest

from config import Url
from pages.repository_page import RepositoryPage


class TestCheq:
    def test_registration(self, main_page):
        main_page.open_cheq_pro()
        main_page.press_button_registration()
        main_page.enter_email()
        main_page.enter_nickname()
        # page.same_password()

    def test_login(self, main_page):
        main_page.open_cheq_pro()
        main_page.enter_email()
        main_page.enter_password_for_login()
        main_page.press_button_login()
        main_page.wait_for_url(Url.CHEQPRO_PROJECT)

    def test_open_project(self, main_page, project_page):
        self.test_login(main_page)
        project_page.open_project()
        main_page.wait_for_url(Url.CHEQPRO_REPOSITORY)

    def test_create_suite(self, main_page, project_page, repository_page):
        self.test_open_project(main_page, project_page)
        repository_page.create_suite() or repository_page.CREATE_ANOTHER_SUITE
        repository_page.enter_name_suite()
        repository_page.enter_description()
        repository_page.enter_preconditions()
        repository_page.save_suite()

    def test_log_out_of_account(self, main_page, project_page, repository_page):
        self.test_open_project(main_page, project_page)
        repository_page.log_out_of_account()
        main_page.wait_for_url(Url.CHEQPRO_REPOSITORY)
