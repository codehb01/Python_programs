# Program 7 : Perform sorting of LIST elements; Press 1 for ascending order and, Press 2 for descending order.

myList =[]
s = int(input("Enter the size of the list: "))
for i in range(1,s+1):
    values = int(input("Enter the values in the list :"))
    myList.append(values)
choice = int(input("\nEnter the choice of sorting \n1.Ascending\n2.Descending\n"))


def switch(choice):
    if choice == 1:
      myList.sort()
      print(myList)
    elif choice == 2:
       myList.sort(reverse=True)
       print(myList)
    else:
       print("Invalid input!")

switch(choice)