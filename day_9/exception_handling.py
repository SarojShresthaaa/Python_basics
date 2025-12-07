# # Simple Calculator

# try:
#     num1 = float(input("Enter a number: "))
#     op = input("Enter an arithmetic operator (+, -, *, /): ")
#     num2 = float(input("Enter another number: "))

#     if op == '+':
#         result = num1 + num2
#     elif op == '-':
#         result = num1 - num2
#     elif op == '*':
#         result = num1 * num2
#     elif op == '/':
#         result = num1 / num2
#     else:
#         print("Invalid operator!")
#         exit()

#     print("Result:", result)

# except ZeroDivisionError:
#     print("Can't divide by zero")

# except ValueError:
#     print("Please enter number")


#--------------------------------------------------------------------------------------------------
# # Triangle
# try:
#     three_angles = []

#     for i in range(3):
#         input_angles = int (input("Enter a angle of triangles: "))
#         three_angles.append(input_angles)
    
#     total_sum = three_angles[0] + three_angles[1] + three_angles[2]

#     if (three_angles[0] + three_angles[1] > three_angles[2] and
#         three_angles[1] + three_angles[2] > three_angles[0] and
#         three_angles[0] + three_angles[2] > three_angles[1]):
#         if total_sum == 180:
#             print("It is a valid triangle.")
#         else:
#             print("Invalid triangle. Total sum must be 180.")
        
#     else:
#         print("Invalid triangle. Sum of two angles must be greater than the third.")

# except ValueError:
#     print("Invalid input! Please enter a number.")


#--------------------------------------------------------------------------------------------------
# # Celsius to Fahrenheit
# try:
#     temp_celsius = float(input("Enter temperature in Celsius: "))
#     temp_fahrenheit = (temp_celsius * 9/5) + 32
#     print(f"Temperature in Fahrenheit: {temp_fahrenheit}")

# except ValueError:
#     print("Invalid input! Please enter a number.")


#--------------------------------------------------------------------------------------------------
# try:
#     user_input = float(input("Enter a number: "))
    
#     if user_input > 1 and user_input < 100:
#         print("The number is between 1-100")
#     else:
#         print("It doesn't lies between 1-100")

# except ValueError:
#     print("Invalid input! Please enter a number.")


#--------------------------------------------------------------------------------------------------
# Student Grade Calculator
try:
    student_marks = int (input("Enter your marks 0-100: "))

    if student_marks > 100 or student_marks < 0:
        raise ValueError("Marks must be between 0 and 100")
    
    elif student_marks < 100 and student_marks >= 90:
        print("You got A+")
    elif student_marks < 90 and student_marks >= 80:
        print("You got A")
    elif student_marks < 80 and student_marks >= 70:
        print("You got B+")
    elif student_marks < 70 and student_marks >= 60:
        print("You got B")
    elif student_marks < 60 and student_marks >= 50:
        print("You got C+")
    elif student_marks < 50 and student_marks >= 40:
        print("You got C")
    else:
        print("Fail")

except ValueError:
    print("Enter valid marks")