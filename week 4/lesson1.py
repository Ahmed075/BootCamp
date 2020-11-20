# for
# list_ = []
# for num in range(1, 21):
#     list_.append(num * 2)
# print(list_)    


# list comprehesion

# list_ = [num * 2 for num in range(1, 21)]
# print(list_)


# list_user = ['Alice', 'Sam', 'Sandy', 'Ben', 'John']
# invitations = ['You are invited ' + name for name in list_user]
# print(invitations)


# list1 = [10, 5, -6, -8, -12, 20, 3, 14, 4]
# list2 = [num for num in list1 if num % 2 == 0 or num % 3 == 0]
# print(list2)


# ak = ['1998', '2001y', '2008year', '2020']
# mab = [year for year in ak if year.isdigit()]
# print(mab)

# attar = ['Ahmed', 'Begaiym', 'Jakyp', 'Islam']
# attar = [len(imya) for imya in attar]
# print(attar)


# kagaz = [-5, -12, 0, 1, 2, 8, 4, 5, 7]
# kagaz = [z if z < 0 else z ** 2 for z in kagaz]
# print(kagaz) 

# kagaz = [-5, -12, 0, 1, 2, 8, 4, 5, 7]

# kagaz = [z if z < 0 else z ** 2 for z in kagaz]
# print(kagaz)

# kagaz = [-5, -12, 0, 1, 2, 8, 4, 5, 7]
# kagaz = [z if z < 0 else z ** 2 for z in kagaz if z % 2 == 0]

# print(kagaz)

# names = ['Ahmed', 'Islam', 'Margo', 'Will', 'Jacob0', 'Lili12', 'Stiv11', 'James']
# filtered_names = [
#     z + 'MAKERS'
#     if len(z) >= 5 
#     else z + 'makers' 
#     for z in names 
#     if z.isalpha()]
# print(filtered_names)


# names = ['Ahmed', 'Islam', 'Margo', 'Will', 'Jacob0', 'Lili12', 'Stiv11', 'James']
# filtered_names = []
# for z in names:
#     if z.isalpha():
#         if len(z) >= 5:
#             result = z + "MAKERS"
#             filtered_names.append(result)
#         else:
#             result = z +'makers'    
#             filtered_names.append(result)
# print(filtered_names)


# john = {'name': 'John', 'age': 22}
# raychel = {'name': 'Raychel', 'age': 21}
# martha = {'name': 'Martha', 'age': 20}

# users = [john, raychel, martha]
# ages = [user.get('age', None) for user in users]

# bigger = 0
# smaller = 0
# count = 0

# for age in ages:
#     if age >= 18:
#         bigger += 1
#     else:
#         smaller += 1
#     count += 1

# bigger = bigger * (100/count)
# smaller = smaller * (100/count)

# print(f'процент пользователей с возрастом больше 18: {round(bigger)} процента') 
# print(f'процент пользователей с возрастом меньше 18: {round(smaller)} процента') 


# matrix = [
#     [0, 2, 5, 6],
#     [7, 3, 0, 7],
#     [5, 7, 1, 6]
# ]

# # ucompress = [n for row in matrix for n in row]
# ucompress = []
# for row in matrix:
#     for n in row:
#         ucompress.append(n)
# print(ucompress)


# dict_abc = {'a': 1, 'b': 2, 'c': 3}
# dict_123 = {key.upper(): value +2 for key, value in dict_abc.items()}
dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': -4, 'e': -7}
new_dict = {key.upper(): value ** 3 for key, value in dict_abc.items() if value > 0}
print(new_dict)