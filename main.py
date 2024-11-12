"""Основной модуль."""


from exceptionv2 import (
    exception_by_five, check_odd_length, check_positive_number, check_is_digit,
    divide_numbers, get_element_from_list, convert_to_integer, custom_division,
    check_negative, check_odd_number, check_large_number, check_negative_value,
    demo_function_one, demo_function_two, demo_function_three,
    NegativeValueError, OddNumberError, LargeNumberError  # Добавлены пользовательские исключения
)
def run_all_functions():
    """Запускает все функции для демонстрации работы исключений."""
    print("Запуск всех функций:")

    # Шаг 1
    try:
        exception_by_five(10)
    except ValueError as e:
        print(f"Exception in exception_by_five: {e}")

    try:
        check_odd_length("hello")
    except IndexError as e:
        print(f"Exception in check_odd_length: {e}")

    # Шаг 2
    check_positive_number(-5)

    # Шаг 3
    check_is_digit("abc")

    # Шаг 4
    divide_numbers(10, 0)
    get_element_from_list([1, 2, 3], 5)
    convert_to_integer("abc")

    # Шаг 5
    custom_division(50, 10)

    # Шаг 6
    try:
        check_negative(-5)
    except NegativeValueError as e:
        print(f"Exception in check_negative: {e}")

    try:
        check_odd_number(7)
    except OddNumberError as e:
        print(f"Exception in check_odd_number: {e}")

    try:
        check_large_number(1500)
    except LargeNumberError as e:
        print(f"Exception in check_large_number: {e}")

    # Шаг 7
    check_negative_value(-10)

    # Шаг 8
    try:
        demo_function_one(0)
    except ValueError as e:
        print(f"Exception in demo_function_one: {e}")

    try:
        demo_function_two([])
    except IndexError as e:
        print(f"Exception in demo_function_two: {e}")

    try:
        demo_function_three(123)
    except TypeError as e:
        print(f"Exception in demo_function_three: {e}")

if __name__ == "__main__":
    run_all_functions()
