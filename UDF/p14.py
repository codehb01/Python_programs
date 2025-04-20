# Program 14 : Demonstrate passing and returning a List to/from a user defined function.

def squaringList(numbers):
    result =[]
    for i in numbers:
        result.append(i**2)
    return result

myList = [1,2,3,4,5]
print("Before Squaring:",myList)
print("After squaring:",squaringList(myList))

