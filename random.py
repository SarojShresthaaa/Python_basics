a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

num_list = [a, b]

length_of_list = len(num_list)
max_num = num_list[0]

i = 1
while i < length_of_list:
    if num_list[i] > max_num:
        max_num = num_list[i]
    i = i + 1

print("Maximum number is:", max_num)
