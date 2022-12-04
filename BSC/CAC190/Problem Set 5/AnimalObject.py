# Dhruv Patel
# 11/14/2022
# CAC190
# Problem 16
# Animal Object-Oriented

class Animal:


    def __init__(self, n):
        self.name = n

    # Walk Method    
    def walk(self):
        print(self.name,'is walking')  

class Bird(Animal):  

    # Fly Method 
    def fly(self):
        print(self.name, 'is flying')
    
    # Sing Method
    def sing(self):
        print(self.name, 'is singing')


def main():
    cat = Animal('Felix')
    cat.walk()
    cardinal = Bird('Larry')
    cardinal.walk()
    cardinal.fly()
    cardinal.sing()

    
main()
