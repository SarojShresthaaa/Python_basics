
#Exercise: 1
num1 = int(input('Enter an integer: '))
op = input('Arithmetic operators(/,+,-,%,//,*): ')
num2 = int(input('Enter another integer: '))

if(op == '+'):
    print(num1 + num2)
elif(op == '-'):
    print(num1-num2)
elif(op == '*'):
    print(num1 * num2)
elif(op == '%'):
    print(num1 % num2)
elif(op == '//'):
    if(num2 != 0):
        print(num1 // num2)
    else:
        print("Can't divide by Zero")
elif(op == '/'):
    if(num2 != 0):
        print(num1 / num2)
    else:
        print("Can't divide by Zero")
else:
    print('Enter correct arithmetic operator')



#------------------------------------------------------------------------------------------------------
#Exercise: 2
input_number = int (input('Enter any positive integers: '))
if (input_number<0):
    print('Please Enter positive integers')
elif (input_number%2 == 0):
    print("Even number")
else:
    print("Odd number")


#------------------------------------------------------------------------------------------------------
#Exercise: 3
number_list = [38,94,43,2,10,7,33,72,1]

temp = 0
temp = number_list[0] + number_list[1]
print(f"Addition: {temp}")

temp -= number_list[2]
print(f"Subtraction: {temp}")

temp *= number_list[3]
print(f"Multiplication: {temp}")

temp /= number_list[4]
print(f"Division: {temp}")

temp //= number_list[5]
print(f"Floor_div: {temp}")

temp %= number_list[6]
print(f"Final answer is: {temp}")
