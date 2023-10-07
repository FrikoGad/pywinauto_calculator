from pages.base_page import BasePage


class ScientificPage(BasePage):

    def get_cosine_value(self, num1) -> int:
        self.set_numbers(num1)
        self.click_cosine()
        return self.get_result()

    def get_sine_value(self, num1) -> int:
        self.set_numbers(num1)
        self.click_sine()
        return self.get_result()

    def get_factorial(self, num1) -> int:
        self.set_numbers(num1)
        self.click_factorial()
        return self.get_result()

    def pi_multiplication(self, num1) -> float:
        self.set_numbers(num1)
        self.click_multiplication()
        self.click_pi()
        self.click_equal()
        return self.get_result_with_a_dot()
