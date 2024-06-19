import pytest

import config
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

import pytest

from pages.base_page import BasePage
from pages.main_cheq_page import MainCheqPage
from pages.project_page import ProjectPage
from pages.repository_page import RepositoryPage


@pytest.fixture
def page():  # Изменение типа возвращаемого значения
    playwright = sync_playwright().start()
    browser = get_chrome_browser(playwright)
    context = get_context(browser)
    # context = browser.new_context(record_video_dir='videos/')
    page = context.new_page()
    # Создаем экземпляр CheqPage
    yield page  # Возвращаем cheq_page вместо page_data
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()


@pytest.fixture
def main_page(page):
    return MainCheqPage(page)


@pytest.fixture
def base_page(page):
    return BasePage(page)


@pytest.fixture
def project_page(page):
    return ProjectPage(page)


@pytest.fixture
def repository_page(page):
    return RepositoryPage(page)


def get_chrome_browser(playwright) -> Browser:
    return playwright.chromium.launch(
        headless=False,
        slow_mo=config.playwright.SLOW_MO
    )


def get_context(browser) -> BrowserContext:
    context = browser.new_context(
        viewport=config.playwright.PAGE_VIEWPORT_SIZE,
    )
    context.set_default_timeout(
        timeout=config.expectations.DEFAULT_TIMEOUT
    )
    return context
