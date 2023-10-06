from pages.standart_page import StandardPage


class TestStandardPage:
    def test_amount_simple_numbers(self, app):
        standard_page = StandardPage(app)
        result = standard_page.amount_numbers(5, 155)
        assert result == 160, 'numbers are not summed or are summed incorrectly'

    def test_difference_simple_numbers(self, app):
        standard_page = StandardPage(app)
        result = standard_page.difference_numbers(9, 7)
        assert result == 2, 'numbers are not subtracted or are subtracted incorrectly'

    def test_multiplication_simple_numbers(self, app):
        standard_page = StandardPage(app)
        result = standard_page.multiplication_numbers(4, 150)
        assert result == 600, 'numbers are not multiplied or multiplied incorrectly'

    def test_division_simple_numbers(self, app):
        standard_page = StandardPage(app)
        result = standard_page.division_numbers(9, 3)
        assert result == 3, 'numbers do not divide or divide incorrectly'

    def test_clear_the_entry_field(self, app):
        standard_page = StandardPage(app)
        result = standard_page.clear_entry_field(9, 3)
        assert result == 0, 'entry field is not cleared'

    def test_clear_all(self, app):
        standard_page = StandardPage(app)
        written_expression, result = standard_page.clear_all_entered_numbers(9, 3)
        assert written_expression == 0 and result == 0, 'input field and written expression not cleared'