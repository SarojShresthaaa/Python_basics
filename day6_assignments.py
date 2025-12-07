# get a number from user and check if it is greater than 10
num = float (input("Enter a number: "))
if num > 10:
    print("It is greater than 10")
else:
    print("It is less than 10")

# get a number from user and check if it is even or odd
num1 = int (input("Enter a positive integer: "))
if num1<0:
    print("Please, Enter positive integer only")
elif num1%2 == 0:
    print("It is even number")
else:
    print("It is odd number: ")


#--------------------------------------------------------------------------------------------------
# create a dict of username and password.
# get username for user. if username exist in the list print "username exist"
# else print "username not found"
username_dict = {
    'username_1': 'Ram',
    'username_2': 'John',
    'username_3': 'Kiki',
    'username_4': 'Rahul'
}
input_username = input("Enter a username: ")

if input_username == username_dict['username_1']:
    print("Username exist")
elif input_username == username_dict['username_2']:
    print("Username exist")
elif input_username == username_dict['username_3']:
    print("Username exist")
elif input_username == username_dict['username_4']:
    print("Username exist")
else:
    print("Username not found")


#--------------------------------------------------------------------------------------------------
# create a list of numbers
# get the greater number from the list
num_list = [-10,33,100,-713,464,-1,0]

#Using loop 
big_num = num_list[0]

list_length = len(num_list)
for i in range(list_length):
    if num_list[i] > big_num:
        big_num = num_list[i]

print(f"The largest num is: {big_num}")

#Using if-else
max_num = num_list[0]

if num_list[1] > max_num:
    max_num = num_list[1]
if num_list[2] > max_num:
    max_num = num_list[2]
if num_list[3] > max_num:
    max_num = num_list[3]
if num_list[4] > max_num:
    max_num = num_list[4]
if num_list[5] > max_num:
    max_num = num_list[5]
if num_list[6] > max_num:
    max_num = num_list[6]

print(f"The largest number is: {max_num}")


#--------------------------------------------------------------------------------------------------
#Student GPA calculator
student_marks = int (input("Enter your marks 0-100: "))

if student_marks > 100 or student_marks < 0:
    print("Please Enter your marks again")
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

#--------------------------------------------------------------------------------------------------
#Driving liscense age validation 

age = int (input("Enter your age: "))
if age >= 16:
    license_check = input("Do you have liscense: ")
    if license_check == "Yes":
        print("You can drive")
    else:
        print("You can't drive")

elif age < 16:
    print("You are not eligible to drive")
    question = input("Do you want to get liscense? ")
    if question == "Yes":
        print("You can apply after 16")
    else:
        print("Uninterested")

