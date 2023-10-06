from pywinauto.findwindows import ElementNotFoundError

from pages.base_page import BasePage


class StandardPage(BasePage):

    def amount_numbers(self, num1, num2) -> int:
        self.click_number(num1)
        self.click_plus()
        self.set_numbers(num2)
        self.click_equal()
        return self.get_result()

    def difference_numbers(self, num1, num2) -> int:
        self.click_number(num1)
        self.click_difference()
        self.set_numbers(num2)
        self.click_equal()
        return self.get_result()

    def multiplication_numbers(self, num1, num2) -> int:
        self.click_number(num1)
        self.click_multiplication()
        self.set_numbers(num2)
        self.click_equal()
        return self.get_result()

    def division_numbers(self, num1, num2) -> int:
        self.click_number(num1)
        self.click_division()
        self.set_numbers(num2)
        self.click_equal()
        return self.get_result()

    def clear_entry_field(self, num1, num2) -> int:
        self.click_number(num1)
        self.click_division()
        self.set_numbers(num2)
        self.click_clear_entry_field()
        return self.get_result()

    def clear_all_entered_numbers(self, num1, num2):
        self.click_number(num1)
        self.click_division()
        self.set_numbers(num2)
        self.click_clear_all_entered_numbers()
        try:
            written_expression = self.get_written_expression()
        except ElementNotFoundError as error:
            written_expression = 0
        result = self.get_result()
        return written_expression, result
