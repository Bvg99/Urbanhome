# *args and **kwargs

info = 'sprint', 'name', 'result'
great_sportsmen = {'Bolt': 9.58, 'Lewis': 9.86, 'Johnson': [9.78, 9.83, 9.93]}


def great_sprinters_list(*args, **kwargs):
    print(*args, **kwargs)


great_sprinters_list(info, great_sportsmen)


# recursive function
def factorial(n):
    if n == 1:
        print(n)
        return 1
    factorial_n_minus_1 = factorial(n=n - 1)
    print(n)
    return n * factorial_n_minus_1


factorial(4)
