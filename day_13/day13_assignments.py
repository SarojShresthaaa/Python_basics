# # give user 2 choices "Login" or "Register"
# # if register, get username from user, store the username in a file
# # if login, get username from user and check if the name exist in the file

# login = input('''Enter 1. signup
# >>>>>>2. login ''')

# if login == "1":
#     get_username = input("Enter your username: ")
#     file = open("login.txt", "a")
#     file.write(get_username + "\n")
#     file.close()
#     print("Signup successful!")

# elif login =="2":
#     input_username = input("Enter your username: ")
#     file = open("login.txt", "r")
#     usernames_in_file = file.read()
#     if input_username in usernames_in_file:
#         print("Login successful. Username exists in file")
#     else:
#         print("Username doesn't exist")
    

login = input('''Enter 1. signup
>>>>>>2. login ''')

if login == "1":
    get_username = input("Enter your username: ")
    get_password = input("Enter your password: ")
    file = open("user_data.txt", "a")
    file.write(get_username + "\n")
    file.write(get_password + "\n")
    file.close()
    print("Signup successful!")

elif login == "2":
    
    get_username = input("Enter your username: ")
    get_password = input("Enter your password: ")
    file = open("user_data.txt", "r")
    login_details = file.read()
    if get_username in login_details and get_password in login_details:
        print("Login successful. Username exists in file")
    else:
        print("Username doesn't exist")
   
