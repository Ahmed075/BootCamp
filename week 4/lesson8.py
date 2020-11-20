# nums = list(range(5, 9))
# print(nums)


# my_list = [expression for item in list]

# for item in list:
#     expression


# my_list = [num * num for num in range(5)]
# print(my_list)

# list_ = ['askat bakytov', 'bakyt askatov', 'ermek aygulov', 'aygul mamatov']
# my_list = [word.title() for word in list_]
# print(my_list)


# my_list = [x * y for x in range(5) for y in range(5)]
# print(my_list)

# nums = [num for num in range(5) if num % 2 == 0]
# print(nums)

# nums2 = []
# for num in range(1, 10):
#     if num % 2 ==0:
#         nums2.append(num * 2)
# print(nums2)


# words = [word for word in [1, 2,]]

# nums = [num for num in range(1, 50) if num % 3 == 0 and num % 5 == 0]
# print(nums)


# nums = ['even' if num % 2 == 0 else  for num in range(1, 20)]


# for num in range(1, 20):
#     print('even' if num % 2 ==0 else "odd")


# nums = [[i*j for j in range(1, 10)] for i in range(1, 10)]
# print(nums)

dict1 = {'a': 1, 'b':2, 'c':3, 'd': 4}
dict2 = {'even' if value % 2 == 0 else key: 'odd' for (key, value) in dict1.items()}
print(dict2)