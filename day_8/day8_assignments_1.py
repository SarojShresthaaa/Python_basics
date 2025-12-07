# # 1. Write a program that converts a temperature from Celsius to Fahrenheit.
# # Formula: F = (C × 9/5) + 32.

# temp_celsius = float (input("Enter temperature in Celsius: "))

# temp_fahrenheit = (temp_celsius * (9/5)) + 32
# print(temp_fahrenheit)


#--------------------------------------------------------------------------------------------------
# # 2.Write a program that asks for the user's age as input (string),
# # converts it to an integer, and calculates what their age will be in 10 years.

# input_age = input("Enter your age: ")
# user_age = int(input_age)
# age_in_10_years = user_age + 10

# print(age_in_10_years)


#--------------------------------------------------------------------------------------------------
# # 3.Write a program that takes a decimal number as input 
# # and prints both the integer part and the decimal part separately.
# decimal_input = float ("Enter a decimal: ")



#--------------------------------------------------------------------------------------------------
# # 4.Create a program that calculates the average of five numbers entered by the user.
# num_list = []
# i=0
# while i<5:
#    input_num = int( input("Enter a number: "))
#    num_list.append(input_num)
#    i += 1

# # Calculating average
# total = 0
# for i in num_list:
#     total = total + i

# average = total / len(num_list)
# print(average)


#--------------------------------------------------------------------------------------------------
# # 5.Build a simple tip calculator: ask for the bill amount and tip percentage, 
# # then calculate the tip and total.

# bill_amount = []
# count = 0

# while True:
#     user_input = float(input("Enter the bill amount: $ "))
#     bill_amount.append(user_input)
#     count += 1
    
#     if count >= 4:
#         more_input = input("Is there more amounts to enter (yes/no): ")
#         if more_input != "yes":
#             break

# # Calculate total 
# total = 0
# for i in bill_amount:
#     total += i
# print(f"The total is: {total}")

# # Calculate tip
# tip_percentage = float(input("What percentage of total is given as tip? : "))
# tip = total * (tip_percentage/100)
# print(f"You should give ${tip} tip")


#--------------------------------------------------------------------------------------------------
# # 6.Use //= to repeatedly divide a number by 2 until it becomes 1.
# # How many divisions did it take? Print it out
# input_num = int(input("Enter a number: "))
# count = 0

# if input_num <= 0:
#     print("Please enter a number greaten than 0")
# elif input_num == 1:
#     print("It took 0 divisions.")
# else:
#     while input_num > 1:
#         input_num //= 2
#         count += 1

# print(input_num)
# print(f"It took {count} divisions")


#--------------------------------------------------------------------------------------------------
# # 7. Create a program that checks if a number is between 1 and 100

# user_input = int (input("Enter a number: "))
# if user_input > 1 and user_input < 100:
#     print("the number  is between 1-100")
# else:
#     print("Enter number between 1-100")


#--------------------------------------------------------------------------------------------------
# # 8. Write a program that checks if a user's input contains the word "Python".
# user_input = input("Enter a string: ")
# check = "Python" in user_input
# if check == True:
#     print("Yes, it contains Python")
# else:
#     print("No, it doesn't contain Python")


#--------------------------------------------------------------------------------------------------
# 9. Ask for a sentence and check if it contains any vowels (a, e, i, o, u)
# user_input = input("Enter a sentence: ").lower()
# vowels = "aeiou"

# vowel_check = False   
# for i in vowels:
#     if i in user_input:
#         vowel_check = True
#         break

# if vowel_check == True:
#     print("Yes, it contains vowels")
# else:
#     print("No, it doesn't contain any vowels")


#--------------------------------------------------------------------------------------------------
# # 10. Write a program that determines if a triangle is valid 
# # (sum of any two sides must be greater than the third side)
# three_angles = []

# for i in range(3):
#     input_angles = int (input("Enter a angle of triangles: "))
#     three_angles.append(input_angles)
    
# total_sum = three_angles[0] + three_angles[1] + three_angles[2]

# if (three_angles[0] + three_angles[1] > three_angles[2] and
#     three_angles[1] + three_angles[2] > three_angles[0] and
#     three_angles[0] + three_angles[2] > three_angles[1]):
#     if total_sum == 180:
#         print("It is a valid triangle.")
#     else:
#         print("Invalid triangle. Total sum must be 180.")
        
# else:
#     print("Invalid triangle. Sum of two angles must be greater than the third.")


#--------------------------------------------------------------------------------------------------
# # 12. Calculate the sum of numbers from 1 to n (n is the user input)
# n = int(input("Enter a positive number (n): "))

# if n <= 0:
#     print("Please enter a positive number!")
# else:
#     # Using formula
#     total = n * (n + 1) / 2
#     print(f"The sum of numbers from 1 to {n} is: {total}")


#--------------------------------------------------------------------------------------------------
# # 13. Write a program that keeps asking for a password until the correct one is entered.
# passwords_list = ["admin123", "Kart333", "ram999"]

# while True:
#     user_input = input("Enter a password: ")
    
#     if user_input not in passwords_list:
#         print("Incorrect password. Try again.")
#     else:
#         break

# print("Access granted!")


#--------------------------------------------------------------------------------------------------
# # 14. Write a program that counts how many vowels are in a string.

# user_input = input("Enter a string: ").lower()

# vowels = "aeiou"
# count = 0

# for i in user_input:
#     if i in vowels:
#         count += 1

# print("Number of vowels:", count)









