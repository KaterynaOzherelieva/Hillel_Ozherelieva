from playwright.sync_api import sync_playwright, expect
from playwright.sync_api import Page, Locator
from dotenv import load_dotenv
import os
import allure

from homework_lesson_30.page_objects.add_remove_elements_page.add_remove_elements_page import AddRemoveElementsPage

load_dotenv()

class HomePage:
    add_remove_elements_btn_locator = "//a[@href='/add_remove_elements/']"
    add_remove_el_header_locator = "//h3[text()='Add/Remove Elements']"

    def __init__(self, page: Page):
        self.page = page
        self.url = os.getenv("PW_URL")


    def open(self):
        return self.page.goto(self.url)

    @allure.step("Clicking on 'Add / Remove Elements' button")
    def click_on_add_remove_elements_btn(self):
        add_remove_elements_btn = self.page.locator(self.add_remove_elements_btn_locator)
        add_remove_elements_btn.click()
        return AddRemoveElementsPage(self.page)

    @allure.step("Checking if page is opened")
    def page_is_opened(self)-> bool:
        try:
            expect(self.page).to_have_url(self.url + "/add_remove_elements/")
            expect(self.page.locator(self.add_remove_el_header_locator)).to_be_visible()
            return True
        except Exception:
            return False






