import allure
from dotenv import load_dotenv
from homework_lesson_30.page_objects.home_page.home_page import HomePage
from homework_lesson_30.page_objects.add_remove_elements_page.add_remove_elements_page import AddRemoveElementsPage
load_dotenv()

class TestAddRemoveElementsPage:

    @allure.feature("Testing if page 'Add / Remove Elements' is opened correctly")
    def test_location_is_correct(self, home_page: HomePage):
        add_remove_el_page = home_page.click_on_add_remove_elements_btn()
        assert add_remove_el_page.page_is_opened()

    @allure.feature("Testing if button 'Add Elements' works properly")
    def test_add_element(self, add_remove_elements_page: AddRemoveElementsPage):
        add_remove_elements_page.click_on_add_element_btn()
        assert add_remove_elements_page.page_is_opened()
        assert add_remove_elements_page.element_added()

    @allure.feature("Testing if button 'Delete Elements' works properly")
    def test_delete_element(self, add_remove_elements_page: AddRemoveElementsPage):
        add_remove_elements_page.click_on_add_element_btn().click_on_delete_btn()
        assert add_remove_elements_page.element_deleted()







