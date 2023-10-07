from pages.date_page import DatePage


class TestDatePage:
    def test_difference_between_dates(self, app):
        date_page = DatePage(app)
        date_page.open_menu()
        date_page.open_page('date')
        result = date_page.difference_between_dates()
        assert result == 6, 'the date has not changed'

    def test_add_or_subtract_days(self, app):
        date_page = DatePage(app)
        date_page.open_menu()
        date_page.open_page('date')
        result_add = date_page.add_or_subtract_days('add')
        result_subtract = date_page.add_or_subtract_days('subtract')
        print(result_add)
        print(result_subtract)
        assert result_add == '17 июня 2031 г.', 'data has not been appended to the date'
        assert result_subtract == '29 октября 1946 г.', 'no data was subtracted from the date'
