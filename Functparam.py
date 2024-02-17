def print_params(a=36.6, b='normal', c=True):
    print(a, b, c)


print_params()
print_params(38.3, b='high')
# print_params(1, 2, 3, 4) функция не работает, лишний аргумент
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [36.7, 'norm', True]
values_dict = {'a': 38.8, 'b': 'high!', 'c': True}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = [37, 38.4]
print_params(*values_list_2, 42)