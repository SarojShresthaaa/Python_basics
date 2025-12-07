# # Simple Calculator

# num1 = int (input("Enter a number: "))
# num2 = int(input("Enter another number: "))

# def add(a, b):
#     print(f"Addition is: {a + b}")

# def mul(a, b):
#     print(f"Multiplication {a * b}")

# def div(a, b):
#     print(f"Division is: {a / b}")

# def sub(a, b):
#     print(f"Subtraction is: {a - b}")

# def floor_div(a, b):
#     print(f"Floor division: {a // b}")

# def calculator():
#     add(num1, num2)
#     mul(num1, num2)
    
#     try:
#         div(num1, num2)
#         floor_div(num1, num2)
#     except ZeroDivisionError:
#         print("Can't divide by zero")

#     sub(num1, num2)

# calculator()


#--------------------------------------------------------------------------------------------------
# # get user information like name, age, address,.....
# # create a function that prints out the introduction of the user


# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# address = input("Enter your address: ")

# def intro(name, age, address):
#     print(f"My name is {name}. I am {age} years old. I live in {address}.")

# intro(name, age, address)


#--------------------------------------------------------------------------------------------------
# # get two number from user.
# # create a function that print out the addition of 2 numbers
# def user_input(c):
#     while True:
#         try:
#             return int(input(c))
#         except ValueError:
#             print("Enter numeric values only")

# num_1 = user_input("Enter a number: ")
# num_2 = user_input("Enter another number: ")

# def add(a, b):
#     return a + b

# print(add(num_1, num_2))


#--------------------------------------------------------------------------------------------------
# # Celsius to Fahrenheit
# def cel_input(c):
#     while True:
#         try:
#             return float(input(c))
#         except ValueError:
#             print("Enter correct temperature")

# temp_celsius = cel_input("Enter temperature in Celsius: ")

# # Function
# def cel_to_fahr(cel):
#     temp_fahrenheit = (temp_celsius * 9/5) + 32
#     print(f"Temperature in Fahrenheit: {temp_fahrenheit}")

# cel_to_fahr(temp_celsius)


#--------------------------------------------------------------------------------------------------
# # get a number from user
# # create a function to check if it is even or odd.

# get_num = int(input("Enter a number: "))

# def even_odd(n):
#     if n < 0:
#         print("Enter positive integers only")
#     elif n % 2 == 0:
#         print("Number is even")
#     else:
#         print("Number is odd")

# even_odd(get_num)


#--------------------------------------------------------------------------------------------------
# square of num
input_num = int(input("Enter a number: "))

def square(n):
    return n * n
print(square(input_num))