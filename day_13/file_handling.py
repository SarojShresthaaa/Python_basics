choice = input('''Enter 1. to register 
2. to Login''')

if choice == "1":
    input_username = input("enter your username: ")
    f = open('file.txt', 'w')
    f.write(f"username: {input_username}")
elif choice == "2":
    input_username = input("enter your username: ")
    f = open('file.tx', 'r')
    f.read(f"username: {input_username}")
