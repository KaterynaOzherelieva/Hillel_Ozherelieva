import pytest
import pathlib
import os
from playwright.sync_api import sync_playwright, Page, Playwright

from homework_lesson_30.page_objects.home_page.home_page import HomePage
from homework_lesson_30.page_objects.add_remove_elements_page.add_remove_elements_page import AddRemoveElementsPage


# @pytest.fixture()
# def clear_page():
#     with sync_playwright() as p:
#          browser = p.chromium.launch(headless=False)
#          context = browser.new_context()
#          page = browser.new_page()
#          page.set_default_timeout(5000)
#          yield page
#          context.close()
#          browser.close()

@pytest.fixture()
def clear_page(page: Page):
    page.set_default_timeout(5000)
    yield page
    page.context.close()


@pytest.fixture()
def home_page(clear_page) -> HomePage:
    home_page = HomePage(clear_page)
    home_page.open()
    return home_page

@pytest.fixture()
def add_remove_elements_page(home_page) -> AddRemoveElementsPage:
    home_page.click_on_add_remove_elements_btn()
    add_remove_el_page = AddRemoveElementsPage(home_page.page)
    return add_remove_el_page

# @pytest.fixture(scope="function", autouse=True)
# def trace_per_test(request, clear_page):
#
#     context = clear_page.context
#
#     trace_path = pathlib.Path(__file__).parent / 'pw_traces'
#     trace_path.mkdir(exist_ok=True)
#
#     # старт трасування
#     context.tracing.start(
#         screenshots=True,
#         snapshots=True,
#         sources=True
#     )
#
#     yield  # тест виконується тут
#
#     # stop tracing і збереження після тесту
#     test_name = request.node.name
#     context.tracing.stop(path=str(trace_path / f"{test_name}.zip"))

