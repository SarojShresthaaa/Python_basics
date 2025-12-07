# # get a user information(name, age, address)
# # get hobbies of users using args
# # other addition info like contact info using kwargs(phone, email, address)
# # print out introduction of the user

# input_name = input("Enter your name: ")
# input_age = input("Enter your age: ")
# input_address = input("Enter your address: ")

# hobbies = []
# count = int(input("How many hobbies do you have? "))

# for i in range(count):
#     hobby = input(f"Enter your hobby: ")
#     hobbies.append(hobby)

# def user_info(name, age, address, *args, **kwargs):
#     print(f'''My name is {name} and I am {age} years old. I live in {address}.
# My hobbies are: {args}. My contact info: {kwargs}''')

# user_info(input_name, input_age, input_address, hobbies, email="johndoe@gmail.com", number=911)



#--------------------------------------------------------------------------------------------------
# # create a dict of username and password {"ram":"ram123"}
# # create a dict of username and initial_balance {"ram":"100000"}
# # get username and password from user. check if it exist in the dictionary, 
# # if yes print "Login Success"
# # show 2 choice, add balance, view balance, if user choice is add, 
# # get amount from user and add the value to the initial balance,
# # if choice is view then show the initial balance to the user
# # if user does not exist in the dictironay, print out a statement

# my_dict = {
#     "ram": "ram123",
#     "kiki": "kiki123",
#     "hari": "hari123"
# }

# my_dict_1 = {
#     "ram": 1000,
#     "kiki": 1430,
#     "hari": 33423
# }
# get_username = input("Enter your username: ")
# get_password = input("Enter your password: ")

# def user_management():

#     if get_username in my_dict:
#         if my_dict[get_username] == get_password:
#             print("Login successful!")
#             choice = input("Do you want to add or view balance?: ")
#             if choice == "add":
#                 add_amount = int(input("Enter the amount to add: "))
#                 print(f"New balance is: {my_dict_1[get_username] + add_amount}")
#             else:
#                 print(f"Your initial balance is: {my_dict_1[get_username]}")
#         else:
#             print("Incorrect password!")
#     else:
#         print("Username does not exist!")

# user_management()


#--------------------------------------------------------------------------------------------------
# create a dict of username and password {"ram":"ram123"}
# create a dict of username and initial_balance {"ram":"100000"}
# get username and password from user. check if it exist in the dictionary, 
# if yes print "Login Success"
# show 2 choice, add balance, view balance, if user choice is add, 
# get amount from user and add the value to the initial balance,
# if choice is view then show the initial balance to the user
# if user does not exist in the dictironay, print out a statement

userdata = {"ram":"ram123","shyam":"shyam123","hari":"hari123"}
userbalance = {"ram":100000,"shyam":50000,"hari":30000}

def add_balance(uname):
   initial = userbalance[uname] 
   amount = int(input("Enter an amount to add: "))
   total = amount + initial
   return total

def view_balance(uname):
   balance = userbalance[uname]
   # print(f"YOur balance is {balance}")
   return balance


def login(name, passw):
   if passw == userdata[name]:
      choice = input("""Login Succuss
   1. Add balance
   2. View Balance
   >>>""")
      if choice == "1":
         total = add_balance(name)
         print(f"Your new balance is {total}")
      elif choice == "2":
         blc = view_balance(name)
         print(f"Your balance is {blc}")
         
   else:
      print("Invalid Credentials")


username = input("Username: ")
password = input("Password: ")

login(username, password)