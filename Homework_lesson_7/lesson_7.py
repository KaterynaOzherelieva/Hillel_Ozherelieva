# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number):
    """
    return the multiplication table, stops if the multiplication result > 25
    """
    multiplier = 1
    while True:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1


# task 2

"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_numbers(a, b):
    """
    returns the sum of two numbers.
    """
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise ValueError('Input must be a number')
    return a + b


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average(numbers):
    """
    returns the arithmetic mean of a list of numbers
    """
    if not numbers:
        raise ZeroDivisionError('List is empty')
    return sum(numbers) / len(numbers)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse(text):
    """
    returns reversed string
    """
    if text is not str:
        raise ValueError('Input must be a string')
    return text[::-1]


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(words):
    """
    returns the longest word
    """
    return max(words, key=len)


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    """
    returns index of the first occurrence of the second string, else returns -1
    """
    return str1.find(str2)

# task 7

def even_numbers(numbers):
    """
    returns sum of even numbers, homework 6.4
    """
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return sum(even_numbers)

# task 8

def string_values(elements):
    """
    returns string values only, homework 6.3
    """
    result = []
    for element in elements:
        if type(element) == str:
            result.append(element)
    return result

# task 9

def unique_10(some_string):
    """
    returns True if some_string has more than 10 unique chars, homework 6.1
    """
    unique_chars = len(set(some_string))
    return unique_chars > 10

# task 10

def letter_h(text):
    """
    Returns string "'H' present" if text contains the letter 'h' or 'H'; or "No 'H'".
    """
    if "h" in text.lower():
        return "'H' present"
    else:
        return "No 'H'"

