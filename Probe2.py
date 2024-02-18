# def greetings(st):
#     print(st)
#     if len(st) == 0:  # Граничный случай
#         return
#     else:  # Рекурсивный случай
#         greetings(st[:-1])
#
#
# greetings('Hello, world!')
#
#
# name = "Дмитрий"
# age = 25
# print(f"Меня зовут {name}. Мне {age} лет.")
#
#
# scores = [100, 95, 88, 92, 99]
#
# def printScores(student, *args):
#    print(f"Student Name: {student}")
#    for score in scores:
#       print(score)
# #printScores("Jonathan",scores)
#
#
# sportsmen_list = {'sprint ': ['Bolt', 'Lewis', 'Jonson'], 'long jump ': 'Powell', 'high jump ': 'Sotomajor'}
# def sportsmen(**kwargs):
#     print(sportsmen_list)
#
#
# #sportsmen()


# info = 'sprint', 'name', 'result'
# great_sportsmen = {'Bolt': 9.58, 'Lewis': 9.86, 'Johnson': [9.78, 9.83, 9.93]}
#
# def great_sprinters_list(*args, **kwargs):
#    print(*args, **kwargs)
#
#
# great_sprinters_list(info, great_sportsmen)


# def factorial(n):
#     if n == 1:
#         print(n)
#         return 1
#     factorial_n_minus_1 = factorial(n= n - 1)
#     print(n)
#     return n * factorial_n_minus_1


# print(factorial(4))

def numbers(n):
    if n == 1:
        return 1
    print(numbers(n= n-1))


numbers(10)