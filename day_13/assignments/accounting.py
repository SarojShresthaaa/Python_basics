import json 

choice = int(input("Enter 1 to Register, 2 to Login: "))

if choice == 1:
    
    f = open("userFile.txt", 'a')
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user_detail = {username: {"password": password, "balance": 0}}
    json_user = json.dumps(user_detail)
    f.write(json_user + "-")
    f.close()
    
    print("Registered successfully!")

elif choice == 2:
    
    f = open("userFile.txt", 'r')
    a = f.read().split('-') 
    f.close()
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    user_found = False
    
    for i in a:
        if i != '':
            user_data = json.loads(i)  
            
            if username in user_data and user_data[username]["password"] == password:
                print("Login Success")
                user_found = True

                user_choice = int(input('''Enter 1 to Add balance and 2 to view balance'''))
                
                if user_choice == 1:
                    amount = float(input("Enter amount to add: "))
                    user_data[username]["balance"] += amount
                    print(f"New balance: {user_data[username]['balance']}")
                    
                    new_data = []
                    for i in a:
                        if i != '':
                            c = json.loads(i)
                            if username in c:
                                c = user_data  
                            new_data.append(json.dumps(c))
                    f = open("userFile.txt", "w")
                    f.write("-".join(new_data) + "-")
                    f.close()
                
                elif user_choice == 2:
                    print(f"Your balance is: {user_data[username]['balance']}")
                
                break
    
    if not user_found:
        print("Error, user not found")
