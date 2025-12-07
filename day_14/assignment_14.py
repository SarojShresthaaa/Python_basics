class Animal:
    name = None
    eye = None
    height = None
    weight = None
    color = None

    def get_info(self, name, eye, height, weight, color):
        self.name = name
        self.eye = eye
        self.height = height
        self.weight = weight
        self.color = color
    
    def print_info(self):
        print("Animal Details:")
        print("Name:", self.name)
        print("Eye:", self.eye)
        print(f"Height: {self.height} feet")
        print(f"Weight: {self.weight} kg")
        print("Color:", self.color)



animal_1 = Animal()


name = input("Enter animal name: ")
eye = input("Enter eye color: ")
height = int(input("Enter height (in feet): "))
weight = int(input("Enter weight (in kg): "))
color = input("Enter body color: ")

animal_1.get_info(name, eye, height, weight, color)

animal_1.print_info()
