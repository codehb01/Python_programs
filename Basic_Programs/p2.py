# Accept the range from the user and then display all prime numbers between the given range.

lastNum = int(input("Enter the last number of the range: "))
for i in range(2, lastNum + 1):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i, end=" ")
