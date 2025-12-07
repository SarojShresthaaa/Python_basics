#Calculator
while True:
    num_1 = float(input("Enter a number: "))
    op = input("Enter operator (+, -, *, /, //, %): ")
    num_2 = float(input("Enter another number: "))

    if op == "+":
        print("Sum:", num_1 + num_2)
    elif op == "-":
        print("Subtraction:", num_1 - num_2)
    elif op == "*":
        print("Multiply:", num_1 * num_2)
    elif op == "/":
        print("Division:", num_1 / num_2)
    elif op == "//":
        print("Floor_Div:", num_1 // num_2)
    elif op == "%":
        print("Modulo:", num_1 % num_2)
    else:
        print("Enter the correct operator")

    user_option = input("Do you want to calculate again? (Yes/No): ")
    if user_option != "Yes":
        break

print("Program finished.")


# Take two number from user, find greater num in list
# Print max num using while loop
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

num_list = [a, b]

length_of_list = len(num_list)
max_num = num_list[0]

i = 1
while i < length_of_list:
    if num_list[i] > max_num:
        max_num = num_list[i]
    i = i + 1

print("Maximum number is:", max_num)
