numbers = [5,3,11,5,33333,1,44,2]
greater_num = numbers[0]
if numbers[1]>greater_num:
    max = numbers[1]
else:
    numbers[1] = greater_num
    
print(greater_num)