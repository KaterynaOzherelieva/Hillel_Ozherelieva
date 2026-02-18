from playwright.sync_api import sync_playwright, expect
from playwright.sync_api import Page, Locator
from dotenv import load_dotenv
import os
import allure

load_dotenv()

class AddRemoveElementsPage:

    add_remove_el_header_locator = "//h3[text()='Add/Remove Elements']"
    add_element_btn_locator = "//button[text()='Add Element']"
    delete_btn_locator = "//button[text()='Delete']"


    def __init__(self, page: Page):
        self.page = page
        self.url = os.getenv("PW_URL") + "/add_remove_elements/"


    def open(self):
        return self.page.goto(self.url)

    @allure.step("Clicking on 'Add Element' button")
    def click_on_add_element_btn(self):
        add_element_btn = self.page.locator(self.add_element_btn_locator)
        add_element_btn.click()
        return self

    @allure.step("Clicking on 'Delete' button")
    def click_on_delete_btn(self):
        delete_btn = self.page.locator(self.delete_btn_locator)
        delete_btn.click()
        return self

    @allure.step("Checking if page is opened")
    def page_is_opened(self)-> bool:
        try:
            expect(self.page).to_have_url(self.url)
            expect(self.page.locator(self.add_remove_el_header_locator)).to_be_visible()
            return True
        except Exception:
            return False

    @allure.step("Checking if element is added")
    def element_added(self)-> bool:
        try:
            expect(self.page.locator(self.delete_btn_locator)).to_be_visible()
            return True
        except Exception:
            return False

    @allure.step("Checking if element is deleted")
    def element_deleted(self)-> bool:
        try:
            expect(self.page.locator(self.delete_btn_locator)).not_to_be_visible()
            return True
        except Exception:
            return False
