from pywinauto import Application

from locators.base_page_locators import BasePageLocators


class BasePage:
    locators = BasePageLocators()

    def __init__(self, app: Application):
        self.app = app
        self.window_app = app['Калькулятор']
        self.window_app.wait('ready', timeout=5)

    def open_menu(self):
        self.window_app.child_window(auto_id=self.locators.NAVIGATION_BUTTON).set_focus().click()

    def click_number(self, number: int):
        self.window_app.child_window(auto_id=f'num{number}Button').set_focus().click()

    def click_plus(self):
        self.window_app.child_window(auto_id=self.locators.PLUS_BUTTON).click_input()

    def click_difference(self):
        self.window_app.child_window(auto_id=self.locators.MINUS_BUTTON).click_input()

    def click_multiplication(self):
        self.window_app.child_window(auto_id=self.locators.MULTIPLY_BUTTON).click_input()

    def click_division(self):
        self.window_app.child_window(auto_id=self.locators.DIVIDE_BUTTON).click_input()

    def click_equal(self):
        self.window_app.child_window(auto_id=self.locators.EQUAL_BUTTON).click_input()

    def click_clear_entry_field(self):
        self.window_app.child_window(auto_id=self.locators.CLEAR_ENTRY_BUTTON).click_input()

    def click_clear_all_entered_numbers(self):
        self.window_app.child_window(auto_id=self.locators.CLEAR_BUTTON).click_input()

    def get_result(self) -> int:
        result = self.window_app.child_window(auto_id=self.locators.RESULT).texts()
        return int(result[0].split(' ')[3])

    def get_written_expression(self) -> int:
        result = self.window_app.child_window(auto_id=self.locators.WRITTEN_EXPRESSION).texts()
        return result

    def set_numbers(self, number: int):
        self.window_app.child_window(auto_id=self.locators.RESULT).type_keys(number)

    def open_page(self, page_name: str):
        pages = {'standard': self.locators.STANDARD_ITEM,
                 'scientific': self.locators.SCIENTIFIC_ITEM,
                 'programmer': self.locators.PROGRAMMER_ITEM,
                 'date': self.locators.DATE_ITEM}
        self.window_app.child_window(auto_id=pages[page_name]).set_focus().click_input()
        if page_name == 'standard':
            from pages.standart_page import StandardPage
            return StandardPage(self.app)
        elif page_name == 'scientific':
            from pages.scientific_page import ScientificPage
            return ScientificPage(self.app)
        elif page_name == 'programmer':
            from pages.programmer_page import ProgrammerPage
            return ProgrammerPage(self.app)
        elif page_name == 'date':
            from pages.date_page import DatePage
            return DatePage(self.app)
