sum=0
num = int(input("Enter a number: "))
for no in range(1, num + 1):
    if no % 2==0:
        sum +=no
print(sum)