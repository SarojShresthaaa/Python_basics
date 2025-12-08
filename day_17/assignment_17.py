# create a class Bank
# the class should have accountnumber and balance attribute
# the attributes should not be accessable through object
# define a method that print out the user_details (accountnumber, balance)
# create 3 objects

class Bank:
    def __init__(self, account_number, balance):
        self.__account_number = account_number   
        self.__balance = balance               

    def show_details(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")

user_1 = Bank(1, 443)
user_2 = Bank(2, 900)

user_1.show_details()
user_2.show_details()


# create a class named login.
# the class should have email and password attribute
# the attributes should not be accessable through object
# define a method that print out the user info (email, password)
# create 3 objects

class Login:
    def __init__(self, email, password):
        self.__email = email        
        self.__password = password  

    def print_info(self):
        print(f"Email: {self.__email}")
        print(f"Password: {self.__password}")


user_1 = Login("johndoe123@gmail.com", "johndoe123")
user_2 = Login("hari@gmail.com", "hari123")

user_1.print_info()
user_2.print_info()


