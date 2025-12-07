dict_1 = {
    "ram": 25,
    "kin": 44,
    "jim": 33,
    "kiki": 8
}

input_username = input("Enter the username")
for i in range(5):
    if input_username == dict_1[i]:
        print("username exist")
