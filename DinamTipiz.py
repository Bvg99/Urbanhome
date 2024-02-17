# def multiplay(number_1, number_2, number_3):
#     print('calling_function_with_parameters ', number_1, number_2, number_3)
#     if isinstance(number_1, int):
#         value = number_1 * number_2 + number_3
#         return value
#     return 'error'
#
# print(multiplay(3,'Hi',0))
# # print(multiplay('Hi', 3))


# def elefant_to_free(some_list):
#     elefant_found = 'elefant' in some_list
#     if elefant_found:
#         some_list.remove('elefant')
#         print('one_elefant_free')
#     return elefant_found
#
#
zoo = ['1', '2', 'elefant', '4', 'elefant', '6']

# elefant_to_free(some_list=zoo)
# print(zoo)


def elefant_to_free(some_list):
    for elefant_found in some_list:
        if elefant_found == 'elefant':
            print('elefant_found')
            print('one_elefant_free')
            some_list.remove('elefant')
            print(some_list)
        print('no_elefant')

elefant_to_free(some_list=zoo)
some_list = zoo
# print(some_list)


