# Program 19 : Write an object oriented program to demonstrate working of default and parameterized constructors
class Student:
    def __init__(self,name="John Doe",age=20):         #default constructor 
        self.name=name
        self.age=age

    def display(self):          #parameterized constructor
        print("Name: ",self.name)
        print("Age: ",self.age)

s1 = Student()
print("Using Default Constructor")
s1.display()

print("\nUsing parameterized constructor")
s2 = Student("Harshal",20)
s2.display()