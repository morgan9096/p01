import re
from tkinter import N
from base import BasePage
from selenium.webdriver.common.by import By

class LOCATORS:
    FIELD = (By.ID, 'text') # todo:
    BUTTON = (By.CLASS_NAME, 'search_button2') # todo:
    TABS = (By.CSS_SELECTOR, '.__tab') # todo
    HEADER = (By.CSS_SELECTOR, '__header') # todo

class HabrHelper(BasePage):

    def get_header_by_text(self, text):
        elements = self.find_element(LOCATORS.HEADER);
        result_list = [element for element in elements if element.textContent.strip() == text]
        return result_list[0] if result_list else None

    def enter_word(self, word):
        search_field = self.find_element(LOCATORS.FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        button = self.find_element(LOCATORS.BUTTON)
        button.click()
        return button

    def get_tabs(self):
        return self.find_elements(LOCATORS.TABS)

    def get_tab_by_name(self, name):
        tabs = self.get_tabs()
        for tab in tabs:
            if tab.textContent.strip() == 'name':
                return tab