# Завдання 1
def sum_natural_numbers(a, b):
    """
    Дано числа a і b (a < b). Виведіть суму всіх натуральних чисел від a до b (включно).
    """
    total_sum = sum(range(a, b + 1))
    print(
        f"Сума всіх натуральних чисел від {a} до {b} (включно) дорівнює {total_sum}")


# Завдання 2
def factorial(n):
    """
    Факторіалом числа n називається число n!=1∙2∙3∙…∙n. Створіть програму, яка обчислює факторіал введеного користувачем числа.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Факторіал числа {n} дорівнює {result}")


# Завдання 3
def print_triangle(height):
    """
    Використовуючи вкладені цикли та функції print(‘*’, end=’’), print(‘ ‘, end=’’) та print() виведіть на екран прямокутний трикутник.
    """
    for i in range(1, height + 1):
        for j in range(i):
            print('*', end='')
        print()


# Завдання 4
def sum_multiples_of_average(a, b):
    """
    Дано числа a і b (a < b). Виведіть на екран суму всіх натуральних чисел від a до b (включно), які є кратними середньому арифметичному цього проміжку.
    """
    average = (a + b) / 2
    total_sum = sum(x for x in range(a, b + 1) if x % average == 0)
    print(
        f"Сума чисел від {a} до {b}, які є кратними середньому арифметичному ({average}), дорівнює {total_sum}")


# Завдання 5
def draw_rectangle(width, height):
    """
    Створіть програму, яка малює на екрані прямокутник із зірочок заданою користувачем ширини та висоти.
    """
    for i in range(height):
        print('*' * width)


# Завдання 6
def authorization_system(correct_login, correct_password):
    """
    Створіть програму авторизації, в якій користувачеві дається 3 спроби ввести свої облікові дані (логін та пароль). Якщо користувач за меншу кількість спроб ввів вірні дані, програма достроково припиняє своє виконання та виводить на екран повідомлення: «Авторизацію успішно пройдено з «№» спроби».
    """
    attempts = 3
    for attempt in range(1, attempts + 1):
        login = input("Введіть логін: ")
        password = input("Введіть пароль: ")
        if login == correct_login and password == correct_password:
            print(f"Авторизацію успішно пройдено з {attempt} спроби")
            return
        else:
            print("Невірні облікові дані. Спробуйте ще раз.")
    print("Всі спроби використані. Доступ заборонено.")


if __name__ == '__main__':
    # Виклик функції
    authorization_system("admin", "1234")
