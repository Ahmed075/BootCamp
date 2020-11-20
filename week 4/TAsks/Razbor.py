# def countingValleys(steps, path):
#     count = 0
#     trip = 0
#     for x in range(0, len(path)):
#         if path[x] == 'U':
#             count += 1
#             if count == 0:
#                 trip += 1
#         else:
#             count-=1
#         print(count) 
#     return trip
# print(countingValleys(8, 'UDDDUDUU'))


# def func(a, b, c=5):
#     return a + b + c
 
# print(func(5, 5, 6))


# Позционные аргумнты ||||||
# Именованные аргументы|||||


# def test_func(a, b, c):
#     return a + b + c

# print(test_func(1, 2, 3))


# def get_full_info(text, first_name, last_name, age):
#     full_info = f"{first_name} - {last_name} - {age}"
#     return full_info

# result = get_full_info('hello', last_name="Snow", age=23, first_name="John")
# print(result)


# def create(**kwargs):
#     print(args, kwargs)
#     dict_ = {}
#     dict_.update(**kwargs)
#     return dict_

# result = create({12, 13,'name': 'Raychel', 'age': 23})
# print(result)


# def func(*args, **kwargs):
#     print(args, kwargs)
#     print(*args)
#     dict_ = {}
#     dict_.update(**kwargs)
#     print(dict_)
# func(12, 12, test="hello")


# def func_one():
#     def func_two():
#         return "hello"
#     return func_two

# print(func_one()())



# print()
# dir()
# type()
# len()
# isinstance()
# max()
# min()

# for 
# while


# Function abs()
# num = -555
# absolute_value = abs(num)
# print(absolute_value)


# Function all()
# elements = [1, 2, 3, 4, 5, 1]
# result = all(elements)
# print(result)


# elements = [1, 2, 1]
# def all_(iterable_obj):
#     for item in iterable_obj:
#         if not item:
#             return False
#     return True

# result = all_(elements)
# print(result)




# Function any()
# names = ['John', "Raychel", 'Sandy', 'Jane', '']
# result = any(names)
# print(result)




# names = ['', False, 0, [], False]
# def any_(iterable_obj):
#     for item in iterable_obj:
#         if item:
#             return True
#     return False
# result = any_(names)
# print(result)


# ascii()
# \x \u \U

# result = ascii([0, 1, 'text'])
# result2 = ascii([10, 12, 'Привет'])
# print(result)
# print(result2)


# Function bin()
# one = bin(1)
# three = bin(3)
# num = bin(100)
# print('one', one)
# print('three', three)
# print('100', num)


# bool()

# print(bool(12))
# print(bool(0))


# Function callable()

# num = 12
# is_callable = callable(num)
# print(is_callable)


# Function callable()

# num = sum
# is_callable = callable(num)
# print(is_callable)




# def adder(a, b):
#     return a + b

# is_callable = callable(adder)
# print(is_callable)


# def __cal__

# Unicode
# chr()

# num1 = chr(100)
# num2 = chr(68)
# num3 = ord('D')
# num4 = ord('d')
# print('D', num1)
# print('d', num2)
# print('D', num3)
# print('d', num4)


# dict_

# dict_with_two_pairs = {'key1': 12, 'key2': 15}
# dict_with_keywords_creation = dict(key=12, key2=15)
# dict_ = dict([(1, 2), (3, 4)])
# print(dict_with_two_pairs)
# print(dict_with_keywords_creation)
# print(dict_)


# print(dir())
# import sys
# import json
# print(dir(sys))
# print(dir(json))


# num1 = 10
# num2 = 30
# result = divmod(num1, num2)
# print(result)



# seasons_year = ['Spring', 'Summer', 'Fail', 'Winter']
# Results = dict(enumerate(seasons_year, start=5))
# print(Results)