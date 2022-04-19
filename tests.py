import time
from pages import HabrHelper


def test_habr_search(browser):
    habr_main_page = HabrHelper(browser)
    habr_main_page.click_on_the_search_button()
    search_field = habr_main_page.enter_word('Selenium')
    habr_main_page.press_enter(search_field)
    assert habr_main_page.get_articles()

def test_development_tab(browser):
    __check_tab(browser, 'Development')
    
def test_admin_tab(browser):
    __check_tab(browser, 'Admin')

def __check_tab(browser, tab_name):
    habr_main_page = HabrHelper(browser)
    tab = habr_main_page.get_tab_by_name(tab_name)
    tab.click()
    time.sleep(1)
    header = habr_main_page.get_header_by_text(tab_name)
    assert header is not None
    assert header.text == tab_name
