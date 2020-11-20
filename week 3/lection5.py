# print(type(4 > 3))

# print('makers' > 'bootcamp')
# ord()

# print(ord('b'))

# chr() 
# print(chr(98))

# print(type(False))

# a = True # = 1
# b = False # = 0
# print(int(True))
# print(int(False))

# print(bool(3.4))
# print(bool(-200))
# print(bool(0))
# print(bool(' '))
# print(bool(""))

# a = 'MAKERS'
# b = 10

# print(a if b > 0 else 'makers')


# Разбор

# Логические операторы - операторы сравнения - КОНСТРУКЦИЯ  (if)


# ?=product_title=samsung
# if product_title:
#     result
# else:
#     raise Exception    


# Bool --- True or False


# == Равно - equal
# != Не равно - not equal
# < меньше
# > больше
# <= меньше или равно
# >= больше или равно
# = присвоение

# num1 = 13
# num2 = 15
# print("num1 == num2", num1 == num2)
# print("num1 != num2", num1 != num2)

# password1 = input("Enter your password")
# password2 = input("Repeat password")
# if password1 != password2:
#     raise Exception("Password1 and password2 didnt match") для ошибки 
# else:
#     print("Ok password successful created!")
    

# num1 = 13
# num2 = 15
# print("num1 < num2", num1 < num2)
# print("num1 > num2", num1 > num2)



# num1 = 13
# num2 = 15
# print("num1 <= num2", num1 <= num2)
# print("num1 >= num2", num1 >= num2)


# name1 = "John"
# name2 = "Patrick"
# print(name1 == name2)


# name1 = "R"
# name2 = "r"
# print(name1 > name2)
# print(ord('R'))
# print(ord('r'))



# true_ = True
# false_ = False
# print("True != False", true_ != false_)

# print(True == 1)
# print(False == 0)


# email = input("Enter your email: ")
# username = input("Enter your username: ")
# password1 = input("Enter your password: ")
# password2 = input("Repeat password: ")
# if email and username and password1 and password2:
#     if password1 != password2:
#         raise Exception("Password1 and Password2 didn't match ")

#     elif '@' not in email:
#         raise Exception("Email is not valid ")

#     elif not len(username) >= 8:
#         raise Exception("Username is not valid ")

#     else:
#         print("Ok User successfuly created!")
# else:
#     raise Exception("Fields cannot be empty")        


# test = input("Введите данные: ")






# print(True or False)
# my_age = 23
# your_age = 21
# result = (my_age == 23) and (your_age == 21)
# print(result)


# print(True or False)



# this_func_will_return_true = 3 > 1
# this_func_will_return_false = 4 < 3
# results = this_func_will_return_true or this_func_will_return_false
# print(results)
# Camelcase

# print(not False)
# var1 = 5 < 4
# results = not var1
# print(results)


# print(!False)

# ==
# print(True == True)  #True
# print(True == False) #False
# print(False == False) #False
# print(False == True) #True
# Or
# print(True and True) #True 
# print(True and False) #True
# print(False and True) #True
# print(False and False) #False

# Not
# print(not True) #False
# print(not False) #True


# Empty value and not empty

# print(bool(2))
# print(bool(-55))
# print(bool(22.1))
# print(bool(0))
# print(bool(3))

# Структуры данных List, Tuple, Set, Dict

# print(bool((1, 2, 3)))
# print(bool(tuple()))
# print(bool((1, 2)))
# print(bool([]))
# print(bool(set()))
# print(bool({1, 2, 3}))
# print(bool({}))
# print(bool({1:1}))

# var = (1, )
# var2 = [1, ]
# print(type(var))
# print(type(var2))



# if - если
# else - иначе
# elif - если иначе --> else if

# grade = input("Enter your grade: ")
# if grade == 5:

# grade = int(input("Enter your grade: "))
# if grade == 5 or grade == 3:
    
#     print("Great! ") 
# else:
#     print("Bad!:(")


# point = input("Введите оценку: ")
# if point == "5":
#     print("Молодец, так держать")
# elif point == "4":
#     print("Эхх, Еще немного и ты крут")
# elif point == "3":
#     print("Махатса будешь сомной")
# elif point == "2":
#     print("До крови до смерти")    
# else:
#     print("Лох")


# cars = ["bmw", "audi", "honda", "mercedes", "toyota", "aston", "tesla", "termo", ""]
# results = []

# search_text = input("Введите ключевое слово: ")
# for car in cars:
#     if search_text == car:
#         results.append(car)
#     if search_text.endswith('a') and car.startswith('a'):
#         results.append(car)     
#     else:
#         continue    
# print(results)




# is_user_facebook_user = True
# is_user_github_user = True
# is_users_age_greate_18 = True
# user_account_money = 1000


# if (is_user_facebook_user and is_user_github_user) and (is_users_age_greate_18 and user_account_money > 999):
#     print("You can Enter the sistem!!! ")
# else:
#     print("Sorry, you should have Facebook and Git hub accounts")


# user_is_logged_in = True
# user_has_twitter_account = True
# user_has_linkedin_account = True

# if user_is_logged_in:
#     print("logged in")
# elif user_has_twitter_account:
#     print("user_has_twitter_account")    
# elif user_has_linkedin_account:
#     print("user_has_linkedin_account")    



