"""
try:
    some code 1
except:
    some code 2
else:
    some code 3
finally:
    some code 4
"""


# try:
#     num1 = int(input('Введите число: '))
# except:
#     print('вы ввели не число')


# try:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#     result = num1 / num2
# except ZeroDivisionError: # голое исключение
#     print('На ноль делить нелзя!') 
# except ValueError:
#     print('Вы ввели не число!')
# else:
#     print(result)
# finally:
#     print('Программа завершена!')


# dict_ = dict.fromkeys(('makers', 'bootcamp', 'hello', 'dictionary'), 0)
# dict_ = {key: len(key) for key, val in dict_.items()}
# dict_.update({'except': 'Exception'})
# print(dict_)

# while True:
#     try: 
#         key = input('Введите слово: ')
#         if key == 'exit':
#             break
#         dict_[key] += 2
#     except (KeyError, TypeError):
#         print('Данного ключа нет либо произвести конкетенацию с числами нельзя!')
#     else:
#         print(dict_[key])
#     finally:
#         print(dict_)f


# list_ = [i for i in range(1, 31)]

# try:
#     index = int(input())
#     list_[index] = 'Ahmed'
# except IndexError:
#     print('You are out of list range')
# except ValueError:
#     print('Please enter the number, not a string')
# else:
#     print('There is not exception')
# finally:
#     print(list_)


# try:
#     print(makers)
# except NameError:
#     print('Вы не создавали переменню makers')


# raise

# number = int(input('Введите число от 1 до 70: '))
# if not number in range(1, 71):
#     raise Exception('Вы ввели число, не в том промежутке')
# print('Okey')