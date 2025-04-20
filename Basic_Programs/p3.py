# Program 3 : Print an n digit number in reverse order

myNums = []
n = int(input("Number of digits to be entered: "))
for i in range(1,n+1):
    nums = int(input("Enter number " + str(i) + ": "))
    myNums.append(nums)
print("List before reversing: ",myNums)
myNums.reverse()
print("Reversed list: ",myNums)