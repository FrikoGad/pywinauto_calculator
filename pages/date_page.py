import allure

from pages.base_page import BasePage


class DatePage(BasePage):
    @allure.step('Difference between dates')
    def difference_between_dates(self):
        self.click_calendar_from()
        self.mouse_click(741, 457)
        self.click_calendar_to()
        self.mouse_click(693, 499)
        result = self.get_date_dif_result()
        return result

    @allure.step('Add or subtract days')
    def add_or_subtract_days(self, action):
        self.click_date_option()
        self.mouse_click(709, 255)
        actions = {'add': self.locators.ADD_RADIO_BUTTON,
                   'subtract': self.locators.SUBTRACT_RADIO_BUTTON}
        self.window_app.child_window(auto_id=actions[action]).click_input()
        self.set_date(7, 8, 10)
        result = self.get_date_result()
        return result
