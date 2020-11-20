# dict1 = {}
# dict2 = dict()

# print(type(dict1))
# print(type(dict2))

# dict_ = {"name": "Sam", "last_name": "White", "age": 23}
# print(dict_)

# dict_ = dict(a=1, b=2, c=3)
# print(dict_)

list_ = [['m', 1], ['a', 2], ['k', 3]]

dict_ = dict(list_, e=4, r=5, s=6)
print(dict_)


# dict_ = {1: 'Makers', '2': True, False: []}
# print(dict_)

# dict_ = {[]: 'list'}
# print(dict_)

# print(dir(int))


#  Python 3.6

# dict[key] = value

# dict_ = {'Toma': 'black', 'Alice': 'pink', 'Sam': 'yellow'}
# dict_['Sam'] = 'green'
# dict_['Rachel'] = 'blue'
# print(dict_)


# dict_ = {'Toma': 'black', 'Alice': 'pink', 'Sam': 'yellow', 'Rachel': 'pink'}
# print(dict_)


# """Method"""

# 1. get(key, None)

# dict_ = {1: 'Tom', 2: "John", 3: 'Alice'}
# print(dict_.get(4, 'no such key in directory'))
# print(dict_.get(4))
# print(dict_[4])


# 2. clear()
# dict_ = {1: 'Tom', 2: "John", 3: 'Alice'}

# dict_.clear()
# print(dict_)

# 3. copy()

# dict_1 = {1: 'Tom', 2: "John", 3: 'Alice'}

# dict_2 = dict_1.copy()

# dict_1[3] = 'Rachel'
# print(dict_1)
# print(dict_2)

# 4. items()

# dict_ = {'name': 'Kate', 'hegiht': 1710, 'weight': 58}
# print(dict_.items())


# 5. keys() values()

# dict_ = {'name': 'Kate', 'hegiht': 1710, 'weight': 58}

# print(dict_.keys())
# print(dict_.values())


# 6. pop()

# dict_ = {'name': 'Kate', 'height': 170, 'weight': 58}

# print(dict_.pop('age'))
# print(deleted_pair)
# print(dict_)


# 7. popitem()

# dict_ = {'name': 'Kate', 'height': 170, 'weight': 58}

# deleted_pair = dict_.popitem()
# print(deleted_pair)
# print(dict_)


# 8. setdefault(key, value)

# dict_ = dict(a=1, b=2, c=3, d=4)
# print(dict_.setdefault('d', 5))


# print(dict_)

# dict_['d'] = 5
# print(dict_)


# 9. update()


# dict_1 = {1: 'Tom', 2: "Alice"}

# dict_2 = {2: 'Bob', 4: 'Ann'}

# dict_1.update(dict_2)
# print(dict_1)
# print(dict_2)


# 10. fromkeys()

# numbers = [1, 2, 3, 4, 5,]
# new_dict = dict.fromkeys(numbers, 'Makers')

# print(new_dict)


# nested_dictionary = {
#     'Makers': {
#         'Aibek': 23,
#         'Adilet': 27,
#         'Aidai': 25

#     }
# }
# print(nested_dictionary['Makers']['Aidai'])


# university = {
#     'програмирование': 150,
#     'экономика': 98,
#     'медицина': 82
# }
# a
# university['экономика'] = 120

# b
# university.setdefault('лингвистика', 56)
# university.update({'лингвистика': 56})
# university['лингвистика'] = 56

# print(university)


# c
# university.pop('медицина')
# print(university)


# all_students = list(university.values())
# print(sum(all_students))


# Task 2

# dictionary = {1: 'a', 2: 'b', 3: 'c'}
# print(dictionary)
# some_dictionary = list(dictionary.items())

# print(some_dictionary)

# tuple1 = tuple(reversed(some_dictionary[0]))
# tuple2 = tuple(reversed(some_dictionary[1]))
# tuple3 = tuple(reversed(some_dictionary[-1]))

# new_dictionary = dict([tuple1, tuple2, tuple3])
# print(new_dictionary)