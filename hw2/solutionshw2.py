# This is solutions for homework 2

def print_words_with_comma():
    """
    Запитує у користувача два слова і виводить їх розділеними комою.
    """
    # Prompt the user to input the first word
    first_word = input("Enter the first word: ")

    # Prompt the user to input the second word
    second_word = input("Enter the second word: ")

    # Print the two words separated by a comma
    print(f"{first_word}, {second_word}")


def print_product_of_three_numbers():
    """
    Запитує три цілі числа a, b і x та друкує їх добуток.
    """
    # Prompt the user to input the first integer
    a = int(input("Enter the first integer (a): "))

    # Prompt the user to input the second integer
    b = int(input("Enter the second integer (b): "))

    # Prompt the user to input the third integer
    x = int(input("Enter the third integer (x): "))

    # Calculate the product of the three integers
    product = a * b * x

    # Print the product
    print(f"The product of {a}, {b}, and {x} is: {product}")


def solve_quadratic_equation():
    """
    Розв'язує квадратне рівняння ax^2 + bx + c = 0 за формулами x1,2 = (-b ±
    sqrt(b^2 - 4ac)) / (2a). Значення a, b та c вводяться з клавіатури.
    Використовується оператор зведення в ступінь для знаходження кореня.
    """
    # Prompt the user to input coefficients a, b, and c
    a = float(input("Введіть коефіцієнт a: "))
    b = float(input("Введіть коефіцієнт b: "))
    c = float(input("Введіть коефіцієнт c: "))

    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    # Calculate the two solutions using the quadratic formula
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)

    # Print the solutions
    print(f"Корені рівняння: x1 = {x1}, x2 = {x2}")


def sum_of_ascii_codes():
    """
    Запитує у користувача фразу з 10 символів і виводить суму ASCII-кодів
    символів введеного рядка.
    """
    # Prompt the user to input a phrase of exactly 10 characters
    phrase = input("Введіть фразу з 10 символів: ")

    # Ensure the input is exactly 10 characters long
    while len(phrase) != 10:
        phrase = input("Будь ласка, введіть точно 10 символів: ")

    # Calculate the sum of ASCII codes of the characters
    ascii_sum = sum(ord(char) for char in phrase)

    # Print the sum of the ASCII codes
    print(f"Сума ASCII-кодів символів: {ascii_sum}")


def reverse_text():
    """
    Запитує у користувача текст і виводить його в оберненому порядку.
    """
    # Prompt the user to input text
    text = input("Введіть текст: ")

    # Reverse the text
    reversed_text = text[::-1]

    # Print the reversed text
    print(f"Текст в оберненому порядку: {reversed_text}")


def calculate_circle_area():
    """
    Запитує користувача радіус круга і виводить його площу.
    Формула площі круга: S = πr^2.
    """
    import math

    # Prompt the user to input the radius
    radius = float(input("Введіть радіус круга: "))

    # Calculate the area of the circle
    area = math.pi * (radius ** 2)

    # Print the area of the circle
    print(f"Площа круга: {area}")


def calculate_travel_time():
    """
    Розраховує час, за який транспортний засіб доїде з пункту А в пункт В.
    Відстань від А до В = 700 км, швидкість автомобіля = 90 км/год.
    Використовується формула: Час = відстань / швидкість.

    """
    v, l = input().split()
    # Define the distance and speed
    length = int(v)  # відстань в кілометрах
    velocity = int(l)  # швидкість в кілометрах на годину

    # Calculate the driving time
    driving_time = length / velocity  # час в годинах

    # Print the driving time
    print(
        f"Час, за який транспортний засіб доїде з пункту А в пункт В: "
        f"{driving_time:.2f} годин")


def print_user_info():
    """
    Запитує у користувача ім'я та вік і виводить повідомлення, використовуючи
    конкатенацію рядків і приведення типу числа до рядка.
    """
    # Prompt the user to input their name and age
    name = input("Введіть ваше ім'я: ")
    age = int(input("Введіть ваш вік: "))

    # Print the message using string concatenation and type conversion
    print("My name is " + name + " and I am " + str(age) + " years old.")


if __name__ == '__main__':
    calculate_travel_time()
