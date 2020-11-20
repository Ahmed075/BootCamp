
# num = int()
# if num % 3 == and num % 5 == 0:
#     print("HahaHoo") 
# elif num % 3 == 0:
#     print("Haha")    
# elif num % 5 == 0:
#     print("Hoo")    
# else:
#     print("Aaaaa")



# words = input("Enter your words: ")
# vowels = "aieulouy"
# for x in word:
#     print(True)
#     break
# else:
#     pass



# text = input("Enter author:")
# dict_ = {'ChyngyzA': 'Jamilya', 'AlexsandrDuma': 'Tri mushketera'}
# result = dict_.get(text, None)
# if result:
#     print(result)
# else:
#     text2 = input("Enter text: ")
#     dict_[text] = text2
# print(dict_)






# Тама циклы: For -- While
#start:end:step | 0:100:1

# for x in range(100):
#     print(id(x))

# x = 0 #12
# x = 1 #13
# x = 2 #14
# x = 3 #20


# pizza = [
#     "first_item", "second_item", "third_item",
#     "fourth_item", "fifth_item", "sixth_item",
#     "seventh_item", "and last_item"
# ]
# for item in pizza:
#     print(f"eating {item} of pizza")

# pizza = [
#     "first_item", "second_item", "third_item",
#     "fourth_item", "fifth_item", "sixth_item",
#     "seventh_item", "and last_item"
# ]
# enumerations = []
# for item in pizza:
#     new_item = item[:-5]
#     enumerations.append(new_item)
# print(enumerations)


# pizza = [
#     "first_item", "second_item", "third_item",
#     "fourth_item", "fifth_item", "sixth_item",
#     "seventh_item", "and last_item"
# ]
# enumerations = []
# for item in pizza:
#     new_item = item.split('_')[0]
#     element = new_item[0]
#     enumerations.append(new_item)
# print(enumerations)



# str_ = "Hello"
# # print(dir(str_))
# print(type(str_))
# var = str_.__iter__()
# # print(dir(var))

# print(var.__next__())
# print(var.__next__())
# print(var.__next__())
# print(var.__next__())
# print(var.__next__())
# print(var.__next__())


# str_ = "world"
# str_ = str_.__iter__()
# print(next(str_))
# print(next(str_))
# print(next(str_))
# print(next(str_))
# print(next(str_))
# print(next(str_))


# 12 + 14

# Break - если находит совпадение по условию, то он выходит из цикла
# continue - Пропускает


# pizza = [
#     "first_item", "second_item", "third_item",
#     "fourth_item", "fifth_item", "sixth_item",
#     "seventh_item", "and last_item"
# ]
# enumerations = []
# for item in pizza:
#     new_item = item.split('_')[0]
#     if new_item.startswith('s'):
#         continue
#     elif new_item.startswith('a'):
#         break
#     enumerations.append(new_item.title())
# print(enumerations)


# pizza = [
#     "first_item", "second_item", "third_item",
#     "fourth_item", "fifth_item", "sixth_item",
#     "seventh_item", "and last_item"
# ]

# enumerations = []

# for index, item in enumerate(pizza):
#     print(f"This is index {index}, and item --> {item}")
#     new_item = item.split('_')[0]
#     enumerations.append(new_item.title())
# print(enumerations)
# print(list(enumerate(pizza)))



# dict_ = {'key1': 1, 'key2': 3, 'key4': 12}
# print(dict_.keys())
# for x, y in dict_.keys():
# print(x, y)


# for перменная in последовательность:
#     for перменная in последовательностьЖ
#         действие()
#     действие()

# new_list = []
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for x in matrix:
#     for i in x:
#         if x not in new_list:
#             new_list.append(i)
#         else:
#             continue
# print(new_list)        

# 0(n2)

# while
# i = 0
# while i < 10:
#     print("hello")
#     i = i + 1


# i = 100
# while i > 0:
#     print("hello", i)
#     # i = i + 1
#     i -= 1




# password = "helloworld"
# input_ = ""
# popytka = 0
# while input_ != password:
#     input_ = input("Enter your password: ")
#     popytka += 1
#     if count >= 5:
#         break