import allure

from pages.date_page import DatePage


@allure.feature('Date')
class TestDatePage:
    @allure.title('Difference between dates')
    def test_difference_between_dates(self, app):
        date_page = DatePage(app)
        date_page.open_menu()
        date_page.open_page('date')
        result = date_page.difference_between_dates()
        assert result == 6, 'the date has not changed'

    @allure.title('Add or subtract days')
    def test_add_or_subtract_days(self, app):
        date_page = DatePage(app)
        date_page.open_menu()
        date_page.open_page('date')
        result_add = date_page.add_or_subtract_days('add')
        result_subtract = date_page.add_or_subtract_days('subtract')
        assert result_add == '18 июня 2031 г.', 'data has not been appended to the date'
        assert result_subtract == '30 октября 1946 г.', 'no data was subtracted from the date'
