# 1. Проверка числа
def check_positive_number(number):
    if number <= 0:
        raise ValueError("Число должно быть больше нуля!")
    return f"Число {number} корректное."

# 2. Функция подсчета гласных букв
def count_vowels(text: str) -> int:
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯaeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# 3. Пример класса с фигурой
class Figure:
    def __init__(self, figure_type: str, length: float):
        self.figure_type = figure_type
        self.length = length

    @property
    def get_figure_type(self):
        return self.figure_type

    @property
    def get_figure_length(self):
        return self.length

    def get_angles(self):
        angles = {
            "квадрат": 4,
            "прямоугольник": 4,
            "треугольник": 3
        }
        if self.length <= 0:
            raise ValueError("Длина должна быть больше нуля")
        if self.figure_type not in angles:
            raise ValueError("Неизвестный тип фигуры")
        return angles[self.figure_type]