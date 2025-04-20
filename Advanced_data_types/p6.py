# Program 6 : Check for a given value in the LIST; display total count of occurrences along with the index positions of each occurrence
myList = []
indexOcc = []
occurrence = 0

size = int(input("Enter size of the list: "))

for i in range(size):
    value = input("Enter the values of the list: ")
    myList.append(value)

print("\nList entered:", myList)

toFind = input("Enter value to be checked in list: ")

for index in range(len(myList)):
    if myList[index] == toFind:
        indexOcc.append(index)
        occurrence += 1

if occurrence > 0:
    print(f"\n'{toFind}' found {occurrence} time(s) at index/indices: {indexOcc}")
else:
    print(f"\n'{toFind}' not found in the list.")
