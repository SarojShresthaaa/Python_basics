# implement for loop to print each hobbies
hobbies = ["reading", "coding", "gaming", "sleeping"]

for i in hobbies:
    print(f"My hobby is {i}")

# get a number from user and print the multiplication table of the number using for loop
user_input = int (input("Enter a number: "))
for i in range(1, 11):
    print(f"{user_input} * {i}  {user_input * i}")


# create a dictionary with names and age, get names from user
# check if name exist in the dictionary,
# if exist print the age of the person, else print user not found

user_dict = {"ram": 25, "shyam": 30, "hari": 22}

input_name = input("Enter a name: ")

if input_name in user_dict:
    print(f"Age of {input_name}, is {user_dict[input_name]}")
else:
    print("User not found")


