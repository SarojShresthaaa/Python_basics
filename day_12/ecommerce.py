# Ecommerse
# create a dict that consists username, password, usertype(buyer,seller)
# [{"username":"ram","password":"123","usertype":"seller"},{"username":"shyam","password":"123","usertype":"buyer"}]
# create a dict that consists product list(name, description, price, seller_name:"ram")

# get username and password from user, check if it exists in the dictionary, if it exists get the usertype
# check if the usertype is buyer or seller,
   # if seller: show choices 1. view my product
   # if buyer: show choice 1. view all product 2. buy product 
      # if choice 1 show all product
      # if choice is 2. ask user what they want to buy, quantity and show the total price (price*quantity)

user_login = [
    {
        "username": "ram",
        "password": "ram123",
        "usertype": "seller"
    },
    {
        "username": "shyam",
        "password": "shyam123",
        "usertype": "buyer"
    },
    {
        "username": "hari",
        "password": "hari123",
        "usertype": "seller"
    },
    {
        "username": "kiki",
        "password": "kiki123",
        "usertype": "buyer"
    }
]

product_list = [
    {
        "name": "shoe",
        "description": "adidas running shoe",
        "price": 5000,
        "currency": "Rs",
        "seller_name": "ram"
    },
    {
        "name": "tshirt",
        "description": "cotton casual tshirt",
        "price": 1200,
        "currency": "Rs",
        "seller_name": "hari"
    },
    {
        "name": "watch",
        "description": "digital sports watch",
        "price": 2500,
        "currency": "Rs",
        "seller_name": "ram"
    },
    {
        "name": "bag",
        "description": "travel backpack",
        "price": 3000,
        "currency": "Rs",
        "seller_name": "hari"
    }
]


#Buy products
def buy_products():
    buy_name = input("Enter product name to buy: ")
    
    for i in product_list:
        if i["name"] == buy_name:
            ask_quantity = int(input("Enter quantity: "))
            total = i["price"] * ask_quantity
            print(f"Total price = {total}")
            return
    print("Product not found")

# Buyer section
def buyer():
    choice = input("Enter 1 to view all products, Enter 2 to buy a product: ")

    if choice == "1":
        for i in product_list:
            print(i)

    elif choice == "2":
        buy_products()


# Seller section
def seller(name):
    choice = input("Enter 1 to view your products: ")

    if choice == "1":
        for i in product_list:
            if i["seller_name"] == name:
                print(i)



# check_usertype
def check_usertype(name):
    for i in user_login:
        if i["username"] == name:
            if i["usertype"] == "seller":
                seller(name)
            elif i["usertype"] == "buyer":
                buyer()
            return



# Login function
def login(name, passw):
    for i in user_login:
        if name == i["username"] and passw == i["password"]:
            print("Login successful!")
            check_usertype(name)
            return

    print("Invalid username or password")


# Input login
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

login(username_input, password_input)

