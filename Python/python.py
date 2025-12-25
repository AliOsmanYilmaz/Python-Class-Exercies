
# Python class exercies

class Animal:
    eyeColor = ""

    def __init__(self,name,age):
        self.name = name
        self.age = age  

    def sound(self):
        return ""          


class Dog(Animal):
    eyeColor = "brown"

    def sound(self):
        return "Hauv Hauv"


class Cat(Animal):
    eyeColor = "green"

    def sound(self):
        return "Meow meow"


a = -1
b = -1
name = ""
age = 0
eyeColor = ""

while a != 0:
    print("0 - Exit")
    print("1 - Dog")
    print("2 - Cat")

    try:
        a = int(input("Your choice: "))
    except ValueError:
        print("Please enter a number (0, 1 or 2).")
        continue

    if a == 0:
        print("Exiting...")


    elif a == 1:
        dog1 = Dog("",0)
        b = -1
        while b != 0:
            print("Dog selected")
            print("0 - Exit")
            print("1 - Set dog name")
            print("2 - Set dog age")
            print("3 - Set dog eye color")
            print("4 - Get dog name")
            print("5 - Get dog age")
            print("6 - Get dog eye color")
            print("7 - Dog sound")

            try:
                b = int(input("Your choice: "))
            except ValueError:
                print("Please enter a number (between 0-6).")
                continue

            if b == 1:
                name = input("Name: ")
                dog1.name = name

            elif b == 2:
                age = int(input("Age: "))
                dog1.age = age

            elif b == 3:
                eyeColor = input("Eye color: ")
                dog1.eyeColor = eyeColor

            elif b == 4:
                print("Dog Name : ",dog1.name)

            elif b == 5:
                print("Dog Age : ",dog1.age)    

            elif b == 6:
                print("Eye color : ",dog1.eyeColor)    

            elif b == 7:
                print("Dog says",dog1.sound())  

            else:
                print("Wrong choice")      


    elif a == 2:

        cat1 = Cat("",0)
        b = -1
        while b != 0:
            print("Cat selected")
            print("0 - Exit")
            print("1 - Set cat name")
            print("2 - Set cat age")
            print("3 - Set cat eye color")
            print("4 - Get cat name")
            print("5 - Get cat age")
            print("6 - Get cat eye color")
            print("7 - Cat sound")

            try:
                b = int(input("Your choice: "))
            except ValueError:
                print("Please enter a number (between 0-6).")
                continue

            if b == 1:
                name = input("Name: ")
                cat1.name = name

            elif b == 2:
                age = int(input("Age: "))
                cat1.age = age

            elif b == 3:
                eyeColor = input("Eye color: ")
                cat1.eyeColor = eyeColor

            elif b == 4:
                print("Cat Name : ",cat1.name)

            elif b == 5:
                print("Cat Age : ",cat1.age)    

            elif b == 6:
                print("Eye color : ",cat1.eyeColor)    

            elif b == 7:
                print("Cat says",cat1.sound())  

            else:
                print("Wrong choice")  


    else:
        print("Wrong choice.")
    
       