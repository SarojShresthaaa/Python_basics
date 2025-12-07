#Indexing and Slicing

b = 'i am a (programmer)'
#Print ( 
print(b[7])

my_list = ['sdjfkdjf', 'b', 'jf', '5']
print(my_list[3])


my_tuple = ['sdjfkdjf', 'b', 'jf', '5']
print(my_tuple[2])


#Assignments:

color = ["red", "blue","green", "pink", "orange", "yellow", "purple"]
#Using positive index
print(color[2])
#Using negative index
print(color[-2])
rgb = color[:3]
print(rgb)

number = [0, 10, 20, 30, 40, 50, 60, 70]
print(number[::3])
print(number[:-1])
multiple = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#print 5
print(multiple[1][1])
#print 9
print(multiple[-1][-1])