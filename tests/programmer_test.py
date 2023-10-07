from pages.programmer_page import ProgrammerPage


class TestProgrammerPage:
    def test_letter_buttons_activity_status(self, app):
        programmer_page = ProgrammerPage(app)
        programmer_page.open_menu()
        programmer_page.open_page('programmer')
        result_hex = programmer_page.letters_activity_status_for_any_number_system('hexadecimal')
        result_dec = programmer_page.letters_activity_status_for_any_number_system('decimal')
        result_oct = programmer_page.letters_activity_status_for_any_number_system('octa')
        result_bin = programmer_page.letters_activity_status_for_any_number_system('binary')
        assert result_hex == 6, 'letter buttons status is not active for hexadecimal'
        assert result_dec == 0, 'letter buttons status is active for decimal'
        assert result_oct == 0, 'letter buttons status is active for octa'
        assert result_bin == 0, 'letter buttons status is active for binary'

    def test_number_buttons_activity_status(self, app):
        programmer_page = ProgrammerPage(app)
        programmer_page.open_menu()
        programmer_page.open_page('programmer')
        result_hex = programmer_page.numbers_activity_status_for_any_number_system('hexadecimal')
        result_dec = programmer_page.numbers_activity_status_for_any_number_system('decimal')
        result_oct = programmer_page.numbers_activity_status_for_any_number_system('octa')
        result_bin = programmer_page.numbers_activity_status_for_any_number_system('binary')
        assert result_hex == 10, 'letter buttons status is not active for hexadecimal'
        assert result_dec == 10, 'letter buttons status is active for decimal'
        assert result_oct == 8, 'letter buttons status is active for octa'
        assert result_bin == 2, 'letter buttons status is active for binary'

    def test_bit_buttons_activity_status(self, app):
        programmer_page = ProgrammerPage(app)
        programmer_page.open_menu()
        programmer_page.open_page('programmer')
        result_dword = programmer_page.bits_button_activity_for_different_data_structure('qword')
        result_word = programmer_page.bits_button_activity_for_different_data_structure('dword')
        result_byte = programmer_page.bits_button_activity_for_different_data_structure('word')
        result_qword = programmer_page.bits_button_activity_for_different_data_structure('byte')
        assert result_qword == 64, 'letter buttons status is not active for hexadecimal'
        assert result_dword == 32, 'letter buttons status is active for decimal'
        assert result_word == 16, 'letter buttons status is active for octa'
        assert result_byte == 8, 'letter buttons status is active for binary'


