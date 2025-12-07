#Exercise 1:
color = ["red","blue","green","purple","yellow","orange"]
#Using positive index
print(color[2])
#Using negative index
print(color[-2])

rgb = color[:3]
print(rgb)

#--------------------------------------------------------------------------------------------------
#Exercise 2:
number = [0,10,20,30,40,50,60,70,80,90]
# print out the sequence with 3 interval
print(number[::3])
# print out the reverse of the sequence number
print(number[::-1])

# extract the data from even index and assign it to even variable
# extract the data from odd index and assign it to odd variable
even = number[::2]
odd = number[1::2]
print(even)
print(odd)

#--------------------------------------------------------------------------------------------------
#Exercise: 3
multiple = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#print 5
print(multiple[1][1])
#print 9
print(multiple[2][2])
# print out [4,5,6] from the sequence
print(multiple[1])

#--------------------------------------------------------------------------------------------------
#Exercise 4:
string = "PYTHON COURSE"
chara = ['A','j','P','R','V']
# print out "PYTHON" from string variable
print(string[:6])
# print out "PY" from the above string and assign it to a variable
new_string = string[:2]
print(new_string)
# replace the character 'j' in chara  with "PY"
chara[1] = new_string
print(chara)

#--------------------------------------------------------------------------------------------------
#Exercise 5:
my_dict = {
   "name":"ram",
   "age":"500",
   "address":"Kathmandu",
   "hobbies": ["reading","watching movies","go hiking","playing games"]
}


# print age, address, hobbies
print(f"My age is {my_dict["age"]}")
print(f"My address is {my_dict['address']}")
print(f"My hobby is {my_dict["hobbies"][0]}")

# print out read
print(my_dict["hobbies"][0][:4])
# print out movies
print(my_dict["hobbies"][1][9:])
# print out hiking
print(my_dict["hobbies"][-2][3:])
# print out playing game
print(my_dict["hobbies"][-1][:-1])