num = int(input("Enter number for factorial: "))
i = 1
result = 1

while i <= num:
    result *= i
    i += 1

print(result)