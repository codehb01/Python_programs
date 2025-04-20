# Program 12 : Display Fibonacci series elements (n) using recursive method.
def fiboFunc(x):
    if x <=1:
        return x
    else:
        return fiboFunc(x-1)+ fiboFunc(x-2)
    
nOfTerms = int(input("Number of terms required in fibonacci series: "))

if nOfTerms <= 0:
    print("Please enter positive number")
else :
    print("\nFibonacci Series is")
    for i in range(nOfTerms):
        print(fiboFunc(i), end=" ")
