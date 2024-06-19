import time
from playwright.sync_api import expect
import pytest
from config import Url
from pages.repository_page import RepositoryPage


class TestCheq:

    def test_login(self, main_page):
        main_page.log_in_to_account()
        main_page.wait_for_url(Url.CHEQPRO_PROJECT)

    def test_open_project(self, main_page, project_page):
        main_page.log_in_to_account()
        project_page.open_project()
        main_page.wait_for_url(Url.CHEQPRO_REPOSITORY)

    def test_create_suite(self, main_page, project_page, repository_page, base_page):
        main_page.log_in_to_account()
        project_page.open_project()
        repository_page.create_suite()

    def test_button_create_cheq_visible(self, main_page, project_page, repository_page):
        main_page.log_in_to_account()
        project_page.open_project()
        repository_page.create_suite()
        repository_page.press_create_cheq_button_under_suite()

    def test_filters_and_suites_panels_visible(self, main_page, project_page, repository_page):
        main_page.log_in_to_account()
        project_page.open_project()
        repository_page.create_suite()
        repository_page.is_suites_panel_visible()
        repository_page.is_filters_panel_visible()

    def test_filters_panel_hidden(self, main_page, project_page, repository_page):
        main_page.log_in_to_account()
        project_page.open_project()
        repository_page.create_suite()
        repository_page.is_filters_panel_hidden()

    def test_create_cheq(self, main_page, project_page, repository_page):
        main_page.log_in_to_account()
        project_page.open_project()
        repository_page.create_cheq()

    def test_press_plus_and_add_cheq(self, main_page, project_page, repository_page):
        main_page.log_in_to_account()
        project_page.open_project()
        repository_page.create_suite()
        repository_page.press_plus_on_suite()
        repository_page.button_add_cheq_visible()

    def test_add_suite(self, main_page, project_page, repository_page):
        main_page.log_in_to_account()
        project_page.open_project()
        repository_page.create_suite()
        repository_page.press_plus_on_suite()
        repository_page.button_add_suite_visible()

    # def test_delete_suite(self, main_page, project_page, repository_page):
    #     main_page.log_in_to_account()
    #     project_page.open_project()
    #     repository_page.create_suite()
    #     repository_page.delete_suite()

    def test_menu_panel(self, main_page, project_page, repository_page):
        main_page.log_in_to_account()
        project_page.open_project()
        repository_page.menu_panel()

    def test_side_window_cheq(self, main_page, project_page, repository_page):
        main_page.log_in_to_account()
        project_page.open_project()
        repository_page.create_cheq()
        repository_page.full_window_view()

    def test_collapse_button(self, main_page, project_page, repository_page):
        main_page.log_in_to_account()
        project_page.open_project()
        repository_page.create_suite()
        repository_page.press_collapse_button()

    # def test_delete_cheq_via_side_window(self, main_page, project_page, repository_page):
    #     main_page.log_in_to_account()
    #     project_page.open_project()
    #     repository_page.create_cheq()
    #     repository_page.full_window_view()
    #     repository_page.delete_cheq_via_view_window()

    def test_menu_hidden(self, main_page, project_page, repository_page):
        main_page.log_in_to_account()
        project_page.open_project()
        repository_page.menu_panel_hidden()

    def test_rename_project(self, main_page, project_page, repository_page):
        main_page.log_in_to_account()
        project_page.open_project()
        repository_page.rename_project()
