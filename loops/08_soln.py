# num = int(input("Enter any number: "))
# # is_prime = True
# if num > 2:
#     for n in range(2,num):
#         if (num % n)==0:
#             print("Is not prime")
#             break
#         else:
#             print("It's a prime")

num = int(input("Enter any number: "))
if num < 2:
    print("It's not a prime")
elif num==2:
    print("It's a prime")
else:
    for n in range(2,num):
        if num % n == 0:
            print("It's not a prime")
            break
    else:
            print("It's a prime")