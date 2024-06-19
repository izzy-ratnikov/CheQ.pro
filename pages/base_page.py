import random
import string
from time import sleep
import allure
from playwright.sync_api import Page, expect

from config import Url


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @classmethod
    def generate_random_string(cls, string_length=8):
        """Генерирует случайную строку заданной длины"""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(string_length))

    @classmethod
    def generate_random_email(cls):
        """Генерирует случайный email"""
        return f"{cls.generate_random_string()}@{cls.generate_random_string()}.com"

    @classmethod
    def generate_random_password(cls, password_length=10):
        """Генерирует случайный пароль"""
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for _ in range(password_length))

    def wait_for_url_change(self, expected_url):
        with allure.step(f"Ожидание изменения URL на {expected_url}"):
            self.page.wait_for_url(expected_url)

    def assert_element_hidden(self, selector):
        expect(self.page.locator(selector)).to_be_hidden()

    def is_element_visible(self, selector):
        with allure.step(f"Проверка видимости элемента: {selector}"):
            expect(self.page.locator(selector)).to_be_visible()

    def is_element_contains_text(self, selector, text):
        expect(self.page.locator(selector)).to_contain_text(text)

    def wait_five_seconds(self):
        self.page.wait_for_timeout(5000)

    def inner_text(self, locator):
        self.page.inner_text(locator)
