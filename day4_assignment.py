#Exercise 1:
username_list = ['John', 'Ram', 'Kim', 'Tom']
input_username = input('Enter a Username: ')

print(input_username in username_list)

#--------------------------------------------------------------------------------------------------

#Exercise 2:
animals = ('cat','dog','apple','cow','horse','buffalo','lion')

#Tuple are immutable. So, we change it to list to add new animal 
animals_list = list(animals)
animals_list[2] = 'tiger'
print(animals_list)

#Check whether rabbit exists in animal tuple
print('rabbit' in animals)

#--------------------------------------------------------------------------------------------------

#Exercise 3:
x = [1,2,3,4]
y = [1,2,3,4]
#y = [1, 2, 3, 4, x]

print(x not in y)

