# Множество
# {} --

# {'key': 12, 'key': 14}

# {'key', 'key'}

# {1, 1, 1, 1}

# hash_func(value) --> hashvalue
# hash_func(1) --> hashvalue --> 13
# hash_func(1) --> hashvalue -->13


# numbers = {1, 1, 2, 2, 3, 3, 4, 5}
# print(type(numbers))
# print(numbers)


# empty_set = set()
# print(type(empty_set))



# первый вариант
# phone_numbers = [
#     777, 999, 777, 555, 999, 111
# ]
# unique_phone_numbers = list(set(phone_numbers))
# print(unique_phone_numbers)



# второй вариант
# phone_numbers = [
#     777, 999, 777, 555, 999, 111
# ]
# unique_phone_numbers = []
# for number is phone  numbers:
#     if number not in unique_phone_numbers:
#         unique_phone_numbers.append(number)
#     else:
#         continue
# print(unique_phone_numbers)            


# print(dir(set()))


# ---
# set  
# users = {'John', 'Raychel', 'Peter', 'Jane', 'Rick'}
# print("Before:", users)
# users.add('Sandy')
# users = list(users)
# users.sort(reverse=True)
# print("After: ", users)
# Method (add)

# ----
# users = {'John', 'Raychel', 'Peter', 'Jane', 'Rick'}
# print("Before: ", users)
# # users.discard('John')
# # print("After: ", users)
# # Method set().discard

# # Method remove() -- Key Error
# users.remove('John')
# print('After: ', users)


# Method pop()
# cars = {'honda', 'toyota', 'bmw', 'audi'}
# print('Before: ', cars)
# removed = cars.pop()
# print('After: ', cars)
# print('removed: ', removed)


# Method clear()
# numbers = {1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3}
# print('before: ', numbers)
# numbers.clear()
# print('after: ', numbers)


# set_ = {(1, 1, 1) 'hello'}
# print(set_)

# [12, 13] --> 13yt
# [12, 13, 14] --> 


# Method union
# months_a = set(['Jan', 'Februar', 'March'])
# months_b = set(['July', 'Aug', 'Sep'])
# result = months_a.union(months_b)
# print(result)


# set_1 = {1, 1, 2, 2}
# set_2 = {3, 3, 4, 4}
# set_3 = {5, 5, 6, 6}
# set_4 = {7, 7, 8, 8}
# all_result = set_1.union(set_2, set_3, set_4)
# print(all_result)

# [] += [] += []


# set_1 = {1, 1, 2, 2}
# set_2 = {3, 3, 4, 4}
# set_3 = {5, 5, 6, 6}
# set_4 = {7, 7, 8, 8}
# all_results = set_1 | set_2 | set_3 | set_4
# print(all_results) 


# numbers = {1, 1, 2, 4}
# new_numbers = {5, 6, 4, 3}
# results = numbers | new_numbers
# print(results)

# intersection -- персечение
# users1 = {'John', 'Raychel', 'Peter'}
# users2 = {'Raychel', 'Jane', 'John', 'Rick', "Make"}
# results = users1.intersection(users2)
# print(results)


# users1 = {'John', 'Raychel', 'Peter'}
# users2 = {'Raychel', 'Jane', 'John', 'Rick', "Make"}
# users3 = {'Jane', 'Rick', 'Raychel'}
# results = users1 & users2 & users3
# print(results)


# -----------
# phone_numbers1 = set([777, 888, 777, 999, 666, 555, 555])
# phone_numbers2 = set([111, 222, 333, 777, 555, 666])

# difference_set1 = phone_numbers1.difference(phone_numbers2)
# difference_set2 = phone_numbers2.difference(phone_numbers1)

# print(difference_set1)
# print(difference_set2)

# -------------

# phone_numbers1 = set([777, 888, 777, 999, 666, 555, 555])
# phone_numbers2 = set([111, 222, 333, 777, 555, 666])

# difference_set1 = phone_numbers1 - phone_numbers2
# difference_set2 = phone_numbers2 - phone_numbers1

# print(difference_set1)
# print(difference_set2)

# --------------

# nums1 = {1, 2, 3, 4, 5}
# nums2 = {4, 5, 6, 7, 8}

# symmetric_difference1 = nums1.symmetric_difference(nums2)
# symmetric_difference2 = nums2.symmetric_difference(nums1)

# print('symmetric_difference1: ', symmetric_difference1)
# print('symmetric_difference2: ', symmetric_difference2)

# --------------


# nums1 = {1, 2, 3, 4, 5}
# nums2 = {4, 5, 6, 7, 8}

# symmetric_difference = nums1 ^ nums2
# print(symmetric_difference)

# ------------
# >=
# <=
# users1 = {'John', 'Raychel', 'Jane', 'peter'}
# users2 = {'John', 'Raychel', 'Jane', 'jane'}
# subset = users1.issubset(users2) #Bool value
# superset = users1.issuperset(users2) #Bool value
# print(subset)
# print(superset)
# -------------


# set_1 = {1, 1, 2, (1, 1)}
# set_copy = set_1.copy()
# print(set_copy)
# --------------

# names_1 ={'Peter', 'Jhon', 'Raychel'}
# names_2 = {'Rick', 'Mike', 'John'}
# print(names_1.isdisjoint(names_2))
# print(names_1 & names_2)

# if names_1.isdisjoint(names_2):
#     print("нет пересичение")
# else:
#     print("есть пересичение")


# frozen_set = frozenset([1, 2, 3, 4, 5])
# print(type(frozen_set))
# print(dir(frozen_set))

# print(dir(set()))