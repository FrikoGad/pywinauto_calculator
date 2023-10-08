import allure

from pages.scientific_page import ScientificPage


@allure.feature('Scientific')
class TestScientificPage:
    @allure.title('Cosine')
    def test_cosine(self, app):
        scientific_page = ScientificPage(app)
        scientific_page.open_menu()
        scientific_page.open_page('scientific')
        result = scientific_page.get_cosine(180)
        assert result == -1, 'the cosine value is wrong'

    @allure.title('Sine')
    def test_sine(self, app):
        scientific_page = ScientificPage(app)
        scientific_page.open_menu()
        scientific_page.open_page('scientific')
        result = scientific_page.get_sine(90)
        assert result == 1, 'the sine value is wrong'

    @allure.title('Factorial')
    def test_factorial(self, app):
        scientific_page = ScientificPage(app)
        scientific_page.open_menu()
        scientific_page.open_page('scientific')
        result = scientific_page.get_factorial(5)
        assert result == 120, 'the factorial value is wrong'

    @allure.title('Pi')
    def test_pi(self, app):
        scientific_page = ScientificPage(app)
        scientific_page.open_menu()
        scientific_page.open_page('scientific')
        result = scientific_page.pi_multiplication(2)
        assert result == 6.283185307179586, 'the pi value is wrong'
