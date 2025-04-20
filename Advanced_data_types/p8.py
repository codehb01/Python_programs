# Program 8 : Add elements of List2 in List1, then display the updated List
List1 = []
List2 = []

size1 = int(input("Enter the size of List1: "))
for i in range(size1):
    value = input(f"Enter value {i+1} for List1: ")
    List1.append(value)

size2 = int(input("Enter the size of List2: "))
for i in range(size2):
    value = input(f"Enter value {i+1} for List2: ")
    List2.append(value)

# Add elements of List2 to List1
List1.extend(List2)

print("\nUpdated List1 after adding elements of List2:")
print(List1)
