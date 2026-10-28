import unittest
from unittest.mock import patch
from app import check_positive_number, count_vowels, Figure

class TestLabWork(unittest.TestCase):

    # Тесты для проверки числа
    def test_check_positive_number_valid(self):
        self.assertEqual(check_positive_number(5), "Число 5 корректное.")

    def test_check_positive_number_invalid(self):
        with self.assertRaises(ValueError):
            check_positive_number(-3)

    # Тесты для подсчета гласных
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("12345"), 0)
        self.assertEqual(count_vowels("привіт"), 2)

    # Тесты для Figure с использованием subTest
    def test_figure_angles_subtest(self):
        figures = [("квадрат", 4), ("прямоугольник", 4), ("треугольник", 3)]
        for f_type, expected_angles in figures:
            with self.subTest(figure_type=f_type):
                fig = Figure(f_type, 10)
                self.assertEqual(fig.get_angles(), expected_angles)

    # Тесты граничных случаев
    def test_figure_invalid_cases(self):
        with self.assertRaises(ValueError):
            Figure("квадрат", 0).get_angles()
        with self.assertRaises(ValueError):
            Figure("неизвестная", 5).get_angles()

    # Тест с помощью mock/patch
    @patch("builtins.input", return_value="10")
    def test_input_function(self, mock_input):
        user_input = input("Введите число: ")
        self.assertEqual(user_input, "10")
        mock_input.assert_called_once()

if __name__ == "__main__":
    unittest.main()