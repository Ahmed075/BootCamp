# Темв: Dictionary -Словари

# {}--'key': value
# {'key': 'value'}
# pep 8

# Dictionary -- {}
# {'key1': 'value', 'key2': 'value2'}
# 0(1)
# 0(n)

# Hash tables = Хеш таблицы
# Асоциативные массивы
# 'key1' --> хеш функция (key1) --> хэш ключ: 12
# 'key2' --> хеш функция (key1) --> хэш ключ: 13
# 'key' --> хеш функция (key1) --> хэш ключ: 12


# names = [12, 13, 14, ]
# names = {'name1': 'John', 'name2': 'Raychel'}
# print(names)
# print(names['name1'])
# print(names['name2'])
# print(names['name3'])
# print(names)


# numbers --- unhasheble - immutable
# string --- unhasheble - immutable
# frozenset --- unhasheble - immutable
# tuple --- unhasheble - immutable


# new_dict = dict(
#     [[1, 1], [2, 2]]
# )

# print(new_dict)

# class dict(dict):
#     def__hash__(self):
#         return sum(self)

# dict_ = dict([(1, 1), (2, 2)])
# print(dict_)
# print(hash(dict_))

# name = 1
# name = 2


# print(dir({'key': 12}))


# laptops = {'macbook': 'Pro', 'lenovo': 'Ideapad', 'Asus': 'Zenbook', 'Acer': 'Aspire'}
# print(type(laptops))
# values = list(laptops.values())
# print(values)
# print(type(values))

# Method - возврощает только значания
# Method {}.keys()


# laptops = {'macbook': 'Pro', 'lenovo': 'Ideapad', 'Asus': 'Zenbook', 'Acer': 'Aspire'}
# keys = laptops.keys()
# print(keys)


# print(dir({}))


# laptops = {'macbook': 'Pro', 'lenovo': 'Ideapad', 'Asus': 'Zenbook', 'Acer': 'Aspire'}

# CRUD - Create Read Update Delete
# create
# laptops['macbook'] = 'Air'

# update
# laptops['macbook'] = 'Pro 2017'

# get - retrieve - read
# print(laptops['macbook'])
# print(laptops)

# print(laptops.get('mac'))

# laptops.get('mac') = 'Hello'


# students = {'st1': 'John Snow', 'st2': 'John Connor', 'st3': 'Raychel Mcadams'}
# values_and_keys = list(students.items())
# values_and_keys.append((1, 1))
# dict_ = dict(values_and_keys)
# print(values_and_keys)
# print(dict_)

# method {}.items() --> [('key', 12), ('key', 14)]
# dict_items([(1, 1, 1]) - - > convert list - -> [(1, 1)]



# students = {'st1': 'John Snow', 'st2': 'John Connor', 'st3': 'Raychel Mcadams'}

# print('before:', students)

# removed = students.pop('st1')

# print('after:', students)

# print(removed)




# Method --> {}.popitem

# students = {'st1': 'John Snow', 'st2': 'John Connor', 'st3': 'Raychel Mcadams'}

# print('before:', students)
# removed = students.popitem()
# print('after:', students)
# print('return', removed)


# users = {'user1': 'test@example.com', 'user2': 'User2@example.com'}
# print('before:', users)
# print(users.setdefault('user3',))
# print('after:', users)

# users = {'user1': 'test@example.com', 'user2': 'User2@example.com'}
# new_users = {'user2': 'user3@gmail.com', 'user': 'user4@gmail.com' }
# print('before: ', users)
# users.update(new_users)
# print('after: ', users)


# new_users = {'user1': 'user3@gmail.com', 'user4': 'user4@gmail.com' }
# print('before: ', users)
# users.update(new_users)
# print('after: ', users)


# users = {'user1': 'test@example.com', 'user2': [1, 2]}

# print(users)
# print('before: ', users)

# users.clear
# print('after ', users)

# new_copy_users = users.copy()
# new_copy_users['users2']{0} = 'Hello World'
# print(new_copy_users)
# print(users)

# example = dict.fromkeys({1:5, 2:6}.keys(), 12)
# print(example)



# list() -- []
# tuple() --[]
# ....
# int()



