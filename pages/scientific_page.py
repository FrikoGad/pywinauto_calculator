import allure

from pages.base_page import BasePage


class ScientificPage(BasePage):
    @allure.step('Get cosine')
    def get_cosine(self, num1) -> int:
        self.set_numbers(num1)
        self.click_cosine()
        return self.get_result()

    @allure.step('Get sine')
    def get_sine(self, num1) -> int:
        self.set_numbers(num1)
        self.click_sine()
        return self.get_result()

    @allure.step('Get factorial')
    def get_factorial(self, num1) -> int:
        self.set_numbers(num1)
        self.click_factorial()
        return self.get_result()

    @allure.step('Pi multiplication')
    def pi_multiplication(self, num1) -> float:
        self.set_numbers(num1)
        self.click_multiplication()
        self.click_pi()
        self.click_equal()
        return self.get_result_with_a_dot()
