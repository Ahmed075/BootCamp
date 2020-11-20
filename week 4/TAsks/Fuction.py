# def function():
    # print('The function is called')
    # return 'Makers'

# print(function())

# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1 + num2)
#     return num1 - num2

# print(substract())

# def get_name(informations):
#     if isinstance(informations, dict):
#         return informations.get('first_name')
#     else:
#         return None
# user = {'first_name': 'John', 'Last_name': 'Snow', 'age': 24}
# result = get_name(user)
# print(result)


# function get_name {
#     adaf
# }

# def  validate_user(email, password1, password2):
#     #Проверяем валидность паролей
#     if '@' not in email:
#         raise Exception('Email is invalid')
#     #Проверяем совпадение паролей
#     if password1 != password2:
#         raise Exception("Password didn't match")
#     return True

# def patrick_user(email, password1, password2):
#     user = {}
#     id_user = 0
#     #Проверяем валидность паролей
#     if '@' not in email:
#         raise Exception('Email is invalid')
#     #Проверяем совпадение паролей
#     if password1 != password2:
#         raise Exception("Password didn't match")
#     #Сохраняем user и увеличиваем id на 1
#     if validate_user(email, password1, password2):
#         user[id user] = (email, password1):
#         return user, {'status': 'succesfully created!!!' } 
#     else:
#         return None, {'status': 'Error!!!'}
#     user[id_user] = (email, password1)
#     id_user += 1
#     return user, {'status': 'succesfully created!!!'}

# email = input("Enter your email: ")
# password1 = input("Enter your password1: ")
# password2 = input("Enter your password2: ")


# result = create_user(email, password1, password2)
# print(result)


# # -----
# def sum_(num1, num2):
#     return num1 + num2

# def multiply(num1, num2):
#     return num1 * num2

# def substract(num1, num2):
#     return num1 - num2

# def divide(num1, num2):
#     result = None
#     try:
#         result = num1 / num2
#     except ZeroDivisionError:
#         raise Exception("You cannot divide number to zero")
#     return result

# def main():
#     num1 = float(input("Enter num1: "))
#     num2 = float(input("Enter num2: "))
#     operator = input("Choise(/ * + -):")
#     result = None

#     if operator == '+':
#         result = sum_(num1 , num2)
    
#     elif operator == '-':
#         result = substract(num1, num2)
    
#     elif operator == '*':
#         result = multiply(num1, num2)
    
#     elif operator == '/':
#         result = divide(num1, num2)
    
#     else:
#         raise Exception("Error")

#     print(result)
#     question = input("Do you want to continue? Yes or No: ")
#     if question.lower() == 'yes':
#         main()
#     else:
#         return result
#     return 'Калькулятор закончил свою работу'

# print(main())






# substract()

# variable = substract()
# print(variable)

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, substract()]
# print(list_)

# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1 + num2)
#     return num1 - num2

# def function():
#     print("I'm calling substract function")
#     variable = substract()
#     return variable

# print(function())


# def multiply(a, b):
#     return a * b

# print(multiply(6, 5))


# def get_word(word):
#     list_letters = list(word)
#     print(list_letters)
#     return list_letters

# def get_vowels(letters):
#     vowels = ['a', 'o', 'y', 'i', 'e', 'u']
#     list_vowels = [letter for letter in letters if letter in vowels]
#     print(list_vowels)
#     result = ''.join(list_vowels)
#     return result

# my_word = input('Enter the word: ')
# print(get_vowels(get_word(my_word)))


# def info(name, age):
#     return f'{name} is {age} years old.'

# print(info(19, 'Ahmed'))