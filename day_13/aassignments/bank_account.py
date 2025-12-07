# Accounting Program: implement file handling(2 file: userdata {"username":"password"} 
# save in text file, userbalance)
# give user 2 choices "Login" or "Register"
# if register, get username, password from user, store the data in a file
# if login, get username, password from user and check if the userdata exist in the file

# show 2 choice, add balce, view balance, if user choice is add, get amount from user and add the value to the initial balance, if choice is view then show the initial balance to the user
# if user does not exist in the dictironay, print out a statement

import json   # dictionary format is changed in json format and viseversa

choice = int(input("1. Register 2. Login "))

if choice==1:
   f= open("userFile.txt", 'a')
   username=input("Enter your username: ")
   password=input("Enter the password: ")
   user_detail = {username:password}
   json_user = json.dumps(user_detail) # dict convert json format
   f.write(json_user+'-')
   print("Registered successfully")

elif choice == 2:
   f= open("userFile.txt", 'r')
   username=input("Enter your username: ")
   password=input("Enter the password: ")
   a = f.read().split('-')  # list_datatype {"sdf":"asdf"}
   for i in a:
      if i != '':
         json_data = json.loads(i)    # json converted into dict
         if password == json_data.get(username):
            print("Login Success")
            
            # show 2 choice, add balce, view balance, if user choice is add, get amount from user and add the value to the initial balance, if choice is view then show the initial balance to the user
            # if user does not exist in the dictironay, print out a statement
            
            
            
         else:
            print("User data not found")