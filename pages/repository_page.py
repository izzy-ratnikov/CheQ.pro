import time

from pages.base_page import BasePage
from playwright.sync_api import Page
import config
from playwright.sync_api import expect


class RepositoryPage(BasePage):
    OPTIONS = '.options'
    SWIPE = 'back-arrow'
    BUTTON_ON_CHEQ = '.icon-btn.stroke.normal'
    ADD_CHEQ_SUITE = '.add-tooltip'
    ADD_EDIT_DELETE = '.icon-btn.stroke.small'
    DELETE_MODEL_WINDOW = '.delete-modal'
    DELETE_SUITE = '.primary-btn'
    SUITE_FORM = '.cheq-suite.root'
    CHEQ_FORM = '.cheq-row'
    BUTTON_CREATE_CHEQ = '.add-button-tertiary'
    CREATE_SUITE_MAIN = '.create-button:has-text("suite")'
    CREATE_CHEQ_MAIN = '.create-button:has-text("cheq")'
    CREATE_SUITE = '.add-btn.suite'
    CREATE_CHEQ = '.add-btn.cheq'
    NAME_CHEQ = '//*[@id="inputField"]'
    NAME_SUITE = '[placeholder="New Suite"]'
    DESCRIPTION = '//*[@id="description"]'
    PRECONDITIONS = '//*[@id="description"]'
    SAVE_SUITE = '.primary-btn'
    SAVE_CHEQ = '//*[@id="cheq-pro"]//div[4]/button[1]'
    LEFT_MENU_PANEL = '.left-menu'
    SUITES_PANEL = '.nav-panel'
    FILTERS_PANEL = '.filters'
    NUMBER_OF_SUITES = '.label.light.small.suites'
    NUMBER_OF_CHEQS = '.label.light.small:not(.suites)'
    CLOSE_FILTERS_PANEL = '.filters .icon-btn.stroke.normal'
    COLLAPSE_BUTTON = 'div.suite-header > svg'
    WINDOW_FULL_VIEW = '.view-modal.expanded'
    WINDOW_SMALL_VIEW = '.view-modal'
    DELETE_CHEQ = '.primary-btn'
    MENU_BUTTONS = '.menu-button'
    SETTING_ICON = '.icon-btn.stroke.normal'
    RENAME_BOX = '.v-field__input'
    SAVE_NEW_NAME_PROJECT = '.primary-btn'
    PROJECT_NAME = 'div.left-menu > div.avatar > h3'
    CHEQ_TYPE = '.selected:has-text("other")'
    CHEQ_STATUS = '.selected:has-text("Actual")'
    CHEQ_PRIORITY = '.selected:has-text("Not set")'
    CHEQ_BEHAVIOR = '.selected:has-text("Positive")'
    CHEQ_SEVERITY = '.selected:has-text("Not set")'
    CREATE_RUN = '.btn-block'


    def __init__(self, page):
        super().__init__(page)

    def is_suites_panel_visible(self):
        self.is_element_visible(self.SUITES_PANEL)

    def is_filters_panel_hidden(self):
        self.page.locator(self.CLOSE_FILTERS_PANEL).click()
        self.page.reload()
        self.assert_element_hidden(self.FILTERS_PANEL)

    def is_filters_panel_visible(self):
        self.is_element_visible(self.FILTERS_PANEL)

    def create_cheq(self):
        self.page.locator(f'{self.CREATE_CHEQ_MAIN}, {self.CREATE_CHEQ}').click()
        self.page.locator(self.NAME_CHEQ).click()
        self.page.locator(self.NAME_CHEQ).fill(BasePage.generate_random_string())
        self.page.locator(self.CHEQ_TYPE).click()
        self.is_element_visible(self.OPTIONS)
        self.page.locator(self.CHEQ_STATUS).click()
        self.is_element_visible(self.OPTIONS)
        self.page.locator(self.CHEQ_PRIORITY).nth(0).click()
        self.is_element_visible(self.OPTIONS)
        self.page.locator(self.CHEQ_BEHAVIOR).click()
        self.is_element_visible(self.OPTIONS)
        self.page.locator(self.CHEQ_SEVERITY).nth(1).click()
        self.is_element_visible(self.OPTIONS)
        with self.page.expect_response("**/case") as response_info:
            self.page.locator(self.SAVE_CHEQ).click()
        return response_info.value.json().get('name')

    def create_suite(self):
        self.page.locator(f'{self.CREATE_SUITE_MAIN}, {self.CREATE_SUITE}').click()
        self.page.locator(self.NAME_SUITE).click()
        self.page.locator(self.NAME_SUITE).fill(BasePage.generate_random_string())
        description = self.page.locator(self.DESCRIPTION).nth(0)
        description.click()
        description.fill(BasePage.generate_random_string())
        preconditions = self.page.locator(self.DESCRIPTION).nth(1)
        preconditions.click()
        preconditions.fill(BasePage.generate_random_string())
        self.page.locator(self.SAVE_SUITE).click()

    def press_create_cheq_button_under_suite(self):
        suite = self.page.locator(self.SUITE_FORM).nth(0)
        suite.locator(self.BUTTON_CREATE_CHEQ).click()

    def press_plus_on_suite(self):
        suite = self.page.locator(self.SUITE_FORM).nth(0)
        suite.locator(self.ADD_EDIT_DELETE).nth(0).click()

    def press_edit_on_suite(self):
        suite = self.page.locator(self.SUITE_FORM).nth(0)
        suite.locator(self.ADD_EDIT_DELETE).nth(1).click()

    def button_add_cheq_visible(self):
        add_cheq = self.page.locator(self.ADD_CHEQ_SUITE).nth(0)
        add_cheq.click()

    def button_add_suite_visible(self):
        add_suite = self.page.locator(self.ADD_CHEQ_SUITE).nth(1)
        add_suite.click()

    def delete_suite(self):
        suite = self.page.locator(self.SUITE_FORM).nth(0)
        suite.locator(self.ADD_EDIT_DELETE).nth(2).click()
        self.is_element_visible(self.DELETE_MODEL_WINDOW)
        self.page.locator(self.DELETE_SUITE).click()
        expect(self.page.locator(self.SUITE_FORM)).to_have_count(2)

    def menu_panel(self):
        self.is_element_visible(self.LEFT_MENU_PANEL)
        self.is_element_contains_text(self.NUMBER_OF_SUITES, 'Suites')
        self.is_element_contains_text(self.NUMBER_OF_CHEQS, 'Cheqs')

    def full_window_view(self):
        cheq = self.page.locator(self.CHEQ_FORM).nth(0)
        cheq.locator(self.ADD_EDIT_DELETE).nth(0).click()
        self.is_element_visible(self.WINDOW_SMALL_VIEW)
        window_view = self.page.locator(self.WINDOW_SMALL_VIEW)
        window_view.locator(self.BUTTON_ON_CHEQ).nth(2).click()
        self.is_element_visible(self.WINDOW_FULL_VIEW)

    def delete_cheq_via_view_window(self):
        window_view = self.page.locator(self.WINDOW_SMALL_VIEW)
        window_view.locator(self.BUTTON_ON_CHEQ).nth(1).click()
        self.page.locator(self.DELETE_CHEQ).click()
        expect(self.page.locator(self.CHEQ_FORM)).to_have_count(0)

    def press_collapse_button(self):
        self.page.locator(self.COLLAPSE_BUTTON).nth(0).click()
        suite = self.page.locator(self.SUITE_FORM).nth(0)
        expect(suite.locator(self.BUTTON_CREATE_CHEQ).nth(0)).to_be_hidden()

    def menu_panel_hidden(self):
        self.page.locator(self.MENU_BUTTONS).nth(2).click()
        self.assert_element_hidden(self.LEFT_MENU_PANEL)

    def rename_project(self):
        current_project_name = self.page.text_content(self.PROJECT_NAME)
        self.is_element_contains_text(self.PROJECT_NAME, current_project_name)
        self.page.locator(self.SETTING_ICON).nth(0).click()
        self.page.locator(self.RENAME_BOX).click()
        self.page.locator(self.RENAME_BOX).fill(BasePage.generate_random_string())
        self.page.locator(self.SAVE_NEW_NAME_PROJECT).click()
        new_project_name = self.page.text_content(self.PROJECT_NAME)
        self.is_element_contains_text(self.PROJECT_NAME, new_project_name)

    def switch_to_cheq_runs(self):
        self.page.locator(self.MENU_BUTTONS).nth(1).click()
        self.page.locator(self.CREATE_RUN).click()

