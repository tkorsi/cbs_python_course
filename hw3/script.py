def cyclical_func():
    for n in range(1, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', int(n / x))
                return
        else:
            print(n, 'is a prime number')


def number_of_diplomas(w, h, X):
    rows = X // max(h, w)
    cols = X // min(h, w)
    return rows * cols


# width - ширина
# height - висота
# diplomas - (h, w)
# знайти мінімальний Х
def border_width(w, h, n, max_border):
    counter = 0
    for X in range(1, max_border + 1):
        counter += 1
        num_diplomas = number_of_diplomas(w, h, X)
        if num_diplomas >= n:
            return X, counter
    return -1, counter


def bin_border_width(w, h, n, max_border):
    l = 1
    r = max_border
    while l + 1 < r:
        m = (l + r) // 2
        if number_of_diplomas(w, h, m) >= n:
            r = m
        else:
            l = m
    return r


print(bin_border_width(1, 1, int(1e14), int(1e7)))
# print(bin_border_width(3, 4, 3, 1000))
# print(bin_border_width(3, 4, 4, 1000))
# print(bin_border_width(2, 2, 8, 1000))

# print(number_of_diplomas(1, 1, 1000))
# result, num_steps = border_width(1, 1, int(1e14), int(1e7))
# print(f"Function gave us {result} and made {num_steps} steps.")
# border_width ~ O(n) = C * n
# O(n**2) - збільшивши вхід в 10, час виконання збільшився на 100
# O(logn), O(e^n)


# d = dict()
#
# d["amount"] = 1000
# print("amount" in d)
# print(d["amount"])
