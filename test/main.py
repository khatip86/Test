"""
Модуль, реализующий простую функцию для вычисления площади квадрата.

Copyright (c) 2023, [Ваше имя]
Блокнот Jupyter
"""

# Импорт необходимых модулей
import math

# Функция для вычисления площади квадрата
def площадь_квадрата(сторона):
    """
    Вычисляет площадь квадрата по его стороне.

    Args:
        сторона (float): Длина стороны квадрата.

    Returns:
        float: Площадь квадрата.
    """

    # Проверка входных данных
    if not isinstance(сторона, (int, float)):
        raise TypeError("Сторона квадрата должна быть числом.")
    if сторона <= 0:
        raise ValueError("Сторона квадрата должна быть положительным числом.")

    # Вычисление площади квадрата
    площадь = сторона ** 2

    # Возврат площади квадрата
    return площадь

# Проверка функции с примером
сторона = 5
print(f"Площадь квадрата со стороной {сторона} равна {площадь_квадрата(сторона)}.")

