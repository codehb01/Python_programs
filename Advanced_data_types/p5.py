# Program 5 : Write a Python program to Display the count of elements of different data types present in a LIST.
myList = []
countStr = 0
countInt = 0
countFloat = 0

s = int(input("Enter the size of the list: "))

for i in range(s):
    val = input("Enter a value: ")
    try:
        val = int(val)
    except ValueError:
        try:
            val = float(val)
        except ValueError:
            pass
    myList.append(val)

# Count types
for item in myList:
    if isinstance(item, int):
        countInt += 1
    elif isinstance(item, float):
        countFloat += 1
    elif isinstance(item, str):
        countStr += 1

print("\nYour list:", myList)
print("Count of integers:", countInt)
print("Count of floats:", countFloat)
print("Count of strings:", countStr)
