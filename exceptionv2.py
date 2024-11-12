"""Модуль для демонстрации работы с исключениями и пользовательскими исключениями"""

# Шаг 1: Функции, выбрасывающие исключения без обработчиков
def exception_by_five(x):
    """Выбрасывает ValueError, если число делится на 5"""
    if x % 5 == 0:
        raise ValueError("Число делится на 5")


def check_odd_length(s):
    """Выбрасывает IndexError если длина строки нечетная"""
    if len(s) % 2 != 0:
        raise IndexError("Длина строки нечетная")
    return s


# Шаг 2
def check_positive_number(x):
    """Проверяет, что число положительное и обрабатывает ValueError"""
    try:
        if x < 0:
            raise ValueError("Число отрицательное")
        return x
    except ValueError as e:
        print(f"Исключение обнаружено: {e}")
        return None


# Шаг 3
def check_is_digit(s):
    """Проверяет что строка состоит из цифр и использует блок finally"""
    try:
        if not s.isdigit():
            raise ValueError("Строка не является цифрой")
        return int(s)
    except ValueError as e:
        print(f"Исключение обнаруженно: {e}")
        return None
    finally:
        print("Завершена операция ")


# Шаг 4
def divide_numbers(a, b):
    """Проверяет деление чисел с обработкой исключений"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Невозможно разделить на ноль")
        return None
    except TypeError:
        print("Входные данные должны быть числами")
        return None
    else:
        return result
    finally:
        print("Завершена операция")


def get_element_from_list(lst, index):
    """Возвращает элемент из списка с обработкой исключений."""
    try:
        return lst[index]
    except IndexError:
        print("Индекс вне диапазона")
        return None
    except TypeError:
        print("Индекс должен быть целым числом")
        return None
    finally:
        print("Завершена операция ")


def convert_to_integer(s):
    """Конвертирует строку в целое число с обработкой исключений"""
    try:
        return int(s)
    except ValueError:
        print("Невозможно преобразовать в целое число")
        return None
    except TypeError:
        print("Ввод должен быть строкой")
        return None
    finally:
        print("Завершена операция")


# Шаг 5
def custom_division(x, divisor):
    """Генерирует исключение если делитель равен 10"""
    try:
        if divisor == 10:
            raise ValueError("Делитель не может быть 10")
        return x / divisor
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    finally:
        print("Завершена операция")


# Шаг 6
class NegativeValueError(Exception):
    """Исключение для отрицательных значений"""


class OddNumberError(Exception):
    """Исключение для нечетных чисел"""


class LargeNumberError(Exception):
    """Исключение для больших значений"""


# Примеры использования пользовательских исключений
def check_negative(x):
    """Проверяет, что значение не отрицательное"""
    if x < 0:
        raise NegativeValueError("Отрицательные значения не допускаются")
    return x


def check_odd_number(x):
    """Проверяет, является ли число нечетным"""
    if x % 2 != 0:
        raise OddNumberError("Нечетные числа не допускаются")
    return x


def check_large_number(x):
    """Проверяет, не превышает ли число 1000."""
    if x > 1000:
        raise LargeNumberError("Значения больше 1000 не допускаются")
    return x


# Шаг 7
def check_negative_value(x):
    """Проверяет, что значение не отрицательное, обрабатывает исключения"""
    try:
        if x < 0:
            raise NegativeValueError("Отрицательные значения не допускаются")
        return x
    except NegativeValueError as e:
        print(f"Обнаружено пользовательское исключение: {e}")
        return None
    finally:
        print("Завершена операция")


# Шаг 8
def demo_function_one(x):
    """Выбрасывает исключение, если значение равно нулю."""
    if x == 0:
        raise ValueError("Нулевое значение не допускается")
    return x


def demo_function_two(lst):
    """Выбрасывает исключение, если список пустой."""
    if len(lst) == 0:
        raise IndexError("Пустой список не разрешен")
    return lst


def demo_function_three(value):
    """Выбрасывает исключение, если значение не является строкой."""
    if not isinstance(value, str):
        raise TypeError("Разрешены только строки")
    return value
