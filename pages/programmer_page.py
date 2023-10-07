from pages.base_page import BasePage


class ProgrammerPage(BasePage):
    def letters_activity_status_for_any_number_system(self, system_name):
        letters = ['a', 'b', 'c', 'd', 'e', 'f']
        quantity_active_letters = 0
        systems = {'hexadecimal': self.locators.HEX_BUTTON,
                   'decimal': self.locators.DECIMAL_BUTTON,
                   'octa': self.locators.OCTA_BUTTON,
                   'binary': self.locators.BINARY_BUTTON}
        self.window_app.child_window(auto_id=systems[system_name]).click_input()
        for letter in letters:
            status = self.get_letter_activity_status(letter)
            if status:
                quantity_active_letters += 1
        return quantity_active_letters

    def numbers_activity_status_for_any_number_system(self, system_name):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        quantity_active_numbers = 0
        systems = {'hexadecimal': self.locators.HEX_BUTTON,
                   'decimal': self.locators.DECIMAL_BUTTON,
                   'octa': self.locators.OCTA_BUTTON,
                   'binary': self.locators.BINARY_BUTTON}
        self.window_app.child_window(auto_id=systems[system_name]).click_input()
        for number in numbers:
            status = self.get_number_activity_status(number)
            if status:
                quantity_active_numbers += 1
        return quantity_active_numbers

    def bits_button_activity_for_different_data_structure(self, structure_name):
        self.click_bit_flip()
        bits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
                54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
        quantity_active_bits = 0
        structures = {'qword': self.locators.QWORD_BUTTON,
                      'dword': self.locators.DWORD_BUTTON,
                      'word': self.locators.WORD_BUTTON,
                      'byte': self.locators.BYTE_BUTTON}
        self.window_app.child_window(auto_id=structures[structure_name]).click_input()
        for bit in bits:
            status = self.get_bit_activity_status(bit)
            if status:
                quantity_active_bits += 1
        return quantity_active_bits
