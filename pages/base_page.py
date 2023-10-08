import allure
import pywinauto.mouse
from pywinauto import Application

from locators.base_page_locators import BasePageLocators


class BasePage:
    locators = BasePageLocators()

    def __init__(self, app: Application):
        self.app = app
        self.window_app = app['Калькулятор']
        self.window_app.wait('ready', timeout=5)

    @allure.step('Open a menu')
    def open_menu(self):
        self.window_app.child_window(auto_id=self.locators.NAVIGATION_BUTTON).set_focus().click()

    @allure.step('Click on the number')
    def click_number(self, number: int):
        self.window_app.child_window(auto_id=f'num{number}Button').set_focus().click()

    @allure.step('Click on the plus')
    def click_plus(self):
        self.window_app.child_window(auto_id=self.locators.PLUS_BUTTON).click_input()

    @allure.step('Click on the minus')
    def click_difference(self):
        self.window_app.child_window(auto_id=self.locators.MINUS_BUTTON).click_input()

    @allure.step('Click on  the multiplication')
    def click_multiplication(self):
        self.window_app.child_window(auto_id=self.locators.MULTIPLY_BUTTON).click_input()

    @allure.step('Click on the division')
    def click_division(self):
        self.window_app.child_window(auto_id=self.locators.DIVIDE_BUTTON).click_input()

    @allure.step('Click on the equal')
    def click_equal(self):
        self.window_app.child_window(auto_id=self.locators.EQUAL_BUTTON).click_input()

    @allure.step('Click the button to clear the entry field')
    def click_clear_entry_field(self):
        self.window_app.child_window(auto_id=self.locators.CLEAR_ENTRY_BUTTON).click_input()

    @allure.step('Click the button to clear all entered numbers')
    def click_clear_all_entered_numbers(self):
        self.window_app.child_window(auto_id=self.locators.CLEAR_BUTTON).click_input()

    @allure.step('Click on the cosine')
    def click_cosine(self):
        self.window_app.child_window(auto_id=self.locators.COS_BUTTON).click_input()

    @allure.step('Click on the sine')
    def click_sine(self):
        self.window_app.child_window(auto_id=self.locators.SIN_BUTTON).click_input()

    @allure.step('Click on the factorial')
    def click_factorial(self):
        self.window_app.child_window(auto_id=self.locators.FACTORIAL_BUTTON).click_input()

    @allure.step('Click on the pi')
    def click_pi(self):
        self.window_app.child_window(auto_id=self.locators.PI_BUTTON).click_input()

    @allure.step('Click on the letter')
    def click_letter(self, letter: str):
        result = self.window_app.child_window(auto_id=f'{letter}Button').click()
        return result

    @allure.step('Click on the bit flip')
    def click_bit_flip(self):
        self.window_app.child_window(auto_id=self.locators.BIT_FLIP).click_input()

    @allure.step('Click to select the countdown date')
    def click_calendar_from(self):
        self.window_app.child_window(auto_id=self.locators.CALENDAR_DATE_BUTTON_FROM).click_input()

    @allure.step('Click to select the countdown end date')
    def click_calendar_to(self):
        self.window_app.child_window(auto_id=self.locators.CALENDAR_DATE_BUTTON_TO).click_input()

    @allure.step('Click on the date options')
    def click_date_option(self):
        self.window_app.child_window(auto_id=self.locators.DATE_OPTION_BUTTON).click_input()

    @allure.step('Move the cursor to the coordinates and click')
    def mouse_click(self, x, y):
        pywinauto.mouse.click(button='left', coords=(x, y))

    @allure.step('Get the activity status of the letter')
    def get_letter_activity_status(self, letter: str):
        result = self.window_app.child_window(auto_id=f'{letter}Button').is_enabled()
        return result

    @allure.step('Get the activity status of a number')
    def get_number_activity_status(self, number: int):
        result = self.window_app.child_window(auto_id=f'num{number}Button').is_enabled()
        return result

    @allure.step('Get the activity status of the bit')
    def get_bit_activity_status(self, number: int):
        result = self.window_app.child_window(auto_id=f'Bit{number}').is_enabled()
        return result

    @allure.step('Get a numerical result')
    def get_result(self) -> int:
        result = self.window_app.child_window(auto_id=self.locators.RESULT).texts()
        return int(result[0].split(' ')[3])

    @allure.step('Get a letter result')
    def get_result_letter(self) -> str:
        result = self.window_app.child_window(auto_id=self.locators.RESULT).texts()
        return result

    @allure.step('Get a written expression result')
    def get_written_expression(self):
        result = self.window_app.child_window(auto_id=self.locators.WRITTEN_EXPRESSION).texts()
        return result

    @allure.step('Get the result with a dot')
    def get_result_with_a_dot(self) -> float:
        result = self.window_app.child_window(auto_id=self.locators.RESULT).texts()
        return float(result[0].split(' ')[3].replace(',', '.'))

    @allure.step('Get the result of the date difference')
    def get_date_dif_result(self) -> int:
        result = self.window_app.child_window(auto_id=self.locators.DATE_DIF_RESULT).texts()
        return int(result[0].split(' ')[0])

    @allure.step('Get the result of the formatted date')
    def get_date_result(self) -> str:
        result = self.window_app.child_window(auto_id=self.locators.DATE_RESULT).texts()
        return result[0].replace('\u200e', '')

    @allure.step('Set the numbers manually')
    def set_numbers(self, number: int):
        self.window_app.child_window(auto_id=self.locators.RESULT).type_keys(number)

    @allure.step('Set the date manually')
    def set_date(self, year: int, month: int, day: int):
        self.window_app.child_window(auto_id=self.locators.YEARS_BUTTON).type_keys(year)
        self.window_app.child_window(auto_id=self.locators.MONTHS_BUTTON).type_keys(month)
        self.window_app.child_window(auto_id=self.locators.DAYS_BUTTON).type_keys(day)

    @allure.step('Selecting the operating mode of the calculator')
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
