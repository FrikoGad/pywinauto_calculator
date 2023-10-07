import pywinauto.mouse
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

    def click_cosine(self):
        self.window_app.child_window(auto_id=self.locators.COS_BUTTON).click_input()

    def click_sine(self):
        self.window_app.child_window(auto_id=self.locators.SIN_BUTTON).click_input()

    def click_factorial(self):
        self.window_app.child_window(auto_id=self.locators.FACTORIAL_BUTTON).click_input()

    def click_pi(self):
        self.window_app.child_window(auto_id=self.locators.PI_BUTTON).click_input()

    def click_letter(self, letter: str):
        result = self.window_app.child_window(auto_id=f'{letter}Button').click()
        return result

    def click_bit_flip(self):
        self.window_app.child_window(auto_id=self.locators.BIT_FLIP).click_input()

    def click_calendar_from(self):
        self.window_app.child_window(auto_id=self.locators.CALENDAR_DATE_BUTTON_FROM).click_input()

    def click_calendar_to(self):
        self.window_app.child_window(auto_id=self.locators.CALENDAR_DATE_BUTTON_TO).click_input()

    def click_date_option(self):
        self.window_app.child_window(auto_id=self.locators.DATE_OPTION_BUTTON).click_input()

    def mouse_click(self, x, y):
        pywinauto.mouse.click(button='left', coords=(x, y))

    def get_letter_activity_status(self, letter: str):
        result = self.window_app.child_window(auto_id=f'{letter}Button').is_enabled()
        return result

    def get_number_activity_status(self, number: int):
        result = self.window_app.child_window(auto_id=f'num{number}Button').is_enabled()
        return result

    def get_bit_activity_status(self, number: int):
        result = self.window_app.child_window(auto_id=f'Bit{number}').is_enabled()
        return result

    def get_result(self) -> int:
        result = self.window_app.child_window(auto_id=self.locators.RESULT).texts()
        return int(result[0].split(' ')[3])

    def get_result_letter(self) -> str:
        result = self.window_app.child_window(auto_id=self.locators.RESULT).texts()
        return result

    def get_written_expression(self) -> int:
        result = self.window_app.child_window(auto_id=self.locators.WRITTEN_EXPRESSION).texts()
        return result

    def get_result_with_a_dot(self) -> float:
        result = self.window_app.child_window(auto_id=self.locators.RESULT).texts()
        return float(result[0].split(' ')[3].replace(',', '.'))

    def get_date_dif_result(self) -> int:
        result = self.window_app.child_window(auto_id=self.locators.DATE_DIF_RESULT).texts()
        return int(result[0].split(' ')[0])

    def get_date_result(self) -> int:
        result = self.window_app.child_window(auto_id=self.locators.DATE_RESULT).texts()
        return result[0].replace('\u200e', '')

    def set_numbers(self, number: int):
        self.window_app.child_window(auto_id=self.locators.RESULT).type_keys(number)

    def set_date(self, year: int, month: int, day: int):
        self.window_app.child_window(auto_id=self.locators.YEARS_BUTTON).type_keys(year)
        self.window_app.child_window(auto_id=self.locators.MONTHS_BUTTON).type_keys(month)
        self.window_app.child_window(auto_id=self.locators.DAYS_BUTTON).type_keys(day)

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
