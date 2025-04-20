# Progam 16: Write a program to demonstrate multiple exceptions handling, specifically, NameError, IndexError, and ZeroDivisionError.

try:
    # NameError example
    print("Accessing an undefined variable:")
    print(unknown_var)  # This will raise NameError

except NameError:
    print("Caught a NameError: Variable is not defined.\n")

try:
    myList = [1,2,3,4]
    print("Accessing an index out of range:")
    print(myList[5])
except IndexError:
    print("Caught an IndexError : List index is out of range\n")

try:
    print("Dividing by zero:")
    result = 10/0
except ZeroDivisionError:
    print("Caught a ZeroDivisionError: Division by zero is not allowed")
